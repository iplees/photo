"""
Developer :- @DF_GD_D 
Channel :- @T62RS 
In :- 2024/1/25
Remember Source 
"""
import telebot, requests, random, sys 
from uuid import uuid4 as uid
from bs4 import BeautifulSoup
import re
import json
from telebot import types 
from time import sleep 
Logo = ('''\033[2;33m
___
_   \   \_  _/_ |  / /    |  /  __/
  /_/ /_  /_/ /  /  | / /  /| |_  /    /
_  /_  _, _// /   |/ / _  _ |  /   _  /_
/_/     /_/ |_| /_/  _/  /_/  |_/_/    /___/

---------------------------------  
''')
def id_file1(id):
 all = False
 file = open("users.txt","r")
 for line in file:
  if line.strip() ==id:
   all = True
 file.close()
 return all 
ti=0
users = []
print(Logo)
Private = types.InlineKeyboardMarkup(row_width=2)
Ch = types.InlineKeyboardButton(text ="𝖣𝖤𝖵𝖤𝖫𝖮𝖯𝖤𝖱" , url = "t.me/DF_GD_D")
Private.add(Ch)
requests.urllib3.disable_warnings() 
token = "Token"#توكنك
sudo = 1651132769 #ايدي
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start(message):
   id = message.from_user.id
   with open("users.txt","a") as f3:
    f3.write(f"{id}\n")
    a = message.from_user.first_name
    b = message.from_user.username
    if message.chat.type == "private":
      if not id in users:
        users.append(id)
        stats = len(users)
        bot.send_message(sudo,"""
↯︙ 🎭 عزيزي الادمن قام شخص جديد بالدخول الى البوت ✅
↯︙ الاسم :- {}  🔎
↯︙ اسم المستخدم :- @{}  ✨
↯︙ الايدي :- {}  📅
↯︙ عدد مستخدمين البوت الكلي :-  {}  ✅
""".format(a,b,id,stats),disable_web_page_preview=True)
    bot.send_photo(message.chat.id,"https://t.me/ifuwufuj/23",caption="""
↯︙ 👋 مرحباً بك عزيزي في بوت الصور ارسل امر /photo لإظهار صورة عشوائية بابعاد 640×480 🤓
---------------------------------  
↯︙ 👋 Welcome dear to the photo bot send the /photo command to show random image with dimensions 640×480 🤓  
""",parse_mode = "markdown" , reply_markup = Private)
@bot.message_handler(commands = ["photo"])
def photo(message):
    url = "https://bing.now.sh/api?rand=true&size=640x480"
    response = requests.get(url)
    if response.status_code == 200:
        bot.send_photo(message.chat.id, response.content)
    else:
        bot.reply_to(message,f""" 
↯︙ ❌ عذراً عزيزي حدث خطأ اثناء الإرسال حاول لاحقاً
---------------------------------  
↯︙ ❌ Sorry, dear, an error occurred while sending, try later 
""",parse_mode = "markdown" , reply_markup = Private)

        bot.send_message(sudo,f""" 
↯︙ 👋 عزيزي الادمن لقد حدث خطأ اثناء الارسال في احد المشتركين يرجى التأكد من واجهة البرمجيات واعادة بناء البوت لاحقا 🤔
↯︙✅ المطور :- @Y_V_O 🔥
""",parse_mode = "markdown" , reply_markup = Private)
@bot.message_handler(commands = ["ueser"])
def num_users(message):
 if message.from_user.id == sudo:
  file = open("users.txt","r")
  Namme = len(file.readlines())
  bot.send_message(message.chat.id,text="عدد المستخدمين :- {}".format(Namme))
 else:
  bot.send_message(message.chat.id,text="انت لست المطور!!!! ")
@bot.message_handler(commands = ["radio"])
def radio(message):
 try:
  if message.from_user.id == sudo:
   idu = message.from_user.id
   t = message.text.replace("/radio" ,"")
   f = open("users.txt","r")
   for idu in f:
    bot.send_message(idu , text="{}".format(t))
  else:
   bot.send_message(message.chat.id, text= " انت لست المطور دوختني (: ")
 except:
  bot.send_message(message.chat.id,text="خطأ اثناء الاذاعة")  
run_msg = "\033[2;35m Running...."
for char in run_msg:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()    
bot.polling(none_stop=True)
"""
Developer :- @Y_V_O 
Channel :- @EJ_J0 
In :- 2024/1/25
Remember Source 
"""