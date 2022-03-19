#!/usr/bin/sh

rm /tmp/mpvd.pid
mpv $1 --input-ipc-server=/tmp/mpvd.socket & disown
echo server launched!

