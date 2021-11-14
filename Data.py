from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Chibai {}

{} Hian ka lo lawm a che

MizoStrings bot hi i ring lo anih chuan, 
1) Message hi chhiar zawm duh tawh suh.
2) he chat hi delete rawh

I la chhiar zel tho maw?
Pyrogram leh telethon string session siam nan min hmang thei a. A hnuaia button khu hmet la han chhiar belh teh !

By @MizoStrings
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Session Siam tan ang", callback_data="generate")],
        [InlineKeyboardButton(text="Phêkpui ah kir ang", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Session Siam tan ang", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Session Siam tan ang", callback_data="generate")],
        [InlineKeyboardButton("Bot Status leh a dang te", url="https://t.me/MizoStrings")],
        [
            InlineKeyboardButton("Engtia hman tur nge?", callback_data="help"),
            InlineKeyboardButton("Keimahni", callback_data="about")
        ],
        [InlineKeyboardButton("Bot ṭha dang te", url="https://t.me/MizoStrings")],
    ]

    # Help Message
    HELP = """
**Commands hman theih te** 

/about - Bot chungchang hriatna
/help - Ṭanpuina
/start - Bot tih nun na
/generate - Session string siam na
/cancel - Hnathawh lai tih tawp na
/restart - Tih that leh na
"""

    # About Message
    ABOUT = """
**He bot chanchin hi** 

Telegram bot pyrogram leh telethon string session  siam na, by @MizoStrings

Discussion : [Mizo Bots Talk](https://t.me/MzBotsTalk)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @MizoStrings
    """
