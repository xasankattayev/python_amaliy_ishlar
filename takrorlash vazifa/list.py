# ismlar=['Xasan', 'Xusan', 'Otabek', 'Rauf']

# # for i in ismlar:
# print(f"Assalomu alaykum  {ismlar[0]}")
# print(f"Assalomu alaykum  {ismlar[1]}")
# print(f"Assalomu alaykum  {ismlar[2]}")

# sonlar=[-2,3,5,-7,12]
# sonlar.append(114)
# c=sum(sonlar)
# sonlar.insert(1,588)
# print(sonlar)

# ismlar=['Xasan', 'Xusan', 'Otabek', 'Rauf']
# ismlar.sort()
# print(ismlar)

# juft_sonlar=list(range(120,1200,2))
# farqi=max(juft_sonlar)-min(juft_sonlar)
# print("Sonlar farqi: ", farqi)

# juft_sonlar=list(range(120,1200,2))

# soni=len(juft_sonlar)
# print("Sonlar soni: ", soni)

# juft_sonlar=list(range(120,1200,2))

#------------------------------------------------
# ismlar=['Xasan', 'Xusan', 'Otabek','Behruz']

# for i in ismlar:
#     print(f"Assalomu alaykum {i} Xush kelibsiz")

#------------------------------------------------
# ismlar=['Xasan', 'Xusan', 'Otabek','Behruz','Mansur']

# for i in ismlar:
#     print(f"Assalomu alaykum {i} Xush kelibsiz")
# c=len(ismlar)
# print(f"Kod {c} marta takrorlandi")

#------------------------------------------------

# sonlar=list(range(9,100,2))
# for i in sonlar:
#     kub=i**3
#     print(f"Sonlar kubi {kub} ga teng")
#-------------------------------------
# kinolar=[]
# print("---------------5 ta yoqtirgan kino nomini kiriting --------------")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-kino nomini kiriting: "))
#     print(kinolar)

#-------------------------------------------
# ismlar=[]
# print(f"----------Siz bugun kimlar bilan uchrashdingiz-------------")
# for i in range(*args):
#     if i=='q':
#         break
#     ismlar.append(input(f"{i+1}-ismni kiriting: "))
#     print(ismlar)
#----------------------------------------------
# cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# for avto in cars:
#     if avto=='gm':
#         print(avto.upper())
#     else:
#         print(avto.title())
#-------------------------------------------------
# cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# for avto in cars:
#     if avto !='gm':
#         print(avto.title())
#     else:
#         print(avto.uppper())

#-------------------------------------------------

# login=input("Logini kiriting: ")
# if login == "admin":
#     print("Xush kelibsiz, Admin Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}")
     
#------------------------------------------------------
# bir=input("1-sonni kiriting: ")
# ikki=input("2-sonni kiriting: ")
# if bir == ikki:
#     print("Sonlar teng")
# else:
#     print("Sonlar teng emas")

#---------------------------------------------------
# son=int(input("Son kiriting: "))
# if son > 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")

#-----------------------------------------------

# son = int(input("Son kiriting: "))
# if son%2==0:
#     print("Juft son")
# else:
#     print("Toq son")

#---------------------------------------------
# son=int(input("Son kiriting: "))

# if son%2==0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas")
#---------------------------------------------------

# yosh=int(input("Yoshingizni kiriting: "))

# if yosh < 4 or yosh >60:
#     print("Bepul")
# elif yosh <18:
#     print("Chipta narxi 10_000 so'm")
# elif yosh > 18:
#     print("Chipta narxi 20_000 so'm")

#---------------------------------------------------

# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))

# if son1 > son2:
#     print("Birinchi son katta")
# elif son1 < son2:
#     print("Ikkinchi son katta")
# elif son1==son2:
    # print("Sonlar teng")

#-----------------------------------------------------

# mahsulot=['olma', 'nok', 'banana', 'kivi', 'non', 
#           'gilos', 'daftar', 'karam','ruchka']

# savat=[]
# savat = input("Mahsulot kiriting": )

#-----------------------------------------------------

# foydalanuvchi=['admin', 'xasan', 'xusan', 'zafar', 'fara']

# login=input("Hurmatli foydalanuvchi login kiriting: ")

# if login.lower() in foydalanuvchi:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

#--------------------------------------------

# son=int(input("Son kiriting: "))
# son1=[]
# for i in range(2,11):
#     if son%i==0:
#         son1.append(i)
#         print(son1)
#         continue
#     # else:
#     #     print("Bunday sonlar mavjud emas")
#--------------------------------------------------

