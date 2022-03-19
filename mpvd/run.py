#!/usr/bin/env python
from os import system 
from sys import argv
from threading import Thread

PATH = "./web_ui/flaskblog.py"
LOGFILE = "/tmp/mpvd.log"
CMD_STR = f"tail -f {LOGFILE}"

def start_func():
  system(f"python3 {PATH} &> {LOGFILE}")

def process_args(argv):
  if argv[1] == "-k" or argv[1] == "--kill":
    system("kill $(pidof mpv)")
    system("rm /tmp/mpvd*")
    exit(0)

if __name__ == "__main__":
  """
  the only argument accepted is used to filter the log via grep
  """
  Thread(target=start_func).start()
  if len(argv) > 1:
    if argv[1][0] != "-":
      CMD_STR += f" | grep {argv[1]}"
    else:
      process_args(argv)
  system(CMD_STR)
