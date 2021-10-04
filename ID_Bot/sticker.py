from pyrogram import Client, filters


@Client.on_message(filters.private & filters.sticker)
async def stickers(_, msg):
    await msg.reply(f"This Sticker's ID is `{msg.sticker.file_id}`", quote=True)
