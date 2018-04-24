from test_runner import *
import sys

function_name = 'find_number_of_repeats'


def all_tests(f):
    empty_substr_test(f)
    empty_s_test(f)
    both_empty_test(f)
    identical_test(f)
    contained_test(f)
    found_test(f)
    not_found_test(f)
    found_timer_test(f)
    not_found_front_timer_test(f)
    not_found_middle_timer_test(f)
    not_found_back_timer_test(f)


@test()
def empty_substr_test(f):
    check = f('', 'abc')
    if check != -1:
        raise TestException('There is no amount of repetition of an empty substring that allows another string to fit within it' +
                  '; given ' + str(check))


@test()
def empty_s_test(f):
    check = f('abc', '')
    if check != 0:
        raise TestException('No repetition is needed to fit an empty string; given ' + str(check))


@test()
def both_empty_test(f):
    check = f('', '')
    if check != 0:
        raise TestException('The null set is a subset of every set, including the null set; given ' + str(check))


@test()
def identical_test(f):
    check = f('abc', 'abc')
    if check != 1:
        raise TestException('Expected 1 since strings are identical, got ' + str(check))


@test()
def contained_test(f):
    check = f('abcdefg', 'bcde')
    if check != 1:
        raise TestException('Expected 1 since s is contained within the substring, got ' + str(check))


@test()
def found_test(f):
    check = f('aabaabaacaabaabaab', 'caabaabaabaabaabaacaabaabaabaabaabaacaabaa')
    if check != 3:
        raise TestException('It takes 3 "aabaabaacaabaabaab" for "caabaabaabaabaabaacaabaabaabaabaabaacaabaa" to fit; given ' +
                  str(check))


@test()
def not_found_test(f):
    check = f('aabaabaacaabaabaa', 'caabaabaabaabaabaacaabaabaabaabaabaacaabaa')
    if check != -1:
        raise TestException('"caabaabaabaabaabaacaabaabaabaabaabaacaabaa" cannot fit in any number of repetitions of ' +
                  '"aabaabaacaabaabaa"; given ' + str(check))


@test()
@timer
def found_timer_test(f):
    string = 'mmsdkja'
    for _i in xrange(10000):
        string += 'hgalkdjflkdmmsdkja'
    string += 'hgalkdjfl'
    check = f('djflkdmmsdkjahgalk', string)
    if check != 10002:
        raise TestException('Expected 10002, got ' + str(check))


s1 = 'mmsdija'
for _i in xrange(10000):
    s1 += 'hgalkdjflkdmmsdkja'
s1 += 'hgalkdjfl'


@test()
@timer
def not_found_front_timer_test(f):
    check = f('djflkdmmsdkjahgalk', s1)
    if check != -1:
        raise TestException('Expected -1, got ' + str(check))


s2 = 'mmsdkja'
for _i in xrange(5000):
    s2 += 'hgalkdjflkdmmsdkja'
s2 += 'hgalkdjfkdmmsdkja'
for _i in xrange(4999):
    s2 += 'hgalkdjflkdmmsdkja'
s2 += 'hgalkdjfl'


@test()
@timer
def not_found_middle_timer_test(f):
    check = f('djflkdmmsdkjahgalk', s2)
    if check != -1:
        raise TestException('Expected -1, got ' + str(check))


s3 = 'mmsdkja'
for _i in xrange(10000):
    s3 += 'hgalkdjflkdmmsdkja'
s3 += 'hgalkejfl'


@test()
@timer
def not_found_back_timer_test(f):
    check = f('djflkdmmsdkjahgalk', s3)
    if check != -1:
        raise TestException('Expected -1, got ' + str(check))


if len(sys.argv) != 2:
    print 'Provide one path'
    exit(1)
run_tests(sys.argv[1], function_name, all_tests)
