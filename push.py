#!/usr/bin/python3
import os, sys
dir = ""
cmds = []
for i in os.getcwd().split("/"):
    dir = i
try:
    cmds.append(f"git commit -m \"{sys.argv[1]}\"")
except IndexError:
    cmds.append(f"git commit")
     
cmds.append(f"git push https://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@github.com/nlsg/{dir}")
for cmd in cmds:
    print(cmd)

if input("[c]ommit\n>") == "c":
    for cmd in cmds:
        os.system(cmd)
