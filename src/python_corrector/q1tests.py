from test_runner import *
from random import randint
import sys

class_name = 'Fibonacci'


def all_tests(c, s):
    base_test(c, s)
    correctness_test(c, s)
    recursion_depth_test(c, s)
    single_timeout_test(c, s)
    multi_timeout_test(c, s)


@test()
def base_test(c, s):
    f = c()
    check = f.get_nth_fibonacci(1)
    if check != 0:
        s.add_err('First Fibonacci number should be 0, got ' + str(check))


@test()
def correctness_test(c, s):
    f = c()
    check = f.get_nth_fibonacci(13)
    if check != 144:
        s.add_err('Thirteenth Fibonacci number should be 144, got ' + str(check))


@test()
def recursion_depth_test(c, s):
    f = c()
    try:
        f.get_nth_fibonacci(1000)
    except RuntimeError as e:
        s.add_err(e.message)


@test()
@timer
def single_timeout_test(c, s):
    f = c()
    f.get_nth_fibonacci(50)


@test()
@timer
def multi_timeout_test(c, s):
    f = c()
    for _i in xrange(1000):
        r = randint(1, 30)
        f.get_nth_fibonacci(r)


if len(sys.argv) != 2:
    print 'Provide one path'
    exit(1)
run_tests(sys.argv[1], class_name, all_tests)
