#!/usr/bin/python3


'''consts'''
cli = {
     "RED"    : "\033[1;31m"
    ,"BLUE"   : "\033[1;34m"
    ,"CYAN"   : "\033[1;36m"
    ,"GREEN"  : "\033[0;32m"
    ,"RESET"  : "\033[0;0m"
    ,"NORMAL" : "\033[0;0m"
    ,"R"      : "\033[0;0m"
    ,"BOLD"   : "\033[;1m"
    ,"B"      : "\033[;1m"
    ,"REVERSE": "\033[;7m"
    ,"REV"    : "\033[;7m"
    }         

log_config = {
    "format":"[%(asctime)s|%(filename)s|%(funcName)s|%(lineno)d]> %(message)s"
    ,"datefmt":"%I:%M", "level":"logging.INFO"}
''' 
logging.basicConfig(**nut.log_config)
log = logging.warning
'''




'''util funct'''
def info(obj, name="", print_obj=True):
  if name != "": print("name: ", name)
  if print_obj:
    try:
      print("obj: ", obj)
    except:
      print("obj: N/A")
  try:
    print("len: ", len(obj))
  except:
    print("len: N/A")
  try:
    print("type: ", type(obj))
  except:
    print("type: N/A")

def ls_raw(directory): 
  '''list content of a dir
  returns popen object
  for output in listformat use ls
  '''
  import os
  return os.popen(f"ls {directory}")
def ls(directory):
  '''for raw popen output use ls_raw'''
  return ls_raw(directory).read().split("\n")

def quiet_exit(exit_code=0,msg="",*args,**kwargs):
  '''same as sys.exit() but gives no stdout'''
  import sys
  print(msg,*args,**kwargs)
  sys.stdout = open('/dev/null', 'w')
  sys.stderr = open('/dev/null', 'w')
  sys.exit(exit_code)

def notify(title, msg = "", argstr = "", critical = False, t=None):
  '''send a notification thru notify-send package.'''
  import os
  if critical:
    argstr +=  " --urgency=critical "
  if t != None:
    argstr += f" -t {str(t)}"
  os.system(f"notify-send {argstr} \"{title}\" \"{msg}\"")



def int_input(fail_txt = "input has to be a number!", txt = "enter a number: ", **kwargs):
  '''force usr to input a integer''' 
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

def time_stamp(format="%d-%b_%H-%M"): 
  from datetime import datetime as dt
  return dt.now().strftime(format)

def grep(regex, itterable):
  '''
  grap an itterable object
  wrapper arround re mudule
  '''
  from re import search
  print_res = True
  res = None
  if type(itterable) == type([]):
    res = []
    for itm in itterable:
      if search(regex, str(itm)) != None:
        res.append(itm)
  elif type(itterable) == type({}):
    res = {}
    for itm in itterable:
      if search(regex, str(itterable[itm])) != None:
        res[itm] = itterable[itm]
  return res

def cat(file):
    #cat a file
    import os.system
    os.system(f"cat {file}")
# add color feature!

def listing(obj):
  '''listing objects line by line'''
  for i in range(len(obj)):
    try:
      print(f"[{i}] -> {obj[i]}")
    except:
      print(f"[{i}] -> {obj}")

'''contextmanagers'''
from contextlib import contextmanager 

@contextmanager
def attr(*attrs):
  attr_ = []
  for a in attrs:
    attr_.append(cli[a])
  for a in attr_:
    print(a, end="")
  yield None
  print(cli["RESET"], end="")


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
  '''log to a file and stdout'''
  from contextlib import redirect_stdout
  with open(file, "a") as f:
    with redirect_stdout(f):
      print(*args,**kwargs)
  print(cli["GREEN"], f"start loging to {file}")
  print(*args,**kwargs)
  print(f"stop loging to {file}", cli["RESET"])

'''decorators'''
def func_info(func, **kwargs):
  '''dehelp(nut)corator which prints info about the called function'''
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


# list_to_dict = {i : list_[i] for i in range(len(list_))}
