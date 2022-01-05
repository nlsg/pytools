#!/usr/bin/bash
  ps -e -o pid,vsz=MEMORY -o comm \
  | awk '{print $2","$1",\""$3"\"]"}' \
  | column -s "," -o "," -t \
  | sort -rg \
  | sed '/^0/d' \
  | awk '{print "["$0}' \
  | cnav.py
