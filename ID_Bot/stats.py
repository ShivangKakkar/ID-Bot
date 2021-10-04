from ID_Bot.database.users_sql import Users, num_users
from ID_Bot.database.chats_sql import Chats, num_chats
from ID_Bot.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(~filters.edited & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(~filters.edited & filters.group, group=2)
async def chats_sql(_, msg: Message):
    if msg.chat:
        q = SESSION.query(Chats).get(int(msg.chat.id))
        if not q:
            SESSION.add(Chats(msg.chat.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(1946995626) & ~filters.edited & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    chats = await num_chats()
    await msg.reply(f"Total Users : {users} \n\nTotal Chats : {chats}", quote=True)
