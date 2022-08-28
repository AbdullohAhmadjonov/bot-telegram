
from ast import parse
from configparser import Error
from youtube_dl import YoutubeDL
from pytube import YouTube
import telebot
import sqlite3  
import time
import os
from telebot import types

from telebot import apihelper




user_dict = {}
user_text= {}
bot = telebot.TeleBot("5693903999:AAFFMb7sbQGh7AojenjDd_ra9mzIGVT6tX0") 
admin = 449215179

def tchannel(message):
	channel = "uz_mahsulot_com"
	result = bot.get_chat_member(f"@{channel}", message.chat.id).status
	if not(result=="creator" or result=="administrator" or result=="member"):
     
		ibuttons = types.InlineKeyboardMarkup()
		yes = types.InlineKeyboardButton(text="Obuna Bo'ldim ✅", callback_data='yes')
  
		kanal = types.InlineKeyboardButton(text="Obuna Bo'lish", url=f't.me/{channel}')
		ibuttons.add(kanal)
		ibuttons.add(yes)
  
		imsg = bot.send_message(message.chat.id, f"""Assalomu Alaykum Hurmatli Foydalanuvchi	
🤖Botimizdan foydalishdan oldin Kanalimizga a'zo bo'lishingiz kerak!	
Siz Hali Botimizga Obuna Bolmagansiz ❌

Kanalimiz:
@{channel}

        """, reply_markup=ibuttons)
  
  
  
		return False
    

    



def create(id,nick_name,first_name,vaqt):
    con=sqlite3.connect('baza.db')
    cur=con.cursor()
    cur.execute("""create table if not exists users(id number,
                                                    nick_name text,
                                                    first_name text,
                                                    vaqt text)""")
    cur.execute("select id from users")
    a=cur.fetchall()
    if (id,) not in a:
        k = 0
    else:
        k = 1
    if k == 0:
        cur.execute("""insert into users values({},"{}","{}","{}")""".format(id,nick_name,first_name,vaqt))
        con.commit()
        con.close()
@bot.message_handler(commands=['start'])
def start(message):

    con=sqlite3.connect('baza.db')
    cur=con.cursor()
    cur.execute("create table if not exists users(id integer,name text,time text)")
    cur.execute("select id from users")
    user=cur.fetchall()
    l=[]
    for i in user:
        l.append(i[0])
    if message.chat.id not in l:
      cur.execute(f"""insert into users values({message.chat.id},
                                                '{message.from_user.first_name}',
                                                '{time.localtime()[:5]}')""")
    con.commit()
    con.close()

    if tchannel(message) == False:
        return
    user_dict[message.chat.id] = 0

    bot.send_message(message.chat.id, """😊 Menga yuklab olmoqchi bo'lgan video yoki rasmingizni  silkasini yuboring ✅""", parse_mode='html')
panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
a = types.KeyboardButton("📤  Xabar  yuborish")
b = types.KeyboardButton("📊  Userlar  soni")
c = types.KeyboardButton("📤  Reklama  yuborish")
d = types.KeyboardButton("📂  Malumotlar  bazasi")
e = types.KeyboardButton("👤  Userga  yuborish")
ads=types.KeyboardButton("ADS Chat")
akt=types.KeyboardButton("Aktivlar Soni")
o = types.KeyboardButton("♻️  START")
x = types.KeyboardButton("🆘  HELP")
panel.row(a, c)
panel.row(d, b)
panel.row(e,ads)
panel.row(o, x)
panel.row(akt)

cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
l = types.KeyboardButton("❌  BEKOR  QILISH  ❌")
cancel.row(l)

def reklama(message):
    con=sqlite3.connect('baza.db')
    cur=con.cursor()

    cur.execute("SELECT rek FROM adse")
    starts=cur.fetchall()
    con.commit()
    con.close()
    bot.send_message(message.chat.id, starts[-1])


