#!/usr/bin/python3


'''consts'''
cli = {"RED"  : "\033[1;31m"
    ,"BLUE" : "\033[1;34m"
    ,"CYAN" : "\033[1;36m"
    ,"GREEN": "\033[0;32m"
    ,"RESET": "\033[0;0m"
    ,"BOLD" :   "\033[;1m"
    ,"REVERSE": "\033[;7m"
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

def notify(title, msg = "", argstr = "", critical = False):
  '''send a notification thru notify-send package.'''
  import os
  if critical:
    argstr +=  " --urgency=critical "
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

'''context managers'''
from contextlib import contextmanager 
class Curses():
  def __init__(self):
    import curses 
    self.curses = curses
    self.stdscr = curses.initscr()
    self.max_y, self.max_x = self.stdscr.getmaxyx()
  def __enter__(self):
    self.curses.noecho()
    self.curses.cbreak()
    self.stdscr.keypad(True)
    self.curses.curs_set(0)
  def popup(self, title_str=None, coords = ()):
    '''returns a popup_window which is nicely placed on the stdscr''' 
    popup_w = None
    if len(coords) < 4:
      popup_w = self.stdscr.subwin(self.max_y//2, self.max_x//2,self.max_y//4,self.max_x//4)
    else: 
      popup_w = self.stdscr.subwin(*coords)
    popup_w.clear()
    popup_w.box()
    if title_str != None:   popup_w.addstr(0,1,title_str)
    return popup_w

  @contextmanager
  def render(self, wnd):
    #simple clear -> do xy -> refresh contextmanager
    wnd.clear()
    try:
      yield wnd
    finally:
      wnd.refresh()
  def render_win(self, win,content_list,title="",y_start=1):
    '''
    each contentl
    '''
    with self.render(win) as scr:
      scr.box()
      scr.addstr(0,1,title)
      for s in content_list:
        if type(s) == list:
          if type(s[0]) == int:
            scr.addstr(*s)
            continue
          else:
            scr.addstr(y_start,1, *s)
        else:
          scr.addstr(y_start,1, s)
        y_start += 1
  def __exit__(self, type, value, traceback):
    self.curses.nocbreak()
    self.stdscr.keypad(False)
    self.curses.echo()
    self.curses.curs_set(1)
    self.curses.endwin()
  

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
