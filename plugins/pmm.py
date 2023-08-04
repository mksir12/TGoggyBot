from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

MOVIEGROUP = {"https://t.me/kmcrp_movie"}

@Client.on_message(filters.private | filters.text)
async def no_pm(client, message):

btn = InlineKeyboardButton("Join Here 💡", url=MOVIEGROUP)

    await.reply_message(Hey {message.from_user.mention}\n\nYou Can't get movies from here. Request on our movie group. To join click the join button below 👇, reply_markup=InlineKeyboardMarkup(btn))