@bot.message_handler(content_types=['text'])
def admin_panel(message):

    con=sqlite3.connect('baza.db')
    cur=con.cursor()
    cur.execute("create table if not exists users(id integer,name text,time text)")
    cur.execute("select id from users")
    user=cur.fetchall()
    l=[]
    for i in user:
        l.append(i[0])
    if message.chat.id not in l:
      cur.execute(f"""insert into users values({message.chat.id},
                                                '{message.from_user.first_name}',
                                                '{time.localtime()[:5]}')""")
    con.commit()
    con.close()
    if tchannel(message) == False:
        return
    user_dict[message.chat.id] = 0
    global link
    link = message.text
    ## -- ##  commands  ## -- ##
    if message.text == '/panel':
       bot.send_message(admin, "<b>Admin panelga hush kelipsiz !</b>", parse_mode='html', reply_markup=panel)

    elif message.text == '♻️  START':
        bot.send_message(message.chat.id, "/start - commandasini malumotlarini o'zgartirish\n\nmalumot kiriting  :", reply_markup=cancel)
        bot.register_next_step_handler(message, starts)

    elif message.text == '🆘  HELP':
        bot.send_message(message.chat.id, "/help - commandasini malumotlarini o'zgartirish\n\nmalumot kiriting  :", reply_markup=cancel)
        bot.register_next_step_handler(message, helps)

    elif message.text == '/help':
        try:
            bot.send_message(message.chat.id, helper)
        except:
            bot.send_message(message.chat.id, """Qanday ishlatish:
   1. Ijtimoiy tarmoqlardan biriga o'ting.
   2. Sizni qiziqtirgan videoni tanlang.
   3. "Nusxa olish" tugmasini bosing.
   4. Bizning botimizga yuboring va faylingizni oling!

Botni quyidagi manzildan yuklab olish mumkin:
    1. TikTok
    2. YouTube
    3.Pinterest
    4. Instagram
    5. Like""")


    ## -- ##  button  ## -- ##
    elif message.text=="ADS Chat":
        bot.send_message(message.chat.id,"'Text Ads Chat'ni Yuboring 🔼 ")
        bot.register_next_step_handler(message, adse)

    elif message.text == "👤  Userga  yuborish":
        bot.send_message(admin, "<b>👤  Userni  🆔-sini  kiriting  :</b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(message, id_ga)

    elif message.text == "📂  Malumotlar  bazasi":
        bot.send_document(message.chat.id, open("baza.db", "rb"))

    elif message.text == "📤  Xabar  yuborish":
        msg = bot.send_message(admin, "<b>Knopkasiz habar yuboring  : </b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(msg, send)

    elif message.text == "📤  Reklama  yuborish":
        msg = bot.send_message(admin, "<b>Knopkali xabar yuboring  : </b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(msg, forwar)
    elif message.text == 'Aktivlar Soni':
        aktive(message)
    elif message.text == "📊  Userlar  soni":
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
        for i in l:
            a=len(l)
        try:
            bot.send_message(admin, f"<b>👥 Umumiy foydalanuvchilar soni : {a} ta\n\n✅ Aktivlar soni : {ketti} ta\n\n❌ Spam berganlar soni {ketmadi} ta</b>", parse_mode='html')
        except:
            bot.send_message(admin, f"<b>👥 Umumiy foydalanuvchilar soni : {a} ta</b>", parse_mode='html')

    elif message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin, "<b>Bekor  qilindi  ❗</b>", parse_mode='html', reply_markup=panel)


    else:
        mainn(message)
#Hamma userlarga habar yuborish
def aktive(message):
    
        boshi = time.time()
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
        ketti = 0
        ketmadi = 0
        for i in l:
            a = len(l)
        for i in l:
            try:
                bot.send_chat_action(i, action='typing')    
                ketti += 1
            except:
                ketmadi += 1
        oxiri = time.time()
        bot.send_message(admin, f"<b>{a}  :  ta  USER  👥\n\n{ketti}  :  tasi Aktiv  ✅\n\n{ketmadi}  :  tasi  Aktiv Emas  ❌\n\nHisoblash Vaqti  {round(boshi-oxiri)} - secundda ⏳</b>", parse_mode='html', reply_markup=panel)

    
    
    
    
def starts(message):
    global starter
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin, "<b>Bekor  qilindi  ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        starter = message.text
        bot.send_message(message.chat.id, "/start - commadndasi muvafaqiyatli o'zgartirildi ✅", reply_markup=panel)

def helps(message):
    global helper
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin, "<b>Bekor  qilindi  ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        helper = message.text
        bot.send_message(message.chat.id, "/help - comandasi muvafaqiyatli o'zgartirildi ✅", reply_markup=panel)
#Hamma userlarga habar yuborish
def adse(message):
    con=sqlite3.connect('baza.db')
    cur=con.cursor()
    cur.execute("create table if not exists ads(reklama text)")
    cur.execute("select  reklama from ads")
    user=cur.fetchall()
    l=[]
    for i in user:
        l.append(i[0])
    if message.chat.id not in l:
      cur.execute(f"""insert into ads values('{message.text}')""")
    con.commit()
    con.close()
def send(message):
    global ketti
    global ketmadi
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        boshi = time.time()
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
        ketti = 0
        ketmadi = 0
        for i in l:
            a = len(l)
        for i in l:
            try:
                bot.copy_message(i, message.chat.id, message.id,disable_notification=True)
                ketti += 1
            except:
                ketmadi += 1
        oxiri = time.time()
        bot.send_message(admin, f"<b>{a}  :  ta  foydalanuvchidan  👥\n\n{ketti}  :  tasiga  yuborildi  ✅\n\n{ketmadi}  :  tasiga  yuborilmadi  ❌\n\nXabar  {round(boshi-oxiri)} - secundda userlarga yuborildi ✅</b>", parse_mode='html', reply_markup=panel)

def forwar(message):
    global ketti
    global ketmadi
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        boshi = time.time()
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
        ketti = 0
        ketmadi = 0
        for i in l:
            a = len(l)
        for i in l:
            try:
                bot.forward_message(i, message.chat.id, message.id,disable_notification=True)
                ketti += 1
            except:
                ketmadi += 1
        oxiri = time.time()
        bot.send_message(admin, f"<b>{a}  :  ta  foydalanuvchidan  👥\n\n{ketti}  :  tasiga  yuborildi  ✅\n\n{ketmadi}  :  tasiga  yuborilmadi  ❌\n\nXabar  {round(boshi-oxiri)} - secundda userlarga yuborildi ✅</b>", parse_mode='html', reply_markup=panel)

#User id-siga habar yuborish
def id_ga(message):
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        global id_si
        id_si = message.text
        bot.send_message(admin, "<b>Userga  yubormoqchi  bo'lgan  habaringizni  yuboring   :</b>", parse_mode='html')
        bot.register_next_step_handler(message, yub)

def yub(message):
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        try:
            bot.copy_message(id_si, message.chat.id, message.id,disable_notification=True)
            bot.send_message(admin, "Xabaringiz yuborildi ✅")
        except:
            bot.send_message(admin, "Xabaringiz yuborilmadi ❌")
def resend(message):
    pass
        # con=sqlite3.connect('baza.db')
        # cur=con.cursor()

        # cur.execute("SELECT reklama FROM ads")
        # starts=cur.fetchall()
        # con.commit()
        # con.close()
        # qwer = types.InlineKeyboardMarkup(row_width=True)
        # na = types.InlineKeyboardButton("Kanaliga o'tish ⤵️",url="https://t.me/Java_Music_Java_muzika")
        # qwer.row(na)
        
        # bot.send_message(message.chat.id, "<b>Sizga Javaning qo'shiqlari🎵 kerakmi? \nUnda javaning kanaliga o'tib eshitingiz iz mumkin!</b>",parse_mode='html',reply_markup=qwer)

def youtubee(message):
    
        from pytube import YouTube
        yt = YouTube(link)


        p1080 = types.InlineKeyboardButton('📹 1080p', callback_data='1080')
        p720 = types.InlineKeyboardButton('📹 720p', callback_data='720')
        p480 = types.InlineKeyboardButton('📹 480p', callback_data='480')
        p320 = types.InlineKeyboardButton('📹 360p', callback_data='360')
        p240 = types.InlineKeyboardButton('📹 240p', callback_data='240')
        p144 = types.InlineKeyboardButton('📹 144p', callback_data='144')
        
        mp3 = types.InlineKeyboardButton('🔊 mp3', callback_data='mp3')
        th = types.InlineKeyboardButton('🖼', callback_data='th')
        
        

        youtube = types.InlineKeyboardMarkup()
        youtube.add(p1080,p720)
        youtube.add(p480,p320)
        youtube.add(p240,p144)
        youtube.add(mp3,th)
        bot.send_message(message.chat.id,f'<b>Title🖇:{yt.title}\n\nDescription📜: {yt.description}\n\n\nAuthor: </b>'+f"<a href='{yt.channel_url}'"+">"+f"{yt.author}</a>\n\nVIEWS👁: {yt.views} \n\nSeconds⏲: {yt.length}",parse_mode='html', reply_markup=youtube)
        
        
    
    
    

        # from pytube import YouTube
        # yt = YouTube(message.text)
        
        # BASE_URL = f"https://vidiget.com/youtube-downloader/{yt.video_id}"
        # s = requests.Session()

        # r = s.post(f'{BASE_URL}')
        # soup = BeautifulSoup(r.text, 'html.parser')
        # urls_v=[]
        # urls_a=[]
        # for linka in soup.findAll('a', {'class': 'btn btn-outline-primary btn-sm btn-dl'}):
        #     try:
        #         bot.send_audio(message.chat.id,linka['href'])
        #     except:
        #         urls_a.append(linka['href'])
            
        # for link in soup.findAll('a', {'class': 'btn btn-sm btn-outline-success btn-dl'}):
        #     try:
        #         bot.send_video(message.chat.id,link['href'])
        #     except:
        #         urls_v.append(link['href'])
        # mydivs = soup.findAll('img',{'class': 'img-thumbnail rounded'}) 
        # for div in mydivs: 
        #     pass
        # urlsa = types.InlineKeyboardMarkup(row_width=True)
        # a = types.InlineKeyboardButton("Video📹 Yuklash 720p ⬇️",url=urls_v[0])
        # c = types.InlineKeyboardButton("Video📹 Yuklash 480p⬇️",url=urls_v[1])
        # g = types.InlineKeyboardButton("Audio🔊 Ochish m4a 📂",url=urls_a[0])
        # b = types.InlineKeyboardButton("Audio🔊 Ochish webm 📂",url=urls_a[1])
        # rasm = types.InlineKeyboardButton("Rasm 🖼 720p",url=div['src'])
        
        
        # urlsa.row(a)
        # urlsa.row(c)
        # urlsa.row(b)
        # urlsa.row(g)
        # urlsa.row(rasm)
        
        # mydivs = soup.findAll('img',{'class': 'img-thumbnail rounded'})

        # bot.send_message(message.chat.id,f"Title:<b>{div['title']}</b>\n\nPastagi Tugmadan birini Tanlang ⤵️",parse_mode='html',reply_markup=urlsa)   
        

        resend(message)
from urllib import request

# Function to get download url
def get_download_url(link,message):
    import requests
    from pyquery import PyQuery as pq

    # Make request to website 
    post_request = requests.post('https://www.expertsphp.com/download.php', data={'url': link})

    # Get content from post request
    request_content = post_request.content
    str_request_content = str(request_content, 'utf-8')
    download_url = pq(str_request_content)('table.table-condensed')('tbody')('td')('a').attr('href')
    bot.send_video(message.chat.id,download_url,caption=f'{message.text}\n\nʏᴜᴋʟᴀʙ ʙᴇʀᴜᴠᴄʜɪ: @fast_saverbot')
    bot.send_photo(message.chat.id,download_url,caption=f'{message.text}\n\nʏᴜᴋʟᴀʙ ʙᴇʀᴜᴠᴄʜɪ: @fast_saverbot')
    resend(message)




def pinterest(message):

    b=(message.text.replace('Взгляните на это… 👀', ''))        
    BASE_URL = "https://pinterestvideodownloader.com/"
    URL = b
    s = requests.Session()

    data = {"url":URL }
    r = s.post(f'{BASE_URL}', data=data)

    soup = BeautifulSoup(r.text, 'html.parser')
    urls=[]
    try:
        video = soup.find("video").get("src")
        bot.send_video(message.chat.id,video,caption='🎥 Bu video @fast_saverbot orqali yuklab olindi 📥')
        resend(message)
        
    except:
        photo = soup.find("img").get("src")
        bot.send_photo(message.chat.id,photo,caption=f'{message.text}\n\nʏᴜᴋʟᴀʙ ʙᴇʀᴜᴠᴄʜɪ: @fast_saverbot')
        resend(message)

        
        
        
def likee(message):
    import requests
    from pyquery import PyQuery as pq

    # Make request to website 
    post_request = requests.post('https://www.expertsphp.com/download.php', data={'url': link})

    # Get content from post request
    request_content = post_request.content
    str_request_content = str(request_content, 'utf-8')
    download_url = pq(str_request_content)('table.table-condensed')('tbody')('td')('a').attr('href')

    a=(download_url.replace('\/\/', '/'))

    b=(a.replace('\/', '/'))
    d=b[-4:]
    i=(b.replace(d, ''))
    deonloads_url=(i.replace('https:/', 'https://'))

    bot.send_video(message.chat.id,deonloads_url,caption=f"{message.text}\nVideo With WaterMark\n\nʏᴜᴋʟᴀʙ ʙᴇʀᴜᴠᴄʜɪ: @fast_saverbot")
    bot.send_message(message.chat.id,deonloads_url.replace('_4', '')+"  Mana Shu Url Orqali Ornatsihingiz mumkun")
    bot.send_video(message.chat.id,deonloads_url.replace('_4', ''),caption=f"{message.text}\nVideo Without WaterMark ®\n\nʏᴜᴋʟᴀʙ ʙᴇʀᴜᴠᴄʜɪ: @fast_saverbot"  )

    resend(message)
import requests
from bs4 import BeautifulSoup
def insta(message):
    BASE_URL = "https://instasave.website/#downloadhere/"
    URL = message.text
    s = requests.Session()

    data = {"link":URL }
    r = s.post(f'{BASE_URL}', data=data)

    soup = BeautifulSoup(r.text, 'html.parser')
    urls=[]
    for a in soup.find_all('a', href=True):
        try: 
            if a['href']=="https://pro.instasave.website/":
                pass
            elif a['href'] == 'https://instasave.website':
                pass            
            elif a['href'] == 'https://server.instasave.website/':
                pass            
            elif a['href'] == 'https://en.wikipedia.org/wiki/Instagram':
                pass
            else:
                bot.send_document(message.chat.id,a['href'])
                # bot.send_video(message.chat.id,a['href'])
                
               
        except Exception as e:
            print(e)
            

    resend(message)
        

def tiktok(message):
    pass
def vimeo(message):
    URL = message.text
    BASE_URL = 'https://vidiget.com/vimeo_downloader'
    s = requests.Session()
    data = {"vimeo_video_page":URL}
    r = s.post(f'{BASE_URL}', data=data)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.findAll('a',{'class':'btn btn-sm btn-outline-success btn-dl'}):
        print(link['href'])
    try:
        bot.send_video(message.chat.id,link['href'])
    except:
        bot.send_message(message.chat.id,link['href'])

def mainn(message):

    if message.text.startswith('https://you') or message.text.startswith('http://you') or message.text.startswith('https://www.you') or message.text.startswith('http://www.you'):   
        
        print("YouTube",message.chat.id)
        youtubee(message)
    if message.text.startswith('https://insta') or message.text.startswith('http://insta') or message.text.startswith('http://www.insta') or message.text.startswith('https://www.insta'):    
        print("instagram",message.chat.id)
        insta(message)
        
        
    if message.text.startswith('httpss'): 
        print("TikTok",message.chat.id)
           
        tiktok(message)
        
    if message.text.startswith('https://likee') or message.text.startswith('http://likee') or message.text.startswith('https://www.like') or message.text.startswith('http://www.like'):      
        likee(message)
    if message.text.startswith('https://pin') or message.text.startswith('http://pin') or message.text.startswith('https://www.pin') or message.text.startswith('http://www.pin'):    
        pinterest(message)
        print("Pinterest",message.chat.id)
        
    if message.text.startswith('https://vimeo') or message.text.startswith('http://vimeo') or message.text.startswith('https://www.vimeo') or message.text.startswith('http://www.vimeo'):    
        vimeo(message)
        print("vimeo",message.chat.id)  
        

@bot.callback_query_handler(func=lambda call: True )
def callback_inline(call):  
    try:
        if call.message:
            if call.data =='1080':
                    youtube = YouTube(link)
                    video = youtube.streams.filter(res="1080p").first().download()
                    os.rename(video,"video1080.mp4")
                    
                    
                    bot.send_video(call.message.chat.id,open('video1080.mp4','rb'),parse_mode='html') 
                    os.remove('video1080.mp4')
                
            if call.data =='720':
                    youtube = YouTube(link)
                    video = youtube.streams.filter(res="720p").first().download()
                    os.rename(video,"video720.mp4")
                    
                    
                    bot.send_video(call.message.chat.id,open('video720.mp4','rb'),parse_mode='html') 
                    os.remove('video720.mp4')
                              
            if call.data =='480':
                    youtube = YouTube(link)
                    video = youtube.streams.filter(res="480p").first().download()
                    os.rename(video,"video480.mp4")
                    
                    
                    bot.send_video(call.message.chat.id,open('video480.mp4','rb'),parse_mode='html')
                    os.remove('video480.mp4')
                    
            if call.data =='360':
                    youtube = YouTube(link)
                    video = youtube.streams.filter(res="360p").first().download()
                    os.rename(video,"video360.mp4")
                    
                    bot.send_video(call.message.chat.id,open('video360.mp4','rb'),parse_mode='html')
                    os.remove('video360.mp4')
                    
            if call.data =='240':
                    youtube = YouTube(link)
                    video = youtube.streams.filter(res="240p").first().download()
                    os.rename(video,"video240.mp4")
                    
                    
                    bot.send_video(call.message.chat.id,open('video240.mp4','rb'),parse_mode='html')
                    os.remove('video240.mp4')
                    
            if call.data =='144':
                    youtube = YouTube(link)
                    video = youtube.streams.filter(res="144p").first().download()
                    os.rename(video,"video.mp4")
                    
                    
                    bot.send_video(call.message.chat.id,open('video.mp4','rb'),parse_mode='html')
                    os.remove('video.mp4')
                    
            if call.data =='mp3':
                    youtube = YouTube(link)
                    video = youtube.streams.filter(res="144p").first().download()
                    os.rename(video,"audio.mp3")
                    iop = YouTube(link)
                    
                    bot.send_audio(call.message.chat.id,open('audio.mp3','rb'),parse_mode='html')
                    os.remove('audio.mp3')
                    
            if call.data =='th':
                    yt = YouTube(link)
                    try:
                        bot.send_photo(call.message.chat.id,yt.thumbnail_url,caption=f'<b>Title:{yt.title}\n\nDescription📜: {yt.description}\n\n\nAuthor: </b>'+f"<a href='{yt.channel_url}'"+">"+f"{yt.author}</a>\n\nVIEWS👁: {yt.views} \n\nSeconds⏲: {yt.length}",parse_mode='html')
                    except:
                        bot.send_photo(call.message.chat.id,yt.thumbnail_url,caption=f'<b>Title:{yt.title}</b>',parse_mode='html')
                        
                    
#################
#################
#################
#################
#################
            if call.data == 'yes':
                if tchannel(call.message) == False:
                    gg = bot.send_message(call.message.chat.id, 'Siz Hali Obuna Bolmaganisiz! ❌')
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, gg.message_id)
                    
                    
                    

                    
                else:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    
                    gg = bot.send_message(call.message.chat.id, 'Obuna Boldingiz endi Botdan Foydalanishingiz Mumkun✅')
                    
                user_dict[call.message.chat.id] = 0
                
            else:
                bot.delete_message(call.message.chat.id, call.message.message_id)
                
    except Exception as e:
        print(e)





if __name__ == '__main__':
    apihelper.API_URL="http://localhost:8081/bot{0}/{1}"
    apihelper.FILE_URL="http://localhost:8081"
    bot.infinity_polling()
# bot.infinity_polling()




#version 1
