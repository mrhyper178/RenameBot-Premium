import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','1965973276:AAFngpmzKFyESfcvQscv7S7Dmus7N-nksWI')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Total User:- {total_user()}\nBot :- @asurenamebot\nCreater :- @Asuran2p0\nLanguage :-Python3\nLibrary :- Pyrogram\nServer :- Render\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
