from test_runner import *
from random import randint
import sys

class_name = 'Fibonacci'


def all_tests(c):
    base_test(c)
    correctness_test(c)
    recursion_depth_test(c)
    single_timeout_test(c)
    multi_timeout_test(c)


@test()
def base_test(c):
    f = c()
    check = f.get_nth_fibonacci(1)
    if check != 0:
        raise TestException('First Fibonacci number should be 0, got ' + str(check))


@test()
def correctness_test(c):
    f = c()
    check = f.get_nth_fibonacci(13)
    if check != 144:
        raise TestException('Thirteenth Fibonacci number should be 144, got ' + str(check))


@test()
def recursion_depth_test(c):
    f = c()
    f.get_nth_fibonacci(1000)


@test()
@timer
def single_timeout_test(c):
    f = c()
    f.get_nth_fibonacci(50)


@test()
@timer
def multi_timeout_test(c):
    f = c()
    for _i in xrange(1000):
        r = randint(1, 30)
        f.get_nth_fibonacci(r)


if len(sys.argv) != 2:
    print 'Provide one path'
    exit(1)
run_tests(sys.argv[1], class_name, all_tests)
