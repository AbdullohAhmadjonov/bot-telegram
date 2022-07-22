
import sqlite3
import time
import PIL
import cv2
import numpy as np
import telebot
from telebot import types
admin=1796927301
bot=telebot.TeleBot("5081153778:AAFteNY6MRx1qtNEZd6kg3b5Xk9_QtEz3Vw")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Salom siz Bu botdan foydalanib Oddiy Rasmni Multik fotoga aylantrishingiz mumkun!\nBot hichqanday kanalga Azo shartlarsiz ishlaydigan yagona bot')
    try:
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
    except:
        pass

panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
a = types.KeyboardButton("📤  Xabar  yuborish")
b = types.KeyboardButton("📊  Userlar  soni")
c = types.KeyboardButton("📤  Reklama  yuborish")
d = types.KeyboardButton("📂  Malumotlar  bazasi")
e = types.KeyboardButton("👤  Userga  yuborish")
ads=types.KeyboardButton("ADS Chat")
o = types.KeyboardButton("♻️  START")
x = types.KeyboardButton("🆘  HELP")
panel.row(a, c)
panel.row(d, b)
panel.row(e,ads)
panel.row(o, x)
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
def text(message):

    link = message.text
    
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
            bot.send_message(message.chat.id, """Как пользоваться:
  1. Зайдите в одну из социальных сетей.
  2. Выберите интересное для вас видео.
  3. Нажми кнопку «Скопировать».
  4. Отправьте нашему боту и получите ваш файл!

Бот может скачивать с:
   1. TikTok
   2. YouTube""")


    
    elif message.text=="ADS Chat":
        bot.send_message(message.chat.id,"'Text Ads Chat'ni Yuboring 🔼 ")
        bot.register_next_step_handler(message, adse)

    elif message.text == "👤  Userga  yuborish":
        bot.send_message(1796927301, "<b>👤  Userni  🆔-sini  kiriting  :</b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(message, id_ga)

    elif message.text == "📂  Malumotlar  bazasi":
        bot.send_document(message.chat.id, open("baza.db", "rb"))

    elif message.text == "📤  Xabar  yuborish":
        msg = bot.send_message(admin, "<b>Knopkasiz habar yuboring  : </b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(msg, send)

    elif message.text == "📤  Reklama  yuborish":
        msg = bot.send_message(admin, "<b>Knopkali xabar yuboring  : </b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(msg, forwar)

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
                bot.copy_message(i, message.chat.id, message.id)
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
            print(i[0])
        ketti = 0
        ketmadi = 0
        for i in l:
            a = len(l)
        for i in l:
            try:
                bot.forward_message(i, message.chat.id, message.id)
                ketti += 1
            except:
                ketmadi += 1
        oxiri = time.time()
        bot.send_message(admin, f"<b>{a}  :  ta  foydalanuvchidan  👥\n\n{ketti}  :  tasiga  yuborildi  ✅\n\n{ketmadi}  :  tasiga  yuborilmadi  ❌\n\nXabar  {round(boshi-oxiri)} - secundda userlarga yuborildi ✅</b>", parse_mode='html', reply_markup=panel)


def id_ga(message):
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        global id_si
        id_si = message.text
        bot.send_message(1796927301, "<b>Userga  yubormoqchi  bo'lgan  habaringizni  yuboring   :</b>", parse_mode='html')
        bot.register_next_step_handler(message, yub)

def yub(message):
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        try:
            bot.copy_message(id_si, message.chat.id, message.id)
            bot.send_message(admin, "Xabaringiz yuborildi ✅")
        except:
            bot.send_message(admin, "Xabaringiz yuborilmadi ❌")


@bot.message_handler(content_types=['photo'])
def get_docs(message):
    try:
        file_info = bot.get_file(file_id=message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f"{message.chat.id}.png", 'wb') as new_file:
                    new_file.write(downloaded_file)
                    time=bot.reply_to(message, f'⏳')


                    photo=message.chat.id
                    img = cv2.imread(f"{message.chat.id}.png")

                    
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    gray = cv2.medianBlur(gray, 5)
                    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                                            cv2.THRESH_BINARY, 9, 9)

                    
                    color = cv2.bilateralFilter(img, 9, 250, 250)
                    cartoon = cv2.bitwise_and(color, color, mask=edges)


                    cv2.imwrite(f'{photo}.png',cartoon)

                    photo=open(f'{photo}.png','rb')

                
                    img = cv2.imread('foto.png')
                    
                    img_gb = cv2.GaussianBlur(img, (7, 7) ,0)
                    
                    img_mb = cv2.medianBlur(img_gb, 5)
                    
                    img_bf = cv2.bilateralFilter(img_mb, 5, 80, 80)
                    
                    img_lp_im = cv2.Laplacian(img, cv2.CV_8U, ksize=5)
                    img_lp_gb = cv2.Laplacian(img_gb, cv2.CV_8U, ksize=5)
                    img_lp_mb = cv2.Laplacian(img_mb, cv2.CV_8U, ksize=5)
                    img_lp_al = cv2.Laplacian(img_bf, cv2.CV_8U, ksize=5)

                    
                    img_lp_im_grey = cv2.cvtColor(img_lp_im, cv2.COLOR_BGR2GRAY)
                    img_lp_gb_grey = cv2.cvtColor(img_lp_gb, cv2.COLOR_BGR2GRAY)
                    img_lp_mb_grey = cv2.cvtColor(img_lp_mb, cv2.COLOR_BGR2GRAY)
                    img_lp_al_grey = cv2.cvtColor(img_lp_al, cv2.COLOR_BGR2GRAY)
                    _, EdgeImage = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

                    
                    blur_im = cv2.GaussianBlur(img_lp_im_grey, (5, 5), 0)
                    blur_gb = cv2.GaussianBlur(img_lp_gb_grey, (5, 5), 0)
                    blur_mb = cv2.GaussianBlur(img_lp_mb_grey, (5, 5), 0)
                    blur_al = cv2.GaussianBlur(img_lp_al_grey, (5, 5), 0)
                    
                    _, tresh_im = cv2.threshold(blur_im, 245, 255,cv2.THRESH_BINARY +  cv2.THRESH_OTSU)
                    _, tresh_gb = cv2.threshold(blur_gb, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                    _, tresh_mb = cv2.threshold(blur_mb, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                    _, tresh_al = cv2.threshold(blur_al, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

                    
                    inverted_original = cv2.subtract(255, tresh_im)
                    inverted_GaussianBlur = cv2.subtract(255, tresh_gb)
                    inverted_MedianBlur = cv2.subtract(255, tresh_mb)
                    inverted_Bilateral = cv2.subtract(255, tresh_al)

                    
                    img_reshaped = img.reshape((-1,3))
                    
                    img_reshaped = np.float32(img_reshaped)
                    
                    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
                    
                    K = 8
                    
                    _, label, center = cv2.kmeans(img_reshaped, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
                    
                    center = np.uint8(center)
                    res = center[label.flatten()]
                    
                    img_Kmeans = res.reshape((img.shape))

                    
                    div = 64
                    img_bins = img // div * div + div // 2

                    
                    inverted_Bilateral = cv2.cvtColor(inverted_Bilateral, cv2.COLOR_GRAY2RGB)
                    
                    cartoon_Bilateral = cv2.bitwise_and(inverted_Bilateral, img_bins)
                    
                    cv2.imwrite('goto.png', cartoon_Bilateral)

                    
                    image = cv2.imread("rasm.png")
                    
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
                    gray = cv2.medianBlur(gray, 7) 
                    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
                    
                    color = cv2.bilateralFilter(image, 12, 250, 250) 
                    cartoon = cv2.bitwise_and(color, color, mask=edges)
                    
                    
                    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    
                    grayImage = cv2.GaussianBlur(grayImage, (3, 3), 0)
                    
                    edgeImage = cv2.Laplacian(grayImage, -1, ksize=5)
                    edgeImage = 255 - edgeImage
                    
                    ret, edgeImage = cv2.threshold(edgeImage, 150, 255, cv2.THRESH_BINARY)
                    
                    edgePreservingImage = cv2.edgePreservingFilter(image, flags=2, sigma_s=50, sigma_r=0.4)
                    
                    output =np.zeros(grayImage.shape)
                    
                    output = cv2.bitwise_and(edgePreservingImage, edgePreservingImage, mask=edgeImage)
                    


                    cartoon_image = cv2.stylization(image, sigma_s=150, sigma_r=0.25)  
                    cv2.imwrite('cartoon.png', cartoon_image)  
                    bot.delete_message(message.chat.id,time.message_id)
                    bot.send_photo(message.chat.id,open("foto.png",'rb'),caption="@multikRasmimBot")
                    bot.send_photo(message.chat.id,open('goto.png','rb'),caption="@multikRasmimBot")
                    bot.send_photo(message.chat.id,open('cartoon.png','rb'),caption="@multikRasmimBot")
    except Exception as e:
            print(e)

@bot.message_handler(content_types=['video'])
def send_text(message):
                bot.send_message(message.chat.id, 'Bu Funksiya 10.000 ta foydalanuvchidan sang ishga tushadi!\nAyni Vaqtda Foto rejimi ishlamoqda')

bot.polling()
