import pytest
import os
import sys


import mypracticefuncs as myf


def testgenerate_prime_list_empty():

    target = []
    number = 0
    primes = myf.generate_prime_list(number)
    assert(primes == target)

    number = 1
    primes = myf.generate_prime_list(number)
    assert(primes == target)

    number = -10
    primes = myf.generate_prime_list(number)
    assert(primes == target)


def testgenerate_prime_list_non_empty():
    number = 20
    target = [2, 3, 5, 7, 11, 13, 17, 19]
    primes = myf.generate_prime_list(number)
    assert(primes == target)


def test_str2range():
    d = ","

    s = f"1{d}10{d}2"
    target = [*range(1,10,2)]
    myrange = myf.str2range(s,d)
    assert( myrange == target )

    s = f"1{d}10"
    target = [*range(1,10,1)]
    myrange = myf.str2range(s,d)
    assert( myrange == target )

    s = f"1{d}10{d}"
    target = [*range(1,10,1)]
    myrange = myf.str2range(s,d)
    assert( myrange == target )

    s = f" 1   {d}   10   {d}    2   "  
    target = [*range(1,10,2)]
    myrange = myf.str2range(s,d)
    assert( myrange == target )


def test_str2range_mismatched_delimiter():
    with pytest.raises(ValueError):
        d = ","
        s = f"1|10|2"
        target = [*range(1,10,2)]
        myrange = myf.str2range(s,d)
    
 
def test_str2range_insufficient_number_of_args1():
    with pytest.raises(myf.InvalidInputError):
        d = ","
        s = f"1{d}{d}"
        target = [*range(1,10,2)]
        myrange = myf.str2range(s,d)


 
def test_str2range_insufficient_number_of_args2():
    with pytest.raises(myf.InvalidInputError):
        d = ","
        s = f"1{d}{d}2"
        target = [*range(1,10,2)]
        myrange = myf.str2range(s,d)
