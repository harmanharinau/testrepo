"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "You are not dead. You are still here. You have no love for me now. Okay .. you're not changed like you used to be..🙂" 
CONTACT = "<b>ᴏᴡɴᴇʀ ›› ʜᴇʏ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴏᴜʀ ʙᴏᴛ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ʙᴇʟᴏᴡ</b>"
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


@Client.on_message(filters.command("contact", COMMAND_HAND_LER) & f_onw_fliter)
async def contact(_, message):
    await message.reply_text(CONTACT)
    buttons = [
            [
                InlineKeyboardButton('💠 ᴄʜᴀɴɴᴇʟ 💠', url='https://t.me/cynitebots')
            ],
            [
                InlineKeyboardButton('♻️ ʜᴇʟᴘ ♻️', url=f"https://t.me/{temp.U_NAME}?start=help")
            ]
            ]
reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(ping.CONTACT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)

@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("zsearcherbot", COMMAND_HAND_LER) & f_onw_fliter)
async def Zsearcherbot(_, message):
    await message.reply_text(ZSEARCHERBOT)


