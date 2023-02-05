import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "1965973276:AAFngpmzKFyESfcvQscv7S7Dmus7N-nksWI")

API_ID = int(os.environ.get("API_ID", "1923471"))

API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")

STRING = os.environ.get("STRING", "BQC9EiEUYn6I9Lnd1KTOnGDXEKUaxik2U3reg5LiE9FbdXoa2AWHKtVKhnoB91uJvAbgGsOvetC8agr3Uc1uG1ESa-XTXQk34uJyE2rALrtPA5o-DJZHYfFJbmwUZs0C9xdBw0fIiZc2-YB5aE-BfsiJoNpFd3HZ8phwYAhh8PDWNdtPY0exl3XDWcBW50Smh7PVEQlwjeWPja3jqWLCNd7E64UBsAUXcCD8TTopvPzkPN_gQYR0QoDER9VMLcmb9QlIn81lgVNVMhIL2_8Owh39bHQmJ5cC5FUkDeXh7E82jD3IKtCOpmT0-dzFK5Z0r-yuapVOs_89m66-vTDDyUZdN11fzQA")


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
