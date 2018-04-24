## Disclaimer

These automated correctors do <b>NOT</b> sandbox
the programs they are running (e.g.: a user can
submit arbitrary code that will run on the host).
As such it is <b>HIGHLY</b> recommended that the
correctors be run in a VM to prevent attacks on
the host computer.

## Creating an automated corrector
### Java
Subclass from AbstractTests<T> where T is the
abstract class whose implementation is to be
tested. This class' constructor should take 3
arguments that are passed to AbstractTests: aClass,
path, and packagePath.

aClass: a Class object of T

Path: the path to the folder containing the .java
files to test (i.e.: the implementations of T)

Package path: the package path (needs to be the
same in all .java files implementing T)

Write tests (annotate with @Test [default timeout
is 10s; not customizable currently]). If you would
like a test to be timed, annotate with @Timed
(order does not matter).

Within a test, to log an error message, throw a new
Error and the framework will associate it with the
test from which it originated.

### Python
<b>The Python automated corrector only works on
Linux!</b>

from test_runner import *

Write tests (annotate with @test() [default
timeout is 10s; to set a different timeout,
@test(timeout=\<timeout in sec\>)]). If you would
like a test to be timed, annotate with @timed
(order matters and @timed should come after
@timed). Each test must take one argument: the
class or function to be tested (if it is a class,
you need to create an instance of it in the test).

Within a test, to log an error message, raise a
TestException and the framework will associate it
with the test from which it originated.

run_tests takes 3 arguments: path, entity_name
name, and tests.

Path: the path to the folder containing the .py
files to test

Entity name: the name of the class or function to
retrieve from the .py files for testing

<b>All .py files to be tested must implement the
entity, as named, and the expected interface
(class) or signature (function)!</b>

Tests: a function that runs all of the tests
you've written (would be nice to automatically
register all functions annotated with @test and
generate this function, but I haven't figured out
how)

Like the tests, this universal test function must
take one argument: the class or function to be
tested.
