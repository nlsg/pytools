#!/usr/bin/python
from sys import path; path.insert(1, '/home/nls/py/cnav')
from cnav import Nav

cont = ["channel1","channel2","channel3"]
n = Nav()
def construct_right_w(coords: set, preview: list):
  if n.choice == 0:
    return ["abc","def",cont[n.choice]]
  if n.choice == 1:
    return ["abcd","def",cont[n.choice], f"{n.info['sr']=}"]
  return ["zyx",cont[n.choice]]

import mpv
p = print

player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True)

player.fullscreen = True
player.loop_playlist = 'inf'
# Option access, in general these require the core to reinitialize
player['vo'] = 'gpu'


@player.on_key_press('q')
def my_q_binding():
    print('THERE IS NO ESCAPE')

player.play("https://www.youtube.com/watch?v=-5KAN9_CzSA")
player.wait_for_playback()
p(f"{player['time-pos']=}")
p("player started")

n.construct_right_window_f = construct_right_w
# n.navigate(cont)
