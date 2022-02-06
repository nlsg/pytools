#!/usr/bin/python 
import socket
p = print
HOST = "192.168.43.66"
PORT = 9998

class cmd():
  def battery(self):
    from os import system, popen
    return popen("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep -E 'State|to\ |time|percentage'").read()
  def running_since(self):
    return str(t() - start_time)
  def shell(self, data):
    from os import system, popen
    if data.split(" ")[0] == "sh":
      try:
        return popen("".join(data.split(" ")[1:])).read()
      except IndexError:
        return f"{data} no sh cmd given "


def handle_info(request):
  if request == "bat":
    return cmd().battery()
  if request == "time":
    return cmd().running_since()
  return cmd().shell(request)
  return f"{request} - n/a"

send_function = None
def send(data, info=""):
  p(f"[SEND] - {info}\n\t{data}")
  send_function(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
from time import time as t
start_time = t()
while True:
  conn, addr = s.accept()
  send_function = conn.sendall
  p(f"{addr} - connected")
  with conn:
    while True:
      data = conn.recv(1024)
      if not data: break
      send(handle_info(data.decode("utf-8")).encode("utf-8"))