# oila={"otam":"Ergash", "yosh":59, "yashash_joy":"Termiz", 
#       "onam": "Halima", "yosh":59, "yashash_joy":"Termiz shahar",
#       "akam":"Ma'mur", "yosh": 31, "yashash_joy":"Pyati",
#       "ukam": "Xusan", "yosh":28, "yashash_joy":"Pitr"}

# # print(f"{oila['otam']}{oila['yosh']}{oila['yashash_joy']}")\
# for i in oila:
#     print(f"{i} {oila[i]}")

#-----------------------------------------------------

# # kitob=input("Yoqtirgan kitob nomini kiriting: ")
# while True:
#     kitob=input("Yoqtirgan kitob nomini kiriting: ")
#     if kitob=='stop':
#         break
#     else:
#        print(f"Siz yoqtirgan kitoblar {kitob}")

#-----------------------------------------------------

# while True:
#     yosh=int (input("Yoshingizni kiriting: "))
#     if yosh<7:
#         print("Chipta narxi 2000 so'm")
#     elif 7<=yosh<=18:
#         print("Chipta narxi 3000 so'm")
#     elif 18<yosh<=65:
#         print("Chipta narxi 10 000 so'm")
#     elif yosh>65:
#         print("Bepul")
#     if yosh=='exit' or yosh=='quit':
#         break
#     print("Chiqishingiz mumkin! ")
#-----------------------------------------------------

# ismlar=[]
# print("Yaqin do'stlaringiz ismini kiriting")
# n=1
# while True:
#     ism=input(f"{n}-do'stingizni kiriting: ")
#     ismlar.append(ism)
#     javob=input(("Yana ism qo'shasizmi (ha/yo'q)"))
#     if javob=='ha':
#         n+=1
#         continue
#     if javob=="yo'q":
#         break
# print("Ro'yxat tuzildi")
# for ism in ismlar:
#     print(ism.title())
#-------------------------------------------------------
# nomi=[]

# while True:
#    buyurtma=input("Buyurmani kiriting: ")
#    nomi.append(buyurtma)
#    print(f"Buyurma ro'yxati:  {nomi}")

#-------------------------------------------------------
# bozor=[]
# print("E-bozor mahsulotlar ro'yxatini shakillatirish")

# while True:
#     mahsulot=input("Mahsulot nomini kiriting: ")
#     narx=int(input(f"{mahsulot.title()} - mahsulot narxini kiriting: "))
#     # bozor[mahsulot]=int(narx)
#     for mahsulot, narx in bozor.items():
#         print(f"{mahsulot.title()} {narx} narxda")

#-------------------------------------------
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh=int(yosh)
#     print(f"Siz {2024-yosh}-yilda tug'ilgansiz")

# except:
#     print("Butun son kiritmadingiz")

# print("Dastur tugadi! ")

#----------------------------

# def nomlar(ism,familiya):
#     return (f"Ism:{ism}, Familiya:{familiya}")
# odam=nomlar("Jamol", "Isayev")
# print(odam)
#-------------------------------------
# x=input("Yoshingizni kiriting: ")
# def nomi(ism,yoshi):
#     print(f"Hurmatli {ism}, Siz {2024-yoshi} - yilda tug'ilgansiz")

# x=nomi("Xasan", 28)
# print(x)

#------------------------------------

# x=int(input("Son kiriting: "))

# def son(x):
#     print(f"{x} - ning kvadrati {x**2} ga teng")
#     print(f"{x} ning kubi {x**3} ga teng")

# x=son(3)

# print (x)

# a=4
# b=11
# print(a|b)
# print(a>>2)
          
# pip install rembg pillow

# from rembg import remove
# from PIL import Image

# input_path = "in.jpg"
# output_path = "out.jpg"

# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)
#-------------------

# talaba={
#     'ismi': 'alijon',
#     'familiya': 'isayev',
#     'yosh': 28,
#     'yashash_joy': 'termiz',
#     'tugilgan_yil': 2001,
#     'fakulteti': 'matematika'
# }

# for kalit, qiymat in talaba.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}")
#---------------------------------------------

# def toq_juft(a):
#     # a=int(input("Son kiriting: "))
#     if a%2==0:
#         print("Juft son")
#     else:
#         print("Toq son")
# son=int(input("Son kiriting: "))

# print(toq_juft(son))
# #----------------------------------------------

# def son(a,b):
#     if a > b:
#         print(a)
#     elif a < b:
#         print(b)
#     elif a == b:
#         print("Sonlar teng")

# print(son(3,4))
#--------------------------------------------
# def son(x,n):
#     print(f"{x} ning {n}-darajasi  {x**n} ga teng")
# x=son(3,4)
# print(x) 

#-----------------------------------------






   





