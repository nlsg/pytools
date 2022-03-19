#!/usr/bin/sh

echo "pidof mpv:   $(pidof mpv)"
echo "pidof mpvd:  $(ls /tmp | grep mpvd.pid)"
echo "pidof webui:" $(lsof -i :5000 | grep python | awk '{print $2}')
echo -e "temp files:\n" $(ls /tmp | grep mpv | sed 's/m/-m/')
