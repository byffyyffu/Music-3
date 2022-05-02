# Copyright (C) 2021 By AmortMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    SUDO_USERS,
    BOT_TOKEN,
    UPDATES_CHANNEL,
)

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبآ عزيزي↤「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」!**\n
🤖 **[ 𝐌𝐔𝐒𝐈𝐂 🎵](https://t.me/VFF35) **
**※ انا اسمي كوبرا استطيع تشغيل الاغاني ولفيديوهات في المكالمه الصوتيه**

※ لتعرف شلون تشغلني وتعرف على الاوامر انقر على زر اوامر التشغيل  📚  !

**※ طريقة تفعيلي بكروبك ازا ماتعرف انقر على  » ❓طريقة التفعيل !**

**البوت معرب بل كامل كل الشكر لمستخدمين بوتات سورس كوبرا**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "※ مبرمج السورس ※",
                        url=f"https://t.me/QABNADLIB",
                    )
                ],
                [
                    InlineKeyboardButton("※ تواصل المحظورين ※", url=f"https://t.me/sdaasfs_bot"),
                    InlineKeyboardButton("※ مساعد المبرمج ※", url=f"https://t.me/Silawy112"),
                ],
                [InlineKeyboardButton("※ قناة الشروحات ※", url=f"https://t.me/VFF34")],
                [InlineKeyboardButton("※❓ طريقة التفعيل ※", callback_data="cbhowtouse")],
                [InlineKeyboardButton("※ الاوامر بالعربي ※", callback_data="https://t.me/VFF34/17")],                 
                [
                    InlineKeyboardButton("※📚 اوامر التشغيل ※", callback_data="cbcmds"),
                    InlineKeyboardButton("※ لتنصيب مدفوع ※", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "※ جروب البوت ※", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "※ قناة البوت ※", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton("※ اضافه البوت اللي مجموعتك ※", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **🫀الدليل الأساسي لاستخدام هذا البوت:🫀 

 1 ↤🫀 أولاً ، أضفني إلى مجموعتك 🫀

 2 ↤🫀 بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي 🫀

 3 ↤🫀 بعد ترقيتي ، اكتب .تحديث في المجموعة لتحديث بيانات المشرفين 🫀

 3 ↤🫀 أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب .استدعاء لدعوة حساب المساعد 🫀

 4 ↤🫀 قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى 🫀

 5 ↤🫀 في بعض الأحيان، يمكن تساعدك إعاده تحميل البوت باستخدام الأمر  .تحديث في إصلاح بعض المشكلات 🫀

 🫀 إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب .غادر ثم اكتب .استدعاء مرة أخرى 🫀

المطورين @VFF35 @VFF34 @QABNADLIB @Silawy112**

⚡ __بواسطة {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("☆ الاوامر الأساسية ☆", callback_data="cbcmds"),
                ],[
                    InlineKeyboardButton("※رجوع※", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **منور يرايق [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **تحياتي لكم من المبرمج سيف كوبرا**

**مطورين السورس** @VFF35 @VFF34 @QABNADLIB @Silawy112

⚡ __بواسطة {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("※ الاوامر بالعربي ※", callback_data="cbadmin"),
                    InlineKeyboardButton("※ اوامــر المطــور ※", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("※ الاوامر بالانجليزي ※", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("☆رجوع☆", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ها هي الأوامر الاساسية:
ملحوظه الاوامر المعربه تكتب كما هي بدون شرط او اي شي
» /mplayاو «تشغيل» 「اسم الأغنية / رابط」تشغيل الصوت mp3
✦┅━╍━╍╍━━╍━━╍━┅✦
 » /vplay او «فيد» 「اسم / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
✦┅━╍━╍╍━━╍━━╍━┅✦
» /stream «بث» لتشغيل بث مباشر من اليوتيوب
✦┅━╍━╍╍━━╍━━╍━┅✦
 » /vstream او «بث» 「رابط」 تشغيل فيديو مباشر من اليوتيوب
✦┅━╍━╍╍━━╍━━╍━┅✦
» /stop  او «ايقاف» لايقاف التشغيل
✦┅━╍━╍╍━━╍━━╍━┅✦
» /resume «او لاستئناف التشغيل«كمل  
✦┅━╍━╍╍━━╍━━╍━┅✦
» /skip  او «تخطي» تخطي الئ التالي
✦┅━╍━╍╍━━╍━━╍━┅✦
» /pauseاو «مؤقتا» ايقاف التشغيل موقتآ
✦┅━╍━╍╍━━╍━━╍━┅✦
» /vmute «اخرس» لكتم البوت
✦┅━╍━╍╍━━╍━━╍━┅✦
» /vunmute «اتكلم» للغاء كتم البوت
✦┅━╍━╍╍━━╍━━╍━┅✦
 ⚡ 🌀
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☆رجوع☆", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""  
 ※ ها هي الأوامر بالانجليزي ※

✦┅━╍━╍╍━━╍━━╍━┅✦
 »/mplay   او «تشغيل» 「اسم الأغنية / رابط」تشغيل الصوت mp3
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /vplay او «فيد» 「اسم / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /stream «او«تشغيل» 「رابط 」تشغيل صوت
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /vstream «او «فيديو» 「رابط」 تشغيل فيديو مباشر من اليوتيوب
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /stop  «او «ايقاف» لايقاف التشغيل
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /resume «او لاستئناف التشغيل«كمل  
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /skip   «او «تخطي» تخطي الئ التالي
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /pause «مؤقتا» ايقاف التشغيل موقتا
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /vmute «لكتم البوت او «كتم
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /vunmute  « او «اتكلم لرفع الكتم عن البوت
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /playlist  «او «الانتظار» ↤ تظهر لك قائمة التشغيل
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /video  «او «تنزيل» + الاسم  تنزيل فيديو من youtube
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /song +  « او« تحميل» الاسم تنزيل صوت من youtube
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /volume  «او «الصوت»+ الرقم لضبط مستوئ الصوت
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /reload  «او «تحديث» لتحديث البوت و قائمة المشرفين
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /userbotjoin  «او «انضم» لاستدعاء حساب المساعد
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /userbotleave « او «غادر» لطرد حساب المساعد 
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /ping «او«تيست» - إظهار حالة البوت بينغ
 ✦┅━╍━╍╍━━╍━━╍━┅✦
 » /alive   او «السورس» إظهار معلومات البوت  (في المجموعه) 
  
✦┅━╍━╍╍━━╍━━╍━┅✦
※ قناة سورس كوبرا 🎵  @VFF35
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("※رجوع※", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""※ ها هي الاوامر  للمطور ※

✦┅━╍━╍╍━━╍━━╍━┅✦
» /rmw  »او «مسح- clean all raw files
✦┅━╍━╍╍━━╍━━╍━┅✦
» /rmd  » او «تنظيف- clean all downloaded files
✦┅━╍━╍╍━━╍━━╍━┅✦
» /sysinfo »او «معلومات- show the system information
✦┅━╍━╍╍━━╍━━╍━┅✦
» /update »او «حدث - update your bot to latest version
✦┅━╍━╍╍━━╍━━╍━┅✦
» /restart «او «ريستارت - restart your bot
✦┅━╍━╍╍━━╍━━╍━┅✦
» /leaveall»او «غادر الكل - order userbot to leave from all group

✦┅━╍━╍╍━━╍━━╍━┅✦
 ※ قناة سورس كوبرا 🎵  @VFF35
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("※رجوع※", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbvamp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""※ ها هي الاوامر  الكامله بالعربي ※ 

✦┅━╍━╍╍━━╍━━╍━┅✦
※ تشغيل + 「اسم الأغنية او / رابط」تشغيل الصوت  mp3
✦┅━╍━╍╍━━╍━━╍━┅✦
※ فيد +  「اسم الفديو او / رابط الفيديو」 تشغيل الفيديو داخل المكالمة  .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ فيديو + لينك + | جودة < 360 - 480- 720 >| » » تشغيل فيديو مباشر من يوتيوب .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ اسكت او ايقاف » »  لايقاف التشغيل .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ مؤقتا » » ايقاف التشغيل موقتآ  .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ كمل  » »  استئناف التشغيل  .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ تخطي » » تخطي الئ التالي  .
✦┅━╍━╍╍━━╍━━╍━┅✦
※  كتم او سكوت  » »   لكتم البوت .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ اتكلم » »  لرفع كتم البوت  .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ الانتظار » » تظهر لك قائمة التشغيل . 
✦┅━╍━╍╍━━╍━━╍━┅✦
※ فيديو + اسم فيديو » » لتحميل فيديوهات من يوتيوب .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ صوت  + اسم اغنية  » لتحميل اغاني mP3 من يوتيوب .  
✦┅━╍━╍╍━━╍━━╍━┅✦
※ بحث » »  اي شيء تريد البحث عنه باليوتيوب .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ ضبط + < رقم 1 - 200 >  » »  الرقم لضبط مستوئ الصوت .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ تحديث » » لتحديث البوت و قائمة المشرفين .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ انضم » »  لاستدعاء حساب المساعد .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ غادر » »  لطرد حساب المساعد .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ تيست او بينج » »  إظهار حالة البوت بينج .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ الوقت » » اظهار الوقت تشغيل البوت . 
✦┅━╍━╍╍━━╍━━╍━┅✦
※ السورس » »  إظهار معلومات البوت . 
✦┅━╍━╍╍━━╍━━╍━┅✦
※ المطور » »  إظهار مطورين البوت .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ الاوامر او اوامراغاني او اغاني » » لعرض قائمه الاوامر في مجموعتك . 

✦┅━╍━╍╍━━╍━━╍━┅✦

※ اوامر  المطور ※
✦┅━╍━╍╍━━╍━━╍━┅✦
※ مسح » » لمسح جميع الملفات المستخدمه .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ تنضيف » »  لتنظيف جميع الملفات المحمله .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ معلومات » » لرؤيه معلومات النظام  البوت .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ حدث » » لتحديث البوت لاخر اصدار من السورس .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ ريستارت » لاعادة تشغيل البوت .
✦┅━╍━╍╍━━╍━━╍━┅✦
※ غادر الكل  » » لمغادره الحساب المساعد لجميع جروبات .

✦┅━╍━╍╍━━╍━━╍━┅✦
※ قناة سورس كوبرا 🎵  @VFF35
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("※رجوع※", callback_data="cbcmds")]]
        ),
    )
           

@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("※ اغلاق ※", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
