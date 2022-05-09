# Copyright (C) 2021 By Amort Music-Project
# Commit Start Date 20/10/2021
# Finished On 28/10/2021

import re
import asyncio

from config import ASSISTANT_NAME, BOT_USERNAME, IMG_1, IMG_2
from driver.filters import command, other_filters
from driver.queues import QUEUE, add_to_queue
from driver.amort import call_py, user
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:70]
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(command(["غل", "تشغيل", "ينوم", "ندق", "ودي", "لخديوي", "mplay", f"mplay@{BOT_USERNAME}"]) & other_filters)
async def play(c: Client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• القائمة", callback_data="cbmenu"),
                InlineKeyboardButton(text="• إغلاق", callback_data="cls"),
            ]
        ]
    )
    if m.sender_chat:
        return await m.reply_text("you're an __Anonymous Admin__ !\n\n» revert back to user account from admin rights.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"خطاء:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 لاستخدامي ، يجب أن أكون ** مشرف ** مع ** الصلاحيات التالية **:\n\n» ❌ __حذف الرسائل__\n» ❌ __دعوة المستخدمين__\n» ❌ __ادارة المكالمات المرئية__\n\n** يتم تحديث البيانات ** تلقائيًا بعد أن تقوم بترقيتي **"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "ليس لدي صلاحية:" + "\n\n» ❌ __ادارة المكالمات المرئية__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "ليس لدي صلاحية:" + "\n\n» ❌ __حذف الرسائل__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("ليس لدي صلاحية:" + "\n\n» ❌ __اضافة المستخدمين__")
        return
    try:
        ubot = await user.get_me()
        b = await c.get_chat_member(chat_id, ubot.id)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **محظور في المجموعة** {m.chat.title}\n\n» **قم بإلغاء حظر المستخدم حساب المساعد أولاً إذا كنت تريد استخدام هذا البوت**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **فشل userbot في الانضمام**\n\n**السبب**: `{e}`")
                return
        else:
            try:
                pope = await c.export_chat_invite_link(chat_id)
                pepo = await c.revoke_chat_invite_link(chat_id, pope)
                await user.join_chat(pepo.invite_link)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **فشل userbot في الانضمام**\n\n**السبب**: `{e}`"
                )

    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **جاري تنزيل الصوت...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **تمت إضافة المقطع إلى قائمة الانتظار »** `{pos}`\n\n🏷 **الاسم:** [{songname}]({link})\n💭 **المجموعة:** `{chat_id}`\n🎧 **طلب بواسطة:** {m.from_user.mention()}",
                    reply_markup=keyboard,
                )
            else:
             try:
                await suhu.edit("🔄 **يتم التشغيل...**")
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().local_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_2}",
                    caption=f"💡 **بداء تشغيل الموسيقئ**\n\n🏷 **الاسم:** [{songname}]({link})\n💭 **المجموعة:** `{chat_id}`\n💡 **الحالة:** `شغال`\n🎧 **طلب بواسطة:** {requester}",
                    reply_markup=keyboard,
                )
             except Exception as e:
                await suhu.delete()
                await m.reply_text(f"خطاء:\n\n» {e}")
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» الرد على ** ملف صوتي ** أو ** أكتب شي للبحث**"
                )
            else:
                suhu = await c.send_message(chat_id, "🔎 **Searching...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **لم يتم العثور على نتائج**")
                else:
                    songname = search[0]
                    url = search[1]
                    veez, ytlink = await ytdl(url)
                    if veez == 0:
                        await suhu.edit(f"❌ تم اكتشاف مشاكل في youtube-dl\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Audio", 0
                            )
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_1}",
                                caption=f"💡 **تمت إضافة المقطع إلى قائمة الانتظار »** `{pos}`\n\n🏷 **الاسم:** [{songname}]({url})\n💭 **المجموعة:** `{chat_id}`\n🎧 **طلب بواسطة:** {requester}",
                                reply_markup=keyboard,
                            )
                        else:
                            try:
                                await suhu.edit("🔄 **يتم التشغيل...**")
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                    ),
                                    stream_type=StreamType().pulse_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                                await suhu.delete()
                                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                await m.reply_photo(
                                    photo=f"{IMG_2}",
                                    caption=f"💡 **بداء تشغيل الموسيقئ**\n\n🏷 **الاسم:** [{songname}]({url})\n💭 **المجموعة:** `{chat_id}`\n💡 **الحالة:** `شغال`\n🎧 **طلب بواسطة:** {requester}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await suhu.delete()
                                await m.reply_text(f"خطاء: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "» الرد على ** ملف صوتي ** أو ** أكتب شي للبحث**"
            )
        else:
            suhu = await c.send_message(chat_id, "🔎 **جاري البحث...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("❌ **لم يتم العثور على نتائج**")
            else:
                songname = search[0]
                url = search[1]
                amort, ytlink = await ytdl(url)
                if amort == 0:
                    await suhu.edit(f"❌ تم اكتشاف مشاكل في youtube-dl\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=f"{IMG_1}",
                            caption=f"💡 **تمت إضافة المقطع إلى قائمة الانتظار »** `{pos}`\n\n🏷 **الاسم:** [{songname}]({url})\n💭 **المجموعة:** `{chat_id}`\n🎧 **طلب بواسطة:** {requester}",
                            reply_markup=keyboard,
                        )
                    else:
                        try:
                            await suhu.edit("🔄 **يتم التشغيل...**")
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_2}",
                                caption=f"💡 **بداء تشغيل الموسيقئ**\n\n🏷 **الاسم:** [{songname}]({url})\n💭 **المجموعة:** `{chat_id}`\n💡 **الحالة:** `شغال`\n🎧 **طلب بواسطة:** {requester}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await suhu.delete()
                            await m.reply_text(f"خطاء: `{ep}`")


# stream is used for live streaming only


@Client.on_message(command(["باشر", "stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(c: Client, m: Message):
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• القائمة", callback_data="cbmenu"),
                InlineKeyboardButton(text="• اغلاق", callback_data="cls"),
            ]
        ]
    )
    if m.sender_chat:
        return await m.reply_text("you're an __Anonymous Admin__ !\n\n» revert back to user account from admin rights.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 لاستخدامي ، يجب أن أكون ** مشرف ** مع ** الصلاحيات التالية **:\n\n» ❌ __حذف الرسائل__\n» ❌ __دعوة المستخدمين__\n» ❌ __ادارة المكالمات المرئية__\n\n** يتم تحديث البيانات ** تلقائيًا بعد أن تقوم بترقيتي **"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "ليس لدي صلاحية:" + "\n\n» ❌ __ادارة المكالمات المرئية__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "ليس لدي صلاحية:" + "\n\n» ❌ __حذف الرسائل__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("ليس لدي صلاحية:" + "\n\n» ❌ __اضافة مستخدمين__")
        return
    try:
        ubot = await user.get_me()
        b = await c.get_chat_member(chat_id, ubot.id)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **محظور في المجموعة** {m.chat.title}\n\n» **قم بإلغاء حظر المستخدم حساب المساعد أولاً إذا كنت تريد استخدام هذا البوت**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **فشل userbot في الانضمام**\n\n**السبب**: `{e}`")
                return
        else:
            try:
                pope = await c.export_chat_invite_link(chat_id)
                pepo = await c.revoke_chat_invite_link(chat_id, pope)
                await user.join_chat(pepo.invite_link)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **فشل userbot في الانضمام**\n\n**السبب**: `{e}`"
                )

    if len(m.command) < 2:
        await m.reply("» أعطني رابط مباشر / من اليوتيوب للتشغيل")
    else:
        link = m.text.split(None, 1)[1]
        suhu = await c.send_message(chat_id, "🔄 **تتم المعالجة انتظر قليلآ...**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            amort, livelink = await ytdl(link)
        else:
            livelink = link
            amort = 1

        if amort == 0:
            await suhu.edit(f"❌ تم اكتشاف مشاكل في youtube-dl\n\n» `{livelink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **تمت إضافة المقطع إلى قائمة الانتظار »** `{pos}`\n\n💭 **المجموعة:** `{chat_id}`\n🎧 **طلب بواسطة:** {requester}",
                    reply_markup=keyboard,
                )
            else:
                try:
                    await suhu.edit("🔄 **يتم الانضمام انتظر قليلآ...**")
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            livelink,
                        ),
                        stream_type=StreamType().live_stream,
                    )
                    add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                    await suhu.delete()
                    requester = (
                        f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                    )
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        caption=f"💡 **[موسيقئ مباشرة]({link}) بداء التشغيل**\n\n💭 **المجموعة:** `{chat_id}`\n💡 **الحالة:** `شغال`\n🎧 **طلب بواسطة:** {requester}",
                        reply_markup=keyboard,
                    )
                except Exception as ep:
                    await suhu.delete()
                    await m.reply_text(f"خطاء: `{ep}`")

