import pytest
import os
import sys


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


import mypracticefuncs as myf


def test_generate_prime_list_empty():

    target = []
    number = 0
    primes = myf._generate_prime_list(number)
    assert(primes == target)

    number = 1
    primes = myf._generate_prime_list(number)
    assert(primes == target)

    number = -10
    primes = myf._generate_prime_list(number)
    assert(primes == target)


def test_generate_prime_list_non_empty():
    number = 20
    target = [2, 3, 5, 7, 11, 13, 17, 19]
    primes = myf._generate_prime_list(number)
    assert(primes == target)

