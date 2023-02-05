import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "1965973276:AAFngpmzKFyESfcvQscv7S7Dmus7N-nksWI")

API_ID = int(os.environ.get("API_ID", "1923471"))

API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
