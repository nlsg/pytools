#!/usr/bin/python3

from datetime import datetime as dt

'''consts'''
cli = {"RED"  : "\033[1;31m",
    "BLUE" : "\033[1;34m",
    "CYAN" : "\033[1;36m",
    "GREEN": "\033[0;32m",
    "RESET": "\033[0;0m",
    "BOLD" :   "\033[;1m",
    "REVERSE": "\033[;7m"
    }

'''util funct'''
def notify(title, msg, argstr = "", critical = False):
    import os
    if critical:
        argstr +=  " --urgency=critical "
    os.system(f"notify-send {argstr} \"{title}\" \"{msg}\"")
    gt.fetch_args()

def int_input(fail_txt = "input has to be a number!", txt = "enter a number: ", **kwargs):
    in_ = 0
    check_for_max = False
    if "max" in kwargs:
        check_for_max = True
        print(f"kwargs[max] -> {kwargs['max']}")
    while True:
        try:
            in_ = int(input(txt))
            if check_for_max == True:
                if in_ <= kwargs["max"]:
                    break
                print("input exceeded the maximum")
                continue
            else:
                break
        except ValueError:
            print(fail_txt)
    return in_

def time_stamp(): return dt.now().strftime("%d-%b_%H-%M")

def grep(regex, itterable, **kwargs):
    import re
    print_res = True
    if "print" in kwargs: print_res = kwargs["print"]
    for itm in itterable:
        if re.search(regex, itm) != None:
            if print_res: print(itm)
            yield itm
    

def cat(file):
    import os
    os.system(f"cat {file}")
# add color feature!

def listing(obj):
    for i in range(len(obj)):
        try:
            print(f"[{i}] -> {obj[i]}")
        except:
            print(f"[{i}] -> {obj}")

class Timer():
    def __init__(self, name = ""):
        self.name = name
        self.stamps = [["name","stamp_t","begin_t"]]
    def __enter__(self):
        import time as t
        self.start_t = t.time()
        self.last_stamp = self.start_t
    def __exit__(self, exc_type, exc_value, exc_traceback):
        import time as t
        print(cli["GREEN"] + f"[{self.name}] took: {round(t.time() - self.start_t, 3)}s" + cli["RESET"])
        if len(self.stamps) > 1:
            listing(self.stamps)
    def stamp(self, name):
        import time as t
        self.stamps.append([name, t.time() - self.last_stamp, t.time() - self.start_t])
        self.last_stamp = t.time()

def tee(file,*args, **kwargs):
    from contextlib import redirect_stdout
    with open(file, "a") as f:
        with redirect_stdout(f):
            print(*args,**kwargs)
    print(cli["GREEN"], f"start loging to {file}")
    print(*args,**kwargs)
    print(f"stop loging to {file}", cli["RESET"])

'''decorators'''
def func_info(func, **kwargs):
    col = "GREEN"
    if "col" in kwargs:
        col = kwargs["col"]
    def dec_func(*args, **kwargs):
        ret = func(*args, **kwargs)
        info =  f"[{func.__name__}] {args}"
        info += (f"\n  kwargs: {kwargs}" if len(kwargs) != 0 else "")
        info += f"\n ({type(ret)}) -> {ret}"
        print(cli[col], info, cli["RESET"])
        return ret
    return dec_func

