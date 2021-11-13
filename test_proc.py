#!/usr/bin/pyton3
import concurrent.futures as cf
import time as t
import nls_util as nut

def func(num):
    del_t = num * .4
    t.sleep(del_t)
    print(f"proc_input -> {num} sleep -> {del_t}")
    return del_t

@nut.func_info
def deced(num):
    return func(num)

mode = ""

def proc_test():
    BOOL = False
    with nut.Timer("whole"):
        for i in range(6):
            print(f"[{i % 2}] -> {'func' if BOOL else 'deced'}")
            with nut.Timer("do procs"):
                with cf.ProcessPoolExecutor() as exec:
                    secs = [5,4,3,2,1]
                    if BOOL:
                        res = exec.map(func, secs)
                    else:
                        res = exec.map(deced, secs)
            BOOL ^= 1

def math_load():
    it, it_, n = 0, 0, 10
    while True:
        try:
            print(f"[{__name__}- {(it := it + 1)}][{it_}] {(n := n*n):.2e}")
            input("q - for quit")
        except OverflowError:
            it, n = 0, 10
            it_ += 1

def fib():
    it, n, n_ = 0, 0, 1
    while True():
        print(n)
        nth = n + n_
        # update values
        n = n_
        n_ = nth
        it += 1


    '''
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
       print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    # generate fibonacci sequence
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
    '''
