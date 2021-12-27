#!/usr/bin/python3
class Nav():
  def __init__(self):
    self.n_rec = 1
    self.keybinding_info = {
       "j, k":" -> Down, Up"
      ,"J, K":" -> PgDn, PgUp"
      ,"q"   :" -> quit and return selected item"
      }
    self.hnd_pointer = self.recursion_hndl

  def navigate(self, iterable):
    self.history = [iterable]
    t = type(iterable)
    if t == dict:
      return self.hnd_pointer(iterable)
    elif t == list:
      list_to_dict = {i : iterable[i] for i in range(len(iterable))}
      return self.hnd_pointer(list_to_dict)
    elif t == str or t == int or t == bool:
      print("can't iterate anymore")

  def recursion_hndl(self, iterable):
    self.history.append(iterable)
    while True:
      choice, info = self.userinput(self.history[len(self.history)-1])
      if info["key"] == 'h' and len(self.history) > 1:
        self.history.pop()
        self.n_rec -= 1
        continue
      else:
        self.history.append(choice)
        self.n_rec += 1
      if (t := type(choice)) != dict and t != list or info["key"] == 'q':
        return self.history[len(self.history)-1]

  def userinput(self, options):
    from nls_util import Curses
    choice = 0
    choices = options
    keys = []
    if (choices_type := type(choices)) == list: 
      keys = [i  for i in range(len(choices))]
      choices_type = "list"
    else:
      keys = list(choices.keys())
    with (c := Curses()):
      in_ = None 
      info = {}
      info.update(self.keybinding_info)
      info["recursion_counter"] = self.n_rec

      def ranger_help(help_dict, coords):
        help_w = c.popup("<help>", coords)
        y,x = help_w.getmaxyx()
        i = 0
        for k in help_dict:
          help_w.addstr(i+2,2,f"{k}\t{help_dict[k]}")
          if i == y-3: break
          i += 1
        help_w.refresh()
        help_w.getch()
        help_w.clear()

      offset = 0
      search_mode = False
      while True:
        c.stdscr.clear()
        pop_w = c.popup(title_str="<ranging>", coords=((c.max_y-4)//2,c.max_x-4,2,2))
        info_w = c.popup(title_str="<info>",   coords=((c.max_y-4)//2,c.max_x-4,(c.max_y//2),2))
        y,x = pop_w.getmaxyx()
        screen_fit = y-3
        for i in range(len(choices)):
          ioff = i + offset
          try:
            type_info = str(type(choices[keys[ioff]])).split("'")[1]
          except IndexError:
            with (f := open("cnav.log", "w+")): f.write(f"{i=}, {ioff=}\n{len(choices)=}, {len(keys)=}")
            type_info = ""
          print_str = f"({type_info}) "
          if type(keys[choice]) == int:
            print_str += "0" if ioff < 10 else ""
          print_str += f"{keys[ioff]} - "
          column_rest = x - (len(print_str) +5)
          print_str += f"{str(choices[keys[ioff]])[:column_rest]}"
          print_str += "..." if len(str(choices[keys[ioff]])) >= column_rest else ""
          info["print_str"] = len(print_str)
          pop_w.addstr(i+1,1,print_str, c.curses.A_REVERSE if choice == ioff else c.curses.A_NORMAL)
          if i == y-3: break

        pop_w.refresh()
        info["yx_pop_w"] = (y,x)
        y,x = info_w.getmaxyx()
        info["yx_info_w"] = (y,x)
        pop_w.refresh()

        info_w.addstr(1,1,f"{choice}/{len(choices)-1}, {in_=}, n_rec={info['recursion_counter']}")
        info_w.addstr(1,x//2,"| h,j,k,l -> move, q -> return")
        for i in range(x-2):  info_w.addstr(2,1+i,"-")
        info_w.addstr(2,2,f"<{keys[choice]}>")

        def str_splitter(str_, n): return [str_[i:i+n] for i in range(0, len(str_), n)]
        preview_strs = str_splitter(str(choices[keys[choice]]).replace('\n', ' '),x-2)
        for i in range(len(preview_strs)):
          info_w.addstr(3+i,1,preview_strs[i])
          if i == y-5: break

        info_w.refresh()
        if in_ != None:
          in_ = pop_w.getkey()
        info["key"] = in_
        if   in_ == 'k' and choice > 0:
          if (choice-offset) == 0: 
            offset -= 1
          choice -= 1
        elif in_ == 'j'  and choice < len(choices)-1 :
          if (choice-offset) == screen_fit:
            offset += 1
          choice += 1
        elif in_ == 'K':
          if (choice-(screen_fit*2)) > 0:
            choice -= screen_fit
            offset -= screen_fit
          else:
            choice = offset = 0
        elif in_ == 'J':
          if (choice+(screen_fit*2)) < len(choices)-1:
            choice += screen_fit
            offset += screen_fit
          else:
            choice = len(choices)-1
            offset = choice - screen_fit
        elif in_ == 'l': break
        elif in_ == 'h': break
        elif in_ == 'q': break
        elif in_ == '?': ranger_help(info, (len(info)*2,c.max_x-8,4,4))
        elif in_ == '/': search_mode = True
        elif in_ == None: in_ = 'k' ; continue
    
        pop_w.clear()  
        info_w.clear()  
    return choices[keys[choice]], info

nav = Nav().navigate

from os import popen
def list_dir(cwd, just_files=True):
  cmd  = f"ls -als {cwd}"
  cmd += "| awk '{print $2 \" | \" $10}'" 
  cmd += "| grep " 
  cmd += "" if just_files else "-v "
  cmd += "-E \"^-\""
  cmd = cmd.replace('\n', ' ')
  print(cmd)
  pop = popen(cmd)
  pop = pop.read().split("\n")
  return pop
  data = [i.split("|") for i in pop]
  return data

data = list_dir(popen("pwd").read())
nav(data)
data = list_dir(popen("pwd").read(), False)
nav(data)
# pseudo code "cnav":
# | d | 10 | eter ui                  |
# | d | 20 | user hits '/'            |
# | - | 30 | show search bar          | toggle search_mode       |
# | - | 35 | render page              |
# | - | 40 | user types a char        | if char == Enter goto 70
# | - |    |                          | else ad char to query
# | - | 45 | update search query      |
# | - | 50 | filter list              |
# | - | 60 | goto 35                  |
# | - | 70 | return item under curser |
