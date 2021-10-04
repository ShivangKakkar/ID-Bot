from pyrogram import Client, filters


@Client.on_message(filters.new_chat_members)
async def welcome(bot, msg):
    bot_id = (await bot.get_me())["id"]
    members = msg.new_chat_members
    for member in members:
        if member.id == bot_id:
            await msg.reply(
                f"Thanks for adding me here! \n\nThis group's ID is `{msg.chat.id}`"
            )
