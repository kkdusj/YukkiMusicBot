import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["ألمطور","كنج","المبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/dev_kingo0o",
        caption=f"""◍ الزرار الاول: قناه السورس \n◍ الزرار الثاني: هو مبرمج السورس\n√""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "🔮𝐒𝐎𝐔𝐑𝐂𝐄 𝙆𝙄ٍَ𝙉ٍ𝙂🔮", url=f"https://t.me/VC_NE"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "ᯓ˚₊· ͟͟͞͞➳𝑫𝑬𝑽➼𝐾𝐼𝑁𝐺« 𓂄𓆩⍢⃝🇪🇬𝑬𝑳-8𝑫𝑨𝑹●𓆪𓂁", url=f"https://t.me/dev_kingo0o"),
                ],
            ]
        ),
    )
