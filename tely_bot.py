import sys, psutil, os
import time as t
sys.path.insert(1, "/home/nls/py/pytools/")
import nls_util as nut
from tely import send_message as sm

import logging
import telegram.ext
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from threading import Thread


# while True:
#   t.sleep(300)
#   battery_percent = psutil.sensors_battery().percent
#   power_now = open("/sys/class/power_supply/BAT0/power_now").read()
#   power_now = float(int(power_now[:-1]) / 1000000)
#   info_str = f"{battery_percent=:.4f}%\n{power_now=}w"
#   print(info_str)
#   sm(info_str)

logging.basicConfig(
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = open("/home/nls/py/nls_notify_bot.token").read()[:-1]

def start(update: Update, context: CallbackContext) -> None:
  """Send a message when the command /start is issued."""
  user = update.effective_user
  update.message.reply_markdown_v2(
    fr'Hi {user.mention_markdown_v2()}\!',
    reply_markup=ForceReply(selective=True),
  )

def help_command(update: Update, context: CallbackContext) -> None:
  """Send a message when the command /help is issued."""
  update.message.reply_text('Help!')

def echo(update: Update, context: CallbackContext) -> None:
  """Echo the user message."""
  segments = update.message.text.split(" ")
  update.message.reply_text(str(segments))
  if segments[0] == "get" and segments[1] == "info":
    battery_percent = psutil.sensors_battery().percent
    power_now = open("/sys/class/power_supply/BAT0/power_now").read()
    power_now = float(int(power_now[:-1]) / 1000000)
    info_str = f"{battery_percent=:.4f}%\n{power_now=}w"
    update.message.reply_text(info_str)

def get_info_command(update: Update, context: CallbackContext) -> None:
  usr_info = update.effective_user.user
  update.message.reply_text(f"got signal {usr_info.mention_markdown_v2()}")

def main() -> None:
  updater = Updater(TOKEN)
  dispatcher = updater.dispatcher
  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(CommandHandler("help", help_command))
  dispatcher.add_handler(CommandHandler("get", get_info_command))
  dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
  
  updater.start_polling()
 
  updater.idle()


main_thread = Thread(target=main)
from nls_util_assets.json_test_data import json_test_data0  as jtd0 
import nls_util as nut
import requests as req


res = req.get("https://jsonplaceholder.typicode.com/comments").json()


if __name__ == "__main__": main()
