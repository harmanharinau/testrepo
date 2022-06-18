"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "You are not dead. You are still here. You have no love for me now. Okay .. you're not changed like you used to be..🙂" 
HOW_TO_OWN = "<b>ᴏᴡɴᴇʀ ›› Auto + IMDB + Unlimited Filter Bot. 🥰🥰

An advanced Filter Bot with Unlimited filters, also Support Auto filters and inline Media search Video and File Store etc...

Features :-

›› Nearly unlimited filter
›› Custom IMDb Poster + Details
›› Double Buttons (callbacks)
›› Broadcast 
›› Random Start Pics
›› Inline Media Search
›› Index Files (no user session required)
›› Extra Show Commands (chats, users, disable, enable, invite. etc
›› Force Subscribe
›› Search on imdb
›› Supports all type of filters
›› Can save button filters directly (Rose Bot Feature)
›› Supports multiple PM connections
›› And all other features of a Filter Bot and Media Search Bot 
›› File Store

How to Deploy On Heroku! :

🔗 Tutorial : https://youtu.be/MfUjmZ1mpfc

Dont Forgot To Subscribe ❤️

Deploy Tutorial  ›› https://youtu.be/MfUjmZ1mpfc

A Big Credits To ➡ Adhi</b>"
CHANNEL = "<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> ›› https://youtube.com/channel/UCMzFIpsfTkZfkI-O20o1gww\n\n<b>𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/cynitebots</b>\n\n<b>𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/cynitemovies</b>"
ZSEARCHERBOT = "<b>𝙱𝙾𝚃 ›› https://t.me/zsearcherbot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
    

@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("zsearcherbot", COMMAND_HAND_LER) & f_onw_fliter)
async def Zsearcherbot(_, message):
    await message.reply_text(ZSEARCHERBOT)


@Client.on_message(filters.command("How_To_Own", COMMAND_HAND_LER) & f_onw_fliter)
async def How_To_Own(_, message):
    await message.reply_text(HOW_TO_OWN)

