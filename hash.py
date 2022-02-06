#!/usr/bin/env python3
import bcrypt

password = b"super secret password"
if __name__ == "__main__":
  from sys import argv
  try:
    password = argv[1]
  except IndexError:
    pass
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  with open("pw.hash", "w") as f:
    f.write(hashed)
  with open("pw.hash","r") as f:
    hashed_ = f.readlines()
  if bcrypt.checkpw(password, hashed_):
      print("It Matches!")
  else:
      print("It Does not Match :(")

