#                     # 1-masala
# a=int (input("0-100 gacha son kiriting:"))
# if 90<=a<=100:
#     print ("A")
# elif 80<=a<=89:
#     print ("B")
# elif 70<=a<=79:
#     print ("C")
# elif 60<=a<=69:
#     print ("D")
# elif 50<=a<=59:
#     print ("E")
# elif 0<=a<=50:
#     print ("F")


                    # 2-masala
# num=int(input("Son:"))

# if num%2==0:
#     print ("Juft son")
# else:
#     print ("Toq son")

                    # 1-masala
# n=int (input("Natural son kiririting:"))
# if n%2==0 and n%4==0:
#     print ("Bu juft son, 4 ga karrali son")
# else:
#     print ("Boshqa son kiriting")
    #----------------------------------------------------------------
# n=int (input("Natural son kiririting:"))
# if n%2==1 and n%5==0:
#     print ("Bu toq son, 5 ga karrali son")
# else:
#     print ("Boshqa son kiriting")
#-----------------------------------------------------------------------
# n=int (input("Natural son kiririting:"))
# if n%2==1 and n%7==0:
#     print ("Bu toq son, 7 ga karrali son")
# else:
#     print ("Boshqa son kiriting")
#---------------------------------------------------------------------

# m=float(input("Eshik enini kiriting: "))
# n=float(input("Eshik bo'yini kiriting: "))

# eshik_olchami=m*n
# a=float(input("Quti eni: "))
# b=float (input ("Quti bo'yi: "))
# c=float (input("Quti balandligi: "))
# quti_olchami=a*b*c

# if eshik_olchami > quti_olchami:
#     print ("Quti eshikdan o'tadi")
# else:
#     print ("Quti eshikdan o'tmaydi")

#---------------------------------------------------------------------
# raqam=float(input("Raqam kiriting: "))
# if raqam>0:
#     print ("Musbat son")
# elif raqam<0:
#     print ("Manfiy son")
# elif raqam==0:
#     print ("Nolga teng")

#----------------------------------------------------------------

# D=float(input("G'ola diametrini kiriting: "))
# A=float(input("Kvadrat brusni enini kiriting: "))

# if D>A:
#     print ("Kesib bo'ladi")
# else:
#     print ("Boshqa brus toping, kesib bo'lmaydi")
#----------------------------------------------------------------
# p=float(input("Pul miqdorini kiriting: "))



#---------------------------------------------------------------
# x=int (input("Son kiriting: "))
# y=int (input("Son kiriting: "))
# z=int (input("Son kiriting: "))

# if x**2==y**2+z**2:
#     print ("To'g'ri burchakli uchburchak")
# elif y**2==x**2+z**2:
#     print ("To'g'ri burchakli uchburchak")
# elif z**2==x**2+y**2:
#     print ("To'g'ri burchakli uchburchak")
# else:
#     print ("To'g'ri burchakili uchburchak bo'lmaydi")

#---------------------------------------------------------------
# avtolar=["audi", "bmw", "volvo", "kia", "hyundai"]
# for avto in avtolar:
#     if avto=="bmw":
#         print(avto.upper())
#     else:
#         print(avto.title())
#---------------------------------------------------------------
# javob =float(input("12x6 nechiga teng: "))
# if javob ==72:
#     print("Javob to'g'ri")
# else:
#     print("Javob xato!")
#------------------------------------------------
# cars=["toyota", "mazda", "hyundai", "gm", "kia"]
# mashina=[]
# for mashina in cars:
#     if mashina=="gm":
#         print (mashina.upper())
#     else:
#         print(mashina.title())
#---------------------------------------------------------------
# cars=["toyota", "mazda", "hyundai", "gm","kia"]
# mashina=[]
# for mashina in cars:
#     if mashina!='gm':
#         print (mashina.upper())
#---------------------------------------------------------------
# login =str (input("Logini kiriting: "))
# # user=[]
# # for user in login:
# if login == "admin":
#     print("Xush kelibsiz, Admin. Foydalanuvchi ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}!")
#---------------------------------------------------------------
# son1=int (input("1-sonni kiriting: "))
# son2=int (input("2-sonni kiriting: "))

# if son1==son2:
#     print("Sonlar teng")
# else:
#     print("Sonlar teng emas")
#---------------------------------------------------------------
# son=float(input("Istalgan son kiriting: "))

# if son>=0:
#     print("Musbat son")
# else: 
#     print("Manfiy son")
#-------------------------------------------------------------
# son = float(input("Son kiriting: "))

# if son > 0:
#     print(son**(0.5))
# else:
#     print("Musbat son kiriting")
#-------------------------------------------------------------
# son=int (input("Son kiriting: "))

# if son%2==0:
#     print("Juft son")
# else:
#     print("Toq son")
#------------------------------------------------------------
# menyu=["osh", "qozonkabob", "shashlik", "norin", "somsa"]
# buyurtma=["osh", "somsa", "manti", "shashlik"]

# for taom in buyurtma:
#     if taom in menyu:
#         print(f"Menyuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menyuda {taom} yo'q")
#------------------------------------------------
# son=int (input("Son kiriting: "))

# if son%2==0:
#     print("Rahmat!")
# else:
#     print("Bu son juft son emas!")
#------------------------------------------------------------
# yosh=int (input("Yoshingizni kiriting: "))
# if yosh<4 or yosh>60:
#     print("Siz uchun bepul")
# elif yosh < 18:
#     print("Muzeyga kirish uchun chipta narxi 10 000 so'm")
# elif yosh > 18:
#     print("Muzeyga kirish uchun chipta narxi 20 000 so'm")
#----------------------------------------------------------------
# son1=float (input("Birinchi sonni kiriting: "))
# son2=float(input("Ikkinchi sonni kiriting: "))
# if son1>son2:
#     print("Birinchi son katta")
# elif son2>son1:
#     print("Ikkinchi son katta")
# elif son1==son2:
#     print("Sonlar teng")
#----------------------------------------------------------------
# mahsulotlar=["sabzi", "karam", "piyoz", "kartoshka", "uzum", 
#             "guruch", "lavlagi", "tuxum","mosh", "olma", "anor"]
# savat=[]
# print("5 ta mahsulot kiriting")    
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
#--------------------------------------------------------------
# mahsulotlar=["sabzi", "karam", "piyoz", "kartoshka", "uzum", 
#             "guruch", "lavlagi", "tuxum","mosh", "olma", "anor"]
# savat=[]
# print("5 ta mahsulot kiriting")    
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# bor_mahsulot=[]
# mavjud_emas=[]

# for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             bor_mahsulot.append(mahsulot)
            
#         else:
#             mavjud_emas.append(mahsulot)
# if mavjud_emas:
#             print (f"Do'konimizda quyidagi mahsulotlar mavjud emas")
# for mahsulot in mavjud_emas:
#             print(mahsulot)
# else:
#             print("Qolgan siz so'ragan barcha mahsulotlar mavjud")
#----------------------------------------------------------------
# foydalanuvchilar=["xasan", "admin", "xusan", "odil", "otash"]
# login=input("Login kiriting: ")
# if login:
#     if login in foydalanuvchilar:
#         print("Login band boshqa login kiriting")
#     else:
#         print(f"Xush kelibsiz, {login.title()}! ")
# else:
#     print("Login kiritilmadi")
#----------------------------------------------------------------
# son=int(input("Son kiriting: "))
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
#----------------------------------------------------------------
soz=int(input("So'z kiriting: "))

for n in soz:
    if n=="aeiuo" or "AEIUO":
        print(n)
        continue
print("Finish")
        


     


        






