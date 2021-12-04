#!/usr/bin/python3

def tely_send(msg,api_token="/py/nls_notify_bot.token"):
  import requests, os.path
  bot_token = open(os.path.expanduser('~') + api_token).read()[:-1]

  req_str = f"https://api.telegram.org/bot{bot_token}/getUpdates"
  bot_chat_id  = requests.get(req_str).json()["result"][0]["message"]["from"]["id"]
  
  req_str = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text="
  req_str += msg

  return requests.get(req_str).json()

if __name__ == "__main__":
  import sys
  import nls_util as nut

  if len(sys.argv) == 2:
    tely_send(sys.argv[1])
  elif len(sys.argv) == 3:
    tely_send(sys.argv[1], sys.argv[2])
  else:
    usage = nut.cli["BOLD"] + "usage" + nut.cli["RESET"] + f" {sys.argv[0]} "
    help_str  = usage + "[msg] - default api path=/py/nls_notify_bot.token\n"
    help_str += usage + "[api-key-file] [msg] -  path to a file containing the api key of the telegram bot (relative to home directory)"
    print(help_str)


