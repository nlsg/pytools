#!/usr/bin/python
p = print
def get_connection():
  import socket
  HOST = "192.168.43.66"
  PORT = 9998
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  return s

if __name__ == "__main__":
  from sys import argv
  conn = get_connection()
  s = conn.sendall
  r = conn.recv
  def sr(data):
    s(data.encode("utf-8"))
    return r(1024).decode("utf-8")

  try:
    data = argv[1]
  except IndexError:
    data = "hallo socket"
  while (data := input(">")) != '\n':
    p(sr(data))
  
