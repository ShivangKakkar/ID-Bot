from pyrogram import Client, filters
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied
from pyrogram.types import Message


@Client.on_message(filters.command("id"))
async def id_(bot: Client, msg: Message):
	if not msg.chat.type == "private":
		main = f"This {msg.chat.type}'s ID is `{msg.chat.id}`"
		if msg.reply_to_message:
			if msg.reply_to_message.from_user:
				main = f"{msg.reply_to_message.from_user.first_name}'s ID is `{msg.reply_to_message.from_user.id}`"
				if msg.reply_to_message.sticker:
					main += f"\n\nThis sticker's id is `{msg.reply_to_message.sticker.file_id}`"
		await msg.reply(main)
	else:
		if len(msg.command) == 1:
			await msg.reply(f"Your Telegram ID is: `{msg.from_user.id}`", quote=True)
		if len(msg.command) == 2:
			try:
				uname = msg.command[1]
				if uname.startswith("@"):
					uname = uname[1:]
				try:
					user = await bot.get_users(uname)
					name = user.mention
					if len(user.first_name) <= 20:
						pass
					elif user.is_bot:
						name = "This Bot"
					else:
						name = "This User"
				except IndexError:
					user = await bot.get_chat(uname)
					name = '@'+user.username if user.username else user.title
				id = user.id
				await msg.reply(f"{name}'s id is `{id}`", quote=True)
			except UsernameInvalid:
				await msg.reply("Invalid Username.", quote=True)
			except UsernameNotOccupied:
				await msg.reply("This username is not occupied by anyone", quote=True)
