#!/usr/bin/python3
import nls_util as nut
notify = nut.notify
class Nav():
  def __init__(self):
    # ui/ux related
    self.c = nut.Curses()
    self.opts = {
       "print_list_numbers":True
      ,"endless_search_mode":True
      ,"horizontal_split":False
      ,"main_w_title":"<cnav>"
      ,"hilight_attr":self.c.curses.A_REVERSE
      }
    self.keybinding_info = {
       "j, k":" -> Down, Up"
      ,"J, K":" -> PgDn, PgUp"
      ,"q"   :" -> quit and return selected item"
      }
    self.n_rec = 1
    self.visual_markpoint = 0
    self.break_list = ['q', 'h', 'l', '\n',"KEY_LEFT","KEY_RIGHT"]
    self.hnd_pointer = self.recursion_hndl
    self.logfile = "cnav.log"
    self.mode = "normal"

  def log(self, log_data="", title=""):
    with (f := open(f"{self.logfile}", "a")):
      import time as t
      log_str = t.strftime("%m-%d %H:%M:%S") + f" - {title} >\n"
      log_str += log_data.replace("\n", "\n  ") + "\n\n"
      f.write(log_str)
      notify(f"log", "log written!")

  def navigate(self, iterable):
    c = self.c
    self.c.__enter__()

    if self.opts["horizontal_split"]:
      main_w_coords = ((c.max_y-2)//2,c.max_x-4,1,2)
      info_w_coords = ((c.max_y-2)//2,c.max_x-4,(c.max_y//2),2)
    else:
      main_w_coords = (c.max_y-2,(c.max_x-4)//2,1,2)
      info_w_coords = (c.max_y-2,(c.max_x-4)//2,1,(c.max_x//2))
    c.main_w = c.popup(title_str=self.opts["main_w_title"], coords=main_w_coords)
    c.info_w = c.popup(title_str="<info>",   coords=info_w_coords)

    self.history = [iterable]
    t = type(iterable)
    if t == dict:
      result = self.hnd_pointer(iterable)
    elif t == list:
      list_to_dict = {i : iterable[i] for i in range(len(iterable))}
      result = self.hnd_pointer(list_to_dict)
    elif t == str or t == int or t == bool:
      print("can't iterate anymore")
    self.c.__exit__(None,None,None)
    return result

  def recursion_hndl(self, iterable):
    self.history.append(iterable)
    while True:
      choice, info = self.get_choice(self.history[-1])
      if info["key"] == 'h' and len(self.history) > 1:
        self.history.pop()
        self.n_rec -= 1
        continue
      else:
        self.history.append(choice)
        self.n_rec += 1
      if info["sr"][0] != info["sr"][1] and info["key"] == "q":
        return self.history[-1]
      if (t := type(choice)) != dict and t != list or info["key"] == 'q':
        return self.history[-1]

  def get_choice(self, choices, preview:list=[]):
    c = self.c

    def str_splitter(str_, n): 
      return [str_[i:i+n] for i in range(0, len(str_), n)]
       
    def ranger_help(help_dict, coords):
      help_w = c.popup("<help>", coords)
      y,x = help_w.getmaxyx()
      i = 0
      for k in help_dict:
        help_w.addstr(i+2,2,f"{k}\t{help_dict[k]}".lstrip())
        if i == y-3: break
        i += 1
      help_w.refresh()
      help_w.getch()
      help_w.clear()

    def handle_line_input(key, line):
      if key == None: key = ""
      try:
        input_ord = ord(key)
      except TypeError:
        input_ord = None
      if input_ord == 127 or key == "KEY_BACKSPACE": #delete
        if len(line) == 0:
          self.mode = "normal"
        line = line[:-1]
      elif input_ord == 27: #escape
        line = ""
        self.mode = "normal"
      elif input_ord != None:
        line += key
      return key, line
                                
    choice = 0
    choices_ = choices
    self.len_resdir = len(choices)-1
    user_key = None 
    info = {}
    info.update(self.keybinding_info)
    info.update(self.opts)
    info["recursion_counter"] = self.n_rec
    offset = 0
    user_line = ""
    skip_input_once = False

    def construct_main_w():
      selected_range = (choice,choice)
      if self.mode == "visual":
        if choice <= self.visual_markpoint:
          selected_range = (choice, self.visual_markpoint)
        else:
          selected_range = (self.visual_markpoint, choice)
      info["sr"] = selected_range
      main_strs = [] # contains str or (str,attr) to be drawn for addstr function
      for i in range(len(choices)):
        ioff = i + offset
        type_info = str(type(choices[keys[ioff]])).split("'")[1]
        print_str = f"({type_info}) "
        if self.opts["print_list_numbers"]:
          if type(keys[choice]) == int:
            print_str += "0" if int(keys[choice]) < 10 else ""
          print_str += f"{keys[ioff]} - "
        print_str += str(choices[keys[ioff]]).rstrip()
        if len(print_str) > x-2:
          print_str = print_str[:x-5] + "..."
        # if choice == ioff:
        if selected_range[0] <= ioff <= selected_range[1]:
          main_strs.append([print_str, self.opts["hilight_attr"]])
        else:
          main_strs.append(print_str)
        if i == y-3: break
      if self.mode == "normal":
        main_strs.append([y-1,1,f"({self.len_resdir})"])
      if (self.mode == "search" or user_line != "") and self.mode != "command":
        main_strs.append([y-1,1,f"({self.len_resdir})/{user_line} >",c.curses.A_BOLD if self.mode == "search" else c.curses.A_NORMAL])
      elif self.mode == "command": 
        main_strs.append([y-1,1,f"($):{user_line} >",c.curses.A_BOLD])
      if self.mode == "repl": 
        main_strs.append([y-1,1,f"(>>>):{user_line} >",c.curses.A_BOLD])
      if self.mode == "visual": 
        main_strs.append([y-1,1,f"({selected_range[0]}:{selected_range[1]} /{self.len_resdir})",c.curses.A_BOLD])
      return main_strs

    while True:
      if type(choices) == list: 
        keys = [i  for i in range(len(choices))]
      else:
        keys = list(choices.keys())

      if choice > len(choices)-1:
        choice = offset = 0

      y,x = c.main_w.getmaxyx()
      screen_fit = y-3
      
      # draw main_w (main window)
      c.render_win(c.main_w, construct_main_w(), info["main_w_title"])
      
      info["yx_pop_w"] = (y,x)
      y,x = c.info_w.getmaxyx()
      info["yx_info_w"] = (y,x)

      try:
        user_key_ord = ord(user_key)
      except TypeError as e:
        user_key_ord = "-"
        self.log(f"{e=}\n{user_key=}","user key is special char")

      info_str  = f"{choice}/{len(choices)-1}|in: {user_key}/{user_key_ord}"
      info_str += f"|r: {self.n_rec}|sm: {self.mode}|c: {choice}, o: {offset}"
      line_str = ""
      info_str = str_splitter(info_str,x-2)[0]
      try:
        key_str = f"<{keys[choice]}>"
      except IndexError:
        key_str = "<->"
        self.log("{e=}","info_w key_str error")
      for i in range(x-2):  line_str += "-"
      
      if len(preview) == 0:
        preview_strs = str_splitter(str(choices[keys[choice]]).replace('\n', ' '),x-2)
      else:
        preview_strs = []
        try:
          for i in str(preview[choice]).split('\n'):
            if len(i) > x-2:
              preview_strs += str_splitter(i,x-2)
            else:
              preview_strs.append(i)
        except IndexError:
          preview_strs = str_splitter(str(choices[keys[choice]]).replace('\n', ' '),x-2)

      with c.render(c.info_w) as scr:
        scr.box()
        scr.addstr(1,1,info_str)
        scr.addstr(2,1,line_str)
        scr.addstr(0,1,key_str)
        for i in range(len(preview_strs)):
          c.info_w.addstr(3+i,1,preview_strs[i])
          if i == y-5: break

      # get user_key
      self.log(f"{user_key=}","about to get key")
      if user_key != None and skip_input_once == False:
        try:
          user_key = c.stdscr.getkey()
        except Exception as e:
          self.log(f"{e=}", "get key error")
        self.log(f"{user_key=}","got key")
      else:
        skip_input_once = False
      info["key"] = user_key

      can_scroll_up   = lambda:choice > 0
      can_scroll_down = lambda:choice < len(choices)-1 
      def scroll_up(c=choice,o=offset):
        if (c-o) == 0: o -= 1
        c -= 1
        return c,o
      def scroll_down(c=choice,o=offset,sc=screen_fit):
        if (c-o) == sc: o += 1
        c += 1
        return c,o
      def scroll_page_up(c=choice,o=offset,sc=screen_fit):
        if (c-(sc*2)) > 0:
          c -= sc
          o -= sc
        else:
          c = o = 0
        return c,o
      def scroll_page_down(c=choice,o=offset,sc=screen_fit):
        if (c+(sc*2)) < len(choices)-1:
          c += sc
          o += sc
        else:
          c = len(choices)-1
          o = c - sc
        return c,o

      self.log(f"{self.mode}","about to evalute key")
      if self.mode == "normal":
        if   user_key in ['k',"KEY_UP"] and can_scroll_up():
          choice, offset = scroll_up()
        elif user_key in ['j', "KEY_DOWN"] and can_scroll_down():
          choice, offset = scroll_down()
        elif user_key == 'K':
          choice, offset = scroll_page_up()
        elif user_key == 'J':
          choice, offset = scroll_page_down()
        elif user_key == '?': ranger_help(info, (len(info)*2,c.max_x-8,4,4))
        elif user_key == '/': self.mode = "search"
        elif user_key == ':': self.mode = "command"
        elif user_key == '>': self.mode = "repl"
        elif user_key == 'v': self.mode = "visual"; self.visual_markpoint = choice
        elif user_key == None: user_key = 'k' ; continue
        elif user_key in self.break_list: break
      elif self.mode == "search":
        import re
        user_key, user_line = handle_line_input(user_key, user_line)

        if user_key in ['\n', "KEY_RIGHT", "KEY_LEFT"]:
          if self.opts["endless_search_mode"]:
            user_line = ""
            user_key = ' '
            skip_input_once = True
            break
          else:
            user_line = user_line[:-1]
            self.mode = "normal"
        elif user_key == "KEY_UP" and can_scroll_up():
          choice, offset = scroll_up()
        elif user_key == "KEY_DOWN" and can_scroll_down():
          choice, offset = scroll_down()
        else: #if not enter -> perform re.search
          res_dir = {}
          choices = choices_

          if type(choices) == list:
            choices = {i : choices[i] for i in range(len(choices))}
          for k in choices:
            search = ""
            search = str(k) + str(choices[k])
            try:
              if re.search(user_line,search) != None:
                res_dir[k] = choices[k]
            except re.error as e:
              self.log(f"\nre.error={e}\n{k=}\n{search}")
              res_dir = choices 
              break
          self.len_resdir = len(res_dir)
          if self.len_resdir >= 1:
            choices = res_dir
      elif self.mode == "command":
        user_key, user_line = handle_line_input(user_key, user_line)
        if user_key == '\n': #enter
          self.mode = "normal"
          info["cmd"] = user_line[:-1]
          break
      elif self.mode == "repl":
        user_key, user_line = handle_line_input(user_key, user_line)
        if user_key == '\n': #enter
          self.mode = "normal"
          try:
            eval(user_line[:-1])
          except Exception as e:
            self.log(f"{e=}\n{user_line=}","raised exception while eval")
      elif self.mode == "visual":
        if user_key in ["^[","\n","l","h","v","q"]:
          self.mode = "normal"
          if user_key in ["\n","q"]: break
        elif user_key in["KEY_UP", "k"] and can_scroll_up():
          choice, offset = scroll_up()
        elif user_key in ["KEY_DOWN", "j"] and can_scroll_down():
          choice, offset = scroll_down()
        elif user_key == 'K':
          choice, offset = scroll_page_up()
        elif user_key == 'J':
          choice, offset = scroll_page_down()
        elif user_key == '?': ranger_help(info, (len(info)*2,c.max_x-8,4,4))

    info["choice"] = choice
    self.log(f"{choice=}\n{choices[keys[choice]]=}","get_choice return ->")

    
    if info["sr"][0] != info["sr"][1]:
      return [choices[keys[i]] for i in range(*info["sr"])], info

    return choices[keys[choice]], info


from os import popen
def prep_data(cwd):
  cmd  = f"ls -hals --group-directories-first {cwd}"
  cmd += "|sed 's/ [0-9]*,//;s/^total.*$//' |  column -o \"|\" -t"
  cmd = cmd.replace('\n', ' ')
  pop = popen(cmd).read().split("\n")
  data = [i.split("|") for i in pop]
  return data

class CNav(Nav):
   
  def file_manager_hnd(self, iterable):
    self.log("cnav started!","-----------------------------")
    self.break_list.append('~')
    cwd = popen("pwd").read()[:-1]
    # cwd = "/"
    while True:
      self.opts["main_w_title"] = f"<cnav@{cwd}"
      self.log(f"{cwd=}","prep data")
      dir_content = []
      dir_info = []
      it = 0
      for i in (data := prep_data(cwd)):
        it += 1
        try:
          cwd_ = cwd + "/" + "".join(i[9:]).rstrip()
          if i[1][0] == 'd':
            prog = "ls -a"
          elif i[1][0] == '-':
            prog = "head -n 4"
          try:
            pop = popen(f"{prog} {cwd_}").read()
          except UnicodeDecodeError as e:
            self.log(f"{e=}","popen(head) decode error")
          dir_content.append(" | ".join([
            i[1]
            ,*i[9:]
            ]))
          dir_info.append("\n".join([
            i[1]
            ," ".join([i_.rstrip() for i_ in i[9:]]).strip()
            ," ".join(i[6:9])
            ,pop
            ]))
        except IndexError:
          break
      choice, info = self.get_choice(dir_content,dir_info)
      self.log(f"{data[info['choice']]=}","data reconstruction")
      choice  = choice.split("|")
      choice[-1] = choice[-1].replace(" ","")

      if info["key"] in ['h',"KEY_LEFT"] or choice[-1] == "..":
        self.n_rec -= 1
        cwd = '/'.join(cwd.split('/')[:-1])
        if cwd == "": cwd = "/"
        continue
      elif choice[-1] != ".":
        cwd += ("/" + choice[-1].replace(" ",""))
        # cwd += ("/" + "".join(data[info["choice"]][9:]).split(" ")[-1])
        self.n_rec += 1

      self.log(f"{choice[0]=}", "determing type")
      if choice[0][0] == 'd':
        self.log("","is dir")
      elif choice[0][0] == '-':
        info["cmd"] = "du"
        self.log("","is file")
      else:
        self.log("","is smt. else")

      if "cmd" in info:
        from os import system
        cmd = ""
        if info["cmd"] == "cd":
          self.log(f"{info['cmd']=}","got cmd")
          cmd = f"cd {cwd} && bash"
        elif info["cmd"] == "du":
          choice1, info1 = self.get_choice(["nvim","disk usage","tail"])
          if choice1 == "nvim": 
            cmd = f"nvim {cwd}"
        else:
          cwd = cwd.split('/')
          cwd = '/'.join(cwd[:-1])

        if cmd != "":
          self.c.__exit__(None,None,None)
          system(cmd)
          self.c.__enter__()
            
      elif info["key"] == '~':
        cwd = popen("echo $HOME").read()[:-1]

      if (t := type(choice)) != dict and t != list or info["key"] == 'q':
        return choice

def fm_test():
  nav = CNav()
  nav.hnd_pointer = nav.file_manager_hnd
  nav.opts["print_list_numbers"] = False

  data = prep_data(None)
  print(nav.navigate(data))

def stdin_to_list():
  lines = []
  from ast import literal_eval
  from sys import exit, path
  import os
  path.insert(1, '/home/nls/py/pytools')
  import nls_util as nut
  with open(0) as stdin:
    if not (is_tty := stdin.isatty()):
      lines = [ ln for ln in stdin.readlines()]
    else:
      lines = None

  if lines == None:
    return None
  res = []
  for ln in lines:
    try:
      res.append(list(literal_eval(ln)))
    except ValueError as e:
      print(f"{e=}\n{ln=}")
  return res

if __name__ == "__main__":
  from os import dup2, system
  obj = stdin_to_list()
  tty=open("/dev/tty")
  dup2(tty.fileno(), 0)
  if obj == None:
    print("no stdin")
  nav = Nav()
  nav.opts["endless_search_mode"] = False
  res = nav.navigate(obj)
  for i in res:
    print(f"kill {i[1]}")
    system(f"kill {i[1]}")
  # nav.navigate([123,12,12,"eqwe","asdv",[12,"de",["as",12,43],23],12])

# pseudo code "cnav":
# | 1 | d | get cwd                    |
# | 2 | d | get selection from nav     |
# | 3 |   | if selection == '../' or h | cwd -- |
# | 5 |   | else cwd = cwd + selection |
# | 4 |   | if selection is dir        |
# | 6 |   | if selection is file       |
# | 7 |   | preview file               |

