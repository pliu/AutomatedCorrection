package java_corrector;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.concurrent.CancellationException;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public abstract class AbstractTests<T> {

    private final CLoader<T> cLoader;
    private final ArrayList<NamedConsumer<T>> tests;

    private Stats stats;

    protected AbstractTests(Class<T> tClass, String path, String packagePath) {
        Runtime rt = Runtime.getRuntime();
        try {
            Process p = rt.exec("javac " + path + "\\*.java");
            p.waitFor(300, TimeUnit.SECONDS);
        } catch (IOException | InterruptedException e) {
            System.out.println("Could not compile the .java files: " + e);
            System.exit(1);
        }
        this.cLoader = new CLoader<>(tClass, path, packagePath);
        this.tests = getTests(this.getClass());
    }

    public void runTestsOnClasses() {
        while (cLoader.hasNext()) {
            try {
                CLoader.LoaderOutput<T> o = cLoader.getNext();
                stats = new Stats(o.className);
                for (NamedConsumer<T> test : tests) {
                    test.c.accept(o.obj);
                }
            } catch (CLoader.LoaderError e) {
                stats = new Stats(e.className);
                stats.putErr("Loading class", e.getMessage());
            }
            stats.printStats();
        }
    }

    private NamedConsumer<T> consumerWrapper(Method m) {
        NamedConsumer<T> newNC = new NamedConsumer<>(m.getName(), t -> {
            try {
                m.invoke(null, t);
            } catch (InvocationTargetException e) {
                stats.putErr(m.getName(), e.getCause().getMessage());
            } catch (Exception e) {
                stats.putErr(m.getName(), e.getMessage());
            }
        });
        return newNC;
    }

    private NamedConsumer<T> testWrapper(NamedConsumer<T> nc) {
        NamedConsumer<T> newNC = new NamedConsumer<>(nc.methodName, t -> {
            final ExecutorService executor = Executors.newSingleThreadExecutor();
            final Future future = executor.submit(new Thread(() -> {
                while(!Thread.interrupted()) {
                    try {
                        Thread.sleep(10);
                    } catch (InterruptedException e) {
                        break;
                    }
                }
            }));
            Thread thr = new Thread(() -> {
                nc.c.accept(t);
                future.cancel(true);
            });
            executor.shutdown();
            thr.start();
            try {
                future.get(10, TimeUnit.SECONDS);
            } catch (CancellationException | InterruptedException | ExecutionException e) {

            } catch (TimeoutException e) {
                thr.stop();
                future.cancel(true);
                stats.putErr(nc.methodName, "Timed out");
            }
        });
        return newNC;
    }

    private NamedConsumer<T> timerWrapper(NamedConsumer<T> nc) {
        NamedConsumer<T> newNC = new NamedConsumer<>(nc.methodName, t -> {
            long start = System.nanoTime();
            nc.c.accept(t);
            stats.putTiming(nc.methodName, (System.nanoTime() - start)/1000 + " us");
        });
        return newNC;
    }

    private ArrayList<NamedConsumer<T>> getTests(Class c) {
        ArrayList<NamedConsumer<T>> tests = new ArrayList<>();
        for (Method m : c.getDeclaredMethods()) {
            if (m.getAnnotation(Test.class) != null) {
                NamedConsumer<T> test = consumerWrapper(m);
                if (m.getAnnotation(Timed.class) != null) {
                    test = timerWrapper(test);
                }
                test = testWrapper(test);
                tests.add(test);
            }
        }
        return tests;
    }
}
