import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5567847114:AAGrO_uulshxfHcqc1X7zygDxahRuyY2C4g")

API_ID = int(os.environ.get("API_ID", "8733404"))

API_HASH = os.environ.get("API_HASH", "f19aed00b0c74abed0359016afc1733f")

STRING = os.environ.get("STRING", "AQAaiBkAt9DsH8XO1z9_dxUkBgcLvnAKii6M9A5uFZi3coeUdFVTOPfNzMqjv6PGUgQa3hoE4uAkyEh7E531j1mGHxNBk8b9NSIV0KibnhJLVGsullkw5ge1H_qUoBCLzy3XHC1J_a9SfEu_5j_41cv82B-Ee1D-gF5luTdMe8W2-m77o8JDS8z1zUwS8zgYMyFy7ZSaoC7u49U8YCBARbaRhxThWwcJVtboFgv-BGacEiMYDtU-xHvgX4Zu1TkYLaz_9neSp4Tt__MYGIt8xttL5qYIYWJz42z_agyB0ktWzIujAU-LF7KTn5zVLq4xh-A3WSih4yitslDc2DvCty_GEAcRgwAAAABRsDH9AA")


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
