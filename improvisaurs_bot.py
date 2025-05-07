{\rtf1\ansi\ansicpg1251\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww27360\viewh16080\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from telegram import Update, ReplyKeyboardMarkup\
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes\
import random\
\
# \uc0\u1054 \u1073 \u1086 \u1079 \u1085 \u1072 \u1095 \u1080 \u1083  \u1058 \u1086 \u1082 \u1077 \u1085  \u1095 \u1077 \u1088 \u1077 \u1079  \u1101 \u1085 \u1074 \
from dotenv import load_dotenv\
import os\
\
load_dotenv()\
BOT_TOKEN = os.getenv("BOT_TOKEN")\
\
\
# \uc0\u1057 \u1087 \u1080 \u1089 \u1082 \u1080  \u1076 \u1072 \u1085 \u1085 \u1099 \u1093 \
nominations = [\
    "\uc0\u1051 \u1091 \u1095 \u1096 \u1080 \u1081  \u1083 \u1086 \u1075 \u1083 \u1072 \u1081 \u1085 ",\
    "\uc0\u1051 \u1091 \u1095 \u1096 \u1080 \u1081  \u1084 \u1086 \u1085 \u1086 \u1083 \u1086 \u1075 ",\
    "\uc0\u1060 \u1080 \u1083 \u1100 \u1084 , \u1074  \u1082 \u1086 \u1090 \u1086 \u1088 \u1099 \u1081  \u1085 \u1080 \u1082 \u1090 \u1086  \u1085 \u1077  \u1074 \u1077 \u1088 \u1080 \u1083 ",\
    "\uc0\u1060 \u1080 \u1083 \u1100 \u1084 , \u1082 \u1086 \u1090 \u1086 \u1088 \u1099 \u1081  \u1084 \u1099  \u1093 \u1086 \u1090 \u1077 \u1083 \u1080  \u1073 \u1099  \u1089 \u1090 \u1077 \u1088 \u1077 \u1090 \u1100  \u1080 \u1079  \u1087 \u1072 \u1084 \u1103 \u1090 \u1080 ",\
    "\uc0\u1057 \u1072 \u1084 \u1099 \u1081  \u1085 \u1077 \u1083 \u1077 \u1087 \u1099 \u1081  \u1087 \u1086 \u1074 \u1086 \u1088 \u1086 \u1090 ",\
    "\uc0\u1051 \u1091 \u1095 \u1096 \u1077 \u1077  \u1074 \u1086 \u1087 \u1083 \u1086 \u1097 \u1077 \u1085 \u1080 \u1077  \u1090 \u1074 \u1080 \u1089 \u1090 \u1072 ",\
    "\uc0\u1057 \u1072 \u1084 \u1099 \u1081  \u1079 \u1088 \u1077 \u1083 \u1080 \u1097 \u1085 \u1099 \u1081  \u1084 \u1086 \u1085 \u1090 \u1072 \u1078 ",\
    "\uc0\u1053 \u1086 \u1084 \u1080 \u1085 \u1072 \u1094 \u1080 \u1103  \u1079 \u1072  \u1079 \u1088 \u1080 \u1090 \u1077 \u1083 \u1100 \u1089 \u1082 \u1091 \u1102  \u1089 \u1080 \u1084 \u1087 \u1072 \u1090 \u1080 \u1102 "\
]\
\
soundtracks = [\
    "https://www.youtube.com/watch?v=rdB13lFexNk",\
    "https://www.youtube.com/watch?v=gZXKl36YS9k",\
    "https://www.youtube.com/watch?v=J9EZGHcu3E8",\
    "https://www.youtube.com/watch?v=HhHwnrlZRus",\
    "https://www.youtube.com/watch?v=e8TZbze72Bc",\
    "https://www.youtube.com/watch?v=xmU1upyu_J8",\
    "https://www.youtube.com/watch?v=Oban0vQYy7o",\
    "https://www.youtube.com/watch?v=ZwAERaRUsp0",\
    "https://www.youtube.com/watch?v=ntXJJwEk1NA"\
]\
\
cards = [\
    \{"title": "\uc0\u1053 \u1077 \u1081 \u1088 \u1086 \u1089 \u1077 \u1090 \u1100  \u1089  \u1082 \u1086 \u1084 \u1087 \u1083 \u1077 \u1082 \u1089 \u1072 \u1084 \u1080 ", "description": "\u1054 \u1090 \u1099 \u1075 \u1088 \u1072 \u1081  \u1072 \u1082 \u1090 \u1105 \u1088 \u1089 \u1082 \u1080 \u1081  \u1084 \u1086 \u1085 \u1086 \u1083 \u1086 \u1075  \u1101 \u1090 \u1086 \u1081  \u1085 \u1077 \u1081 \u1088 \u1086 \u1089 \u1077 \u1090 \u1080 . \u1055 \u1086 \u1089 \u1083 \u1077  \'97 \u1075 \u1086 \u1083 \u1086 \u1089 \u1086 \u1074 \u1072 \u1085 \u1080 \u1077 . \u1055 \u1088 \u1080  \u1091 \u1089 \u1087 \u1077 \u1093 \u1077  \'97 \u1087 \u1086 \u1083 \u1091 \u1095 \u1072 \u1077 \u1096 \u1100  \u1054 \u1089 \u1082 \u1072 \u1088 ."\},\
    \{"title": "\uc0\u1060 \u1072 \u1085 \u1072 \u1090 \u1089 \u1082 \u1072 \u1103  \u1090 \u1077 \u1086 \u1088 \u1080 \u1103 ", "description": "\u1058 \u1074 \u1086 \u1103  \u1080 \u1089 \u1090 \u1086 \u1088 \u1080 \u1103  \'97 \u1074 \u1089 \u1077 \u1075 \u1086  \u1083 \u1080 \u1096 \u1100  \u1090 \u1077 \u1086 \u1088 \u1080 \u1103  \u1092 \u1072 \u1085 \u1072 \u1090 \u1072 . \u1055 \u1088 \u1080 \u1090 \u1103 \u1085 \u1080  \u1079 \u1072  \u1091 \u1096 \u1080  \u1072 \u1083 \u1100 \u1090 \u1077 \u1088 \u1085 \u1072 \u1090 \u1080 \u1074 \u1085 \u1086 \u1077  \u1086 \u1073 \u1098 \u1103 \u1089 \u1085 \u1077 \u1085 \u1080 \u1077  \u1089 \u1086 \u1073 \u1099 \u1090 \u1080 \u1081 ."\},\
    \{"title": "\uc0\u1055 \u1077 \u1088 \u1077 \u1087 \u1091 \u1090 \u1072 \u1085 \u1085 \u1099 \u1081  \u1084 \u1086 \u1085 \u1090 \u1072 \u1078 ", "description": "\u1055 \u1086 \u1084 \u1077 \u1085 \u1103 \u1081  \u1084 \u1077 \u1089 \u1090 \u1072 \u1084 \u1080  2 \u1089 \u1094 \u1077 \u1085 \u1099  \u1080  \u1086 \u1073 \u1098 \u1103 \u1089 \u1085 \u1080 , \u1087 \u1086 \u1095 \u1077 \u1084 \u1091  \u1090 \u1072 \u1082  \u1087 \u1086 \u1083 \u1091 \u1095 \u1080 \u1083 \u1086 \u1089 \u1100 ."\},\
    \{"title": "\uc0\u1057 \u1094 \u1077 \u1085 \u1072  \u1087 \u1086 \u1089 \u1083 \u1077  \u1090 \u1080 \u1090 \u1088 \u1086 \u1074 ", "description": "\u1044 \u1086 \u1073 \u1072 \u1074 \u1100  \u1101 \u1087 \u1080 \u1083 \u1086 \u1075  \u1082  \u1089 \u1074 \u1086 \u1077 \u1084 \u1091  \u1092 \u1080 \u1083 \u1100 \u1084 \u1091  \'97 \u1089 \u1094 \u1077 \u1085 \u1091  \u1087 \u1086 \u1089 \u1083 \u1077  \u1090 \u1080 \u1090 \u1088 \u1086 \u1074 , \u1082 \u1086 \u1090 \u1086 \u1088 \u1072 \u1103  \u1074 \u1089 \u1105  \u1084 \u1077 \u1085 \u1103 \u1077 \u1090 ."\},\
    \{"title": "\uc0\u1052 \u1077 \u1090 \u1072 \u1082 \u1086 \u1084 \u1084 \u1077 \u1085 \u1090 \u1072 \u1088 \u1080 \u1081 ", "description": "\u1042 \u1086  \u1074 \u1088 \u1077 \u1084 \u1103  \u1088 \u1072 \u1089 \u1089 \u1082 \u1072 \u1079 \u1072  \'97 \u1082 \u1086 \u1084 \u1084 \u1077 \u1085 \u1090 \u1080 \u1088 \u1091 \u1081  \u1089 \u1072 \u1084 \u1086 \u1075 \u1086  \u1089 \u1077 \u1073 \u1103  \u1086 \u1090  \u1083 \u1080 \u1094 \u1072  \u1088 \u1077 \u1078 \u1080 \u1089 \u1089 \u1105 \u1088 \u1072  \u1080 \u1083 \u1080  \u1082 \u1088 \u1080 \u1090 \u1080 \u1082 \u1072 ."\}\
]\
\
# \uc0\u1050 \u1086 \u1084 \u1072 \u1085 \u1076 \u1099 \
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    keyboard = [["
\f1 \uc0\u55356 \u57260 
\f0  \uc0\u1053 \u1086 \u1084 \u1080 \u1085 \u1072 \u1094 \u1080 \u1103 ", "
\f1 \uc0\u55356 \u57269 
\f0  \uc0\u1057 \u1072 \u1091 \u1085 \u1076 \u1090 \u1088 \u1077 \u1082 "], ["
\f1 \uc0\u55356 \u57268 
\f0  \uc0\u1050 \u1072 \u1088 \u1090 \u1072  \u1076 \u1085 \u1103 "]]\
    await update.message.reply_text(\
        "\uc0\u1055 \u1088 \u1080 \u1074 \u1077 \u1090 ! \u1071  \u1073 \u1086 \u1090 -\u1082 \u1086 \u1084 \u1087 \u1072 \u1085 \u1100 \u1086 \u1085  \'ab\u1048 \u1084 \u1087 \u1088 \u1086 \u1074 \u1080 \u1079 \u1072 \u1074 \u1088 \u1086 \u1074 \'bb. \u1042 \u1099 \u1073 \u1077 \u1088 \u1080  \u1076 \u1077 \u1081 \u1089 \u1090 \u1074 \u1080 \u1077 :",\
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)\
    )\
\
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    msg = update.message.text\
    if "\uc0\u1053 \u1086 \u1084 \u1080 \u1085 \u1072 \u1094 \u1080 \u1103 " in msg:\
        await update.message.reply_text(random.choice(nominations))\
    elif "\uc0\u1057 \u1072 \u1091 \u1085 \u1076 \u1090 \u1088 \u1077 \u1082 " in msg:\
        await update.message.reply_text(random.choice(soundtracks))\
    elif "\uc0\u1050 \u1072 \u1088 \u1090 \u1072  \u1076 \u1085 \u1103 " in msg:\
        card = random.choice(cards)\
        await update.message.reply_text(f"
\f1 \uc0\u55356 \u57268 
\f0  \uc0\u1050 \u1072 \u1088 \u1090 \u1072  \u1076 \u1085 \u1103 : \{card['title']\}\\n
\f1 \uc0\u9997 \u65039 
\f0  \{card['description']\}")\
    else:\
        await update.message.reply_text("\uc0\u1042 \u1099 \u1073 \u1077 \u1088 \u1080  \u1082 \u1085 \u1086 \u1087 \u1082 \u1091  \u1074 \u1099 \u1096 \u1077  \u1080 \u1083 \u1080  \u1085 \u1072 \u1087 \u1080 \u1096 \u1080  /start.")\
\
# \uc0\u1047 \u1072 \u1087 \u1091 \u1089 \u1082 \
app = ApplicationBuilder().token(BOT_TOKEN).build()\
app.add_handler(CommandHandler("start", start))\
app.add_handler(MessageHandler(filters.TEXT, handle_message))\
app.run_polling()\
}