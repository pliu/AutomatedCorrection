package java_corrector.q1;

public class FibonacciBrute extends Fibonacci {
    @Override
    public long getNthFibonacci(int n) {
        if (n == 0 || n == 1) {
            return 1L;
        }
        return getNthFibonacci(n - 1) + getNthFibonacci(n - 2);
    }
}
