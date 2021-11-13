#!/usr/bin/pyton3
from multiprocessing import Process
from threading import Thread
from contextlib import redirect_stdout
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time as t
import nls_util as nut
import os
from datetime import datetime

def proc_test():
    bool_ = False
    with nut.Timer("whole"):
        for i in range(6):
            print(f"[{i % 2}] -> {'func' if bool_ else 'deced'}")
            with nut.Timer("do procs"):
                with cf.ProcessPoolExecutor() as exec:
                    secs = [5,4,3,2,1]
                    if bool_:
                        res = exec.map(func, secs)
                    else:
                        res = exec.map(deced, secs)
            bool_ ^= 1
'''pandas'''

def net_load(n_tests):
    lns = []
    for _ in range(n_tests):
        with open("bench_net_load.txt", "r") as f:
            lns = f.readlines()
        for ln in lns:
            os.system(f"tuxi {ln}")

def math_load(n_tests):
    it, it_, it__, n = 0, 0, 0, 10
    while True:
        if it_ == n_tests:
            it_ = 0; it__ += 1
            if it__ == 10:
                break
        try:
            print(f"[math_load - {(it := it + 1)}][{it_}][{it__}] {(n := n*n):.2e}\n")
        except OverflowError:
            it, n = 0, 10
            it_ += 1

def fib(n_tests):
    it, n, n_ = 0, 0, 1
    while True:
        print(f"[fib- {(it := it + 1)}] {n}")
        nth = n + n_
        # update values
        n = n_
        n_ = nth
        it += 1
        if it == n_tests:
            break

def delay_func(time):
    t.sleep(time)
    print(f"[delay_function - {time}s]")

def do_benchmark(func = math_load, args_ = (10,), n_tests = 10, n_processes = 8):
    cols = []
    for u in range(n_tests):
        cols.append(f"tst{u}")
    cols.append("avg")

    ts_seq, ts_th, ts_proc = [], [], []

    with nut.Timer("[do_benchmark] timer"):
        for i in range(n_tests):
            print(nut.cli["BLUE"])
            with open(f"seq_bench_{i}.log", "w") as f:
                with redirect_stdout(f):
                    t_ = t.time()
                    for _ in range(n_processes):
                        func(*args_)
            ts_seq.append(t.time() - t_)

            print(nut.cli["GREEN"] + f"[{func.__name__} - seq] took {ts_seq[-1]:.3f}")
            t_ = t.time()
            threads = []
            with open(f"th_bench_{i}.log", "w") as f:
                with redirect_stdout(f):
                    for _ in range(n_processes):
                        p = Thread(target = func, args = args_)
                        p.start()
                        threads.append(p)
                    for p in threads:
                        p.join()
            ts_th.append(t.time()-t_)

            print(nut.cli["CYAN"] + f"[{func.__name__} - th] took {ts_th[-1]:.3f}")
            t_ = t.time()
            processes = []
            with open(f"proc_bench_{i}.log", "w") as f:
                with redirect_stdout(f):
                    for _ in range(n_processes):
                        p = Process(target = func, args = args_)
                        p.start()
                        processes.append(p)
                    for p in processes:
                        p.join()
            ts_proc.append(t.time()-t_)

            print(nut.cli["BLUE"] + f"[{func.__name__} - proc] took {ts_proc[-1]:.3f}")
            print(f"[do_benchmark] iteration {i} finished")
            def average(ts):
                t_ = 0
                for t__ in ts:
                    t_ += t__
                return t_/len(ts)
            if i == n_tests - 1:
                ts_seq.append(average(ts_seq))
                ts_th.append(average(ts_th))
                ts_proc.append(average(ts_proc))

    data = np.array([ts_seq, ts_th, ts_proc])
    rows = ["sequential program", "multithreaded program", "multiple processes"]
    return pd.DataFrame(data, rows, cols)

cores, n_tests = 8, 1
seperator = pd.DataFrame([[0]],["math"], [""])
seperator1 = pd.DataFrame([[0]],["fib"], [""])
seperator2 = pd.DataFrame([[0]],["net"], [""])
bench_math = do_benchmark(math_load, (1000,), n_tests, cores)
bench_fib = do_benchmark(fib, (900,), n_tests, cores)
bench_net = do_benchmark(net_load, (2,), n_tests, cores)
df = pd.concat([seperator, bench_math, seperator1, bench_fib, seperator2, bench_net])
if (in_ := input("[p]lot\n>")) == "p":
    df.plot()
    plt.show()
