# if you can read this, this meant you use code from Ubot | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Ubot and Ram doesn't care about credit
# at least we are know as well
# who Ubot and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Ubot | Ram Team
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from . import *

@Client.on_message(filters.command("cjoin", [""]) & filters.user(DEVS) & ~filters.me)
@Ubot(["join"], "")
async def join(client: Client, message: Message):
    tex = message.command[1] if len(message.command) > 1 else message.chat.id
    g = await message.reply_text("`Processing...`")
    try:
        await client.join_chat(tex)
        await g.edit(f"**Successfully Joined Chat ID** `{tex}`")
    except Exception as ex:
        await g.edit(f"**ERROR:** \n\n{str(ex)}")


@Ubot(["leave"], "")
async def leave(client: Client, message: Message):
    xd = message.command[1] if len(message.command) > 1 else message.chat.id
    xv = await message.reply_text("`Processing...`")
    try:
        await xv.edit_text(f"{client.me.first_name} has left the group, bye!!")
        await client.leave_chat(xd)
    except Exception as ex:
        await xv.edit_text(f"**ERROR:** \n\n{str(ex)}")


@Ubot(["leaveallgc"], "")
async def kickmeall(client: Client, message: Message):
    tex = await message.reply_text("`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await tex.edit(
        f"**Successfully left {done} Groups, Failed to left {er} Groups**"
    )


@Ubot(["leaveallch"], "")
async def kickmeallch(client: Client, message: Message):
    ok = await message.reply_text("`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await ok.edit(
        f"**Successfully left {done} Channel, failed to left {er} Channel**"
    )


add_command_help(
    "join",
    [
        [f"kickme","Leave group!!."],
        [f"leaveallgc", "leave semua group."],
        [f"leaveallch", "leave semua channel."],
        [f"join [Username]", "mengundang seseorang untuk join."],
        [f"leave [Username]", "mengeluarkan seseorang dari group."],
    ],
)
