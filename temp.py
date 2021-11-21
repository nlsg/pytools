def a():
    import time as t
    it = 0
    while True:
        t.sleep(1)
        with open("/tmp/tmp_py_try","w+") as f:
            f.write(f"blabla {it=}\n")
            print(f"file writen! {it=}")
        it += 1

a()



os.system("cat /tmp/tmp_py_try")

import os

import sys



