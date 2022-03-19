#!/usr/bin/env python
from python_mpv_jsonipc import MPV
from sys import path; path.insert(1, '/home/nls/py/pytools'); import nls_util as nut
from sys import path; path.insert(1, '/home/nls/py/cnav')   ; from cnav import nav 
from sys import path; path.insert(1, '/home/nls/py/batd')   ; from daemon_class import Daemon 

def notify(msg):
  nut.notify(msg)
  with open("/tmp/mpvd.log", "a") as f:
    f.write(f"{msg}\n")

class MpvDaemon(Daemon):
  def __init__(self):
    self.pidfile = "/tmp/mpvd.pid"
    self.command = None

  def init(self):
    self.kill()
    self.restart()

  def run(self):
    from os import system, popen
    pop = popen(f"mpv ~/pytools/mpvd/Asheru__Judo_Flip.mp3 --input-ipc-server=/tmp/mpvd.socket")
    while True:
      pass

  def kill(self):
   from os import popen
   if (pid := get_mpv_pid()):
     popen(f"kill {' '.join(pid)}").read()
   self.stop()


class Mpv(MPV):
  def __init__(self, ytdl=True, start_mpv=False, ipc_socket="/tmp/mpvd.socket"):
    MPV.__init__(self, ytdl=ytdl, start_mpv=start_mpv, ipc_socket=ipc_socket)

  def is_playing(self):
    return self.core_idle

  def toggle(self):
    self.pause = not self.core_idle

  def get_player_status(self):
    try:
      return self.percent_pos
    except BrokenPipeError:
      return "error occurred, mpv probably not running"

  def play_file(self, file):
    self.command("loadfile",file)
    self.toggle()

  def help(self,subject="properties"):
    from sys import path; path.insert(1, '/home/nls/py/cnav')
    from cnav import nav
    if subject:
      print(nav([*vars(self)[subject]]))
    else:
      print(nav(vars(self)))


class MpvTests():
  def toggle_feature(self):
    import time as t
    mpv = Mpv()
    while True:
      if input("(t)oggle mpv?\n>") == "t":
       mpv.toggle()

  def toggle_daemon(self):
    if get_mpv_pid():
      if input("mpvd is running\n\r(k)ill (a)bort\n\r>") == "k":
        MpvDaemon().kill()
    else:
      if input("mpvd is not running\n\r(i)nit (a)bort\n\r>") == "i":
        MpvDaemon().init()



import time as t
class MpvCtrl():
  def __init__(self):
    self.init_mpv()
    self.start_time = t.time()
    self.auth = False
    self.update_counter = 0

  from contextlib import contextmanager 
  @contextmanager
  def try_with_mpv(self):
    try:
      yield None
    except BrokenPipeError:
      self.init_mpv()
      yield None

  def init_mpv(self):
    #raise exception if no mpv instance is found
      from os import path
      if path.isfile("/tmp/mpv.socket") and get_mpv_pid() != None:
        self.mpv = Mpv(ytdl=True)
        notify("got pid")
      else:
        self.mpv = Mpv(start_mpv=True, ytdl=True)
        notify("creating instance")

  def authenticate(self):
    self.auth = True

  def is_auth(self):
    return self.auth

  def get_counter(self):
    self.update_counter += 1
    from datetime import datetime
    time_str = datetime.utcfromtimestamp(t.time() - self.start_time).strftime('%Y-%m-%d %H:%M:%S')
    return str(time_str).split(" ")[1]

  def get_battery(self):
    import psutil
    battery = psutil.sensors_battery()
    plugged = "charging" if battery.power_plugged else "discharging"
    return f"{battery.percent:.5}% | {plugged}"


def get_mpv_pid():
  from os import popen
  try:
    pid = popen("pidof mpv").read()
    pid = pid[:-1].split(" ")
    int(pid[0])
  except ValueError:
    return None
  return pid



def main():
  from sys import path; path.insert(1, '/home/nls/py/cnav')
  from cnav import Nav
  from os import popen
  nav = Nav()
  try:
    mpv = Mpv(start_mpv=True)
  except ConnectionRefusedError:
    MpvDaemon().init()
  song = nav.navigate(popen("ls ~/sd/music/hiphop").read().split("\n"))[0][0]
  song = song.replace(" ", "\ ")
  print(song)
  mpv.play(f"~/sd/music/hiphop/{song}")

if __name__ == "__main__":
  main()


# # mpv.command("set_property", "pause", self.get_mpv_pid())

# # @mpv.property_observer("time-pos")
# def time_getter(name, value):
#   print(f"{name}: {value}")

# # After you have an MPV, you can read and set (if applicable) properties.
# # mpv.volume # 100.0 by default
# mpv.volume = 60

# # Bind to key press events with a decorator
# @mpv.on_key_press("space")
# def space_handler():
#   notify("pressed space")
# # You can also observe and wait for properties.
# @mpv.property_observer("core-idle")
# def handle_eof(name, value):
#   print(f"core-idle: {value}")

# @mpv.property_observer("filename")
# @mpv.property_observer("playlist-pos")
# def handle_eof(name, value):
#   print(f"name is: {value}")

