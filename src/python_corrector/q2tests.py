from test_runner import *
from random import randint
import sys

function_name = 'find_minimum_loss'


def all_tests(f):
    empty_test(f)
    one_element_test(f)
    standard_test(f)
    no_solution_test(f)
    negative_test(f)
    duplicate_test(f)
    timing_test(f)


@test()
def empty_test(f):
    check = f([])
    if check != 0:
        raise TestException('Min loss with an empty array should be 0, got ' + str(check))


@test()
def one_element_test(f):
    check = f([1])
    if check != 0:
        raise TestException('Min loss with an array of length 1 should be 0, got ' + str(check))


@test()
def standard_test(f):
    check = f([10, 5, 7, 2, 3, 6])
    if check != 1:
        raise TestException('Min loss of [10, 5, 7, 2, 3, 6] should be 1, got ' + str(check))


@test()
def no_solution_test(f):
    check = f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if check != 0:
        raise TestException('Min loss of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] should be 0, got ' + str(check))


@test()
def negative_test(f):
    check = f([15, 13, -4, 4, 6, 7, -5, 8])
    if check != 1:
        raise TestException('Min loss of [15, 13, -4, 4, 6, 7, -5, 8] should be 1, got ' + str(check))


@test()
def duplicate_test(f):
    check = f([8, 4, 2, 9, 5, 3, 8, 10, 0])
    if check != 1:
        raise TestException('Min loss of [8, 4, 2, 9, 5, 3, 8, 10, 0] should be 1, got ' + str(check))


a = []
for _i in xrange(100000):
    a.append(randint(0, 100000))


@test()
@timer
def timing_test(f):
    f(a)


if len(sys.argv) != 2:
    print 'Provide one path'
    exit(1)
run_tests(sys.argv[1], function_name, all_tests)
