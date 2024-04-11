# dostlar=[]
# print("5 ta yaqin do'stingizni kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting:"))
#     print(dostlar)

#----------------------------------------------------------------
# ismlar=["Xasan", "Xusan", "Davlat", "Muros", "Jafar"]
# for n in ismlar:
#     print(n,"," " 20 dekabr kuni to'yga kutib qolaman")
#     print( "Hurmat ila: Ergashovlar oilasi" )
#----------------------------------------------------------------
# ism=["Ali", "Vali", "Hasan", "Husan", "Olim"]
# for n in ism:
#     print("Salom",n)
# print ("Kod:", len(ism), "marta takrorlandi")
#----------------------------------------------------------------
# for n in range(11,100,2):
#     print(n**3)
#----------------------------------------------------------------
# kinolar=[]
# print ("5 ta sevimli kinolar qaysi:")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar)
#----------------------------------------------------------------
# a=int(input("Bugun nechi kishi bilan suxbat qildingiz:"))
# ismlar=[]
# for n in range(a):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi:"))
# print(ismlar)
#----------------------------------------------------------------
# n=int (input("Son kiriting:"))
# k=int (input("Son kiriting 2:"))
# for n in k:
#     print (n)
#----------------------------------------------------------------
# print (" n natural son qiymatini kiriting:")
# n=int (input("n="))
# s=0
# for i in range(1,n+1):
#     s+=i*(i+1)
#     print("Yig'indini qiymati:", s)
#----------------------------------------------------------------
# raqam=[1,2,3,4,8,10,22,28,36,32,34,42,41,43,45,47]
# raqam_juft=[]

# for i in raqam:
#     if i%2==0:
#         raqam_juft.append(i)
# print (raqam_juft)
#----------------------------------------------------------------
# meva=["Olma", "Nok", "Banana", "Uzum", "Anor"]
# meva_1=""
# c=0
# for i in meva:
#     if len(i)>c:
#         meva_1=i
#         c=len(i)

   
# print(meva_1)
#----------------------------------------------------------------
# soz="Men O'zbekistonda yashayman"
# word=""
# c=-1
# for i in soz:
#     word+=soz[c]
#     c-=1
# print(word)
#----------------------------------------------------------------
# a=int (input("Son kiriting:"))
# b=int (input("Son kiriting:"))
# c=int (input("Son kiriting:"))

# if a>0:
#     print("a musbat son",a)
#     if b>0:
#         print("b musbat son")
#         if c>0:
#             print("c musbat son")
#         else:
#             print("musbat son mavjud emas")
#----------------------------------------------------------------
# a=int (input("Son kiriting:"))
# b=int (input("Son kiriting:"))
# c=int (input("Son kiriting:"))
# if a>0:
#     print("musbat son",a)
# if a<0:
#     print("manfiy son",a)
# if b>0:
#     print("musbat son",b)
# if b<0:
#     print("manfiy son",b)
# if c>0:
#     print("musbat son",c)
# if c<0:
#     print("manfiy son",c)
#----------------------------------------------------------------
# a=int (input("Son kiriting:"))
# b=int (input("Son kiriting:"))

# if a>b:
#     print (a)
# if a<b:
#     print (b)
# if a==b:
#     print("Boshqa son kiriting")
#----------------------------------------------------------------
# a=int (input("Son kiriting:"))
# b=int (input("Son kiriting:"))

# if a>b:
#     print (1)
# if b>a:
#     print (2)
# if a==b:
#     print(0)
#----------------------------------------------------------------
# a=int (input("Son kiriting:"))
# b=int (input("Son kiriting:"))
# # a<=b
# for i in range(a,b+1):
#     print (i, end=" ") 
#----------------------------------------------------------------
# a=int (input("Son kiriting:"))
# b=int (input("Son kiriting:"))
# # a<b
# for i in range(a,b):
#     if a<b:
#         print (i, end=" ")
#     if a>b:
#         for k in range(b,a):
#             print (k, end=" ")
#----------------------------------------------------------------
# for i in range(1,10):
#     print(i**2,end=" ")
#----------------------------------------------------------------
# for i in range(1,10):
#     print (i+=1, end=" ")
# import random

# def gacha_yigindisi(sonlar_soni, gacha_soni):
#     yigindi = 0
#     for _ in range(gacha_soni):
#         yigindi += random.randint(1, sonlar_soni)
#     return yigindi

# sonlar_soni = 10
# gacha_soni = 1

# yigindi = gacha_yigindisi(sonlar_soni, gacha_soni)
# print(f"{gacha_soni} ta {sonlar_soni} gacha bo'lgan sonlarni olib yig'indisi: {yigindi}")
#-----------------------------------------------------------------
# word=input("So'z kiriting: ")
# new_word=""
# unli="aeiuoAEIUO "
# for i in word:
#     if i not in unli:
#         continue
#     new_word+=i
#     print(new_word)
#----------------------------------------------------------------
# numb=[
#     [2,3,6,8,12,21,25,87],
#     [5,6,9,8,7,11,12,33],
#     [7,85,88,23,20]
# ]
# c=0
# for i in numb:
#     for j in i:
#         c+=j
# print(c)
#----------------------------------------------------------------
# print ("""Yaxshi otga bir qamchi,\nYomon otga ming qamchi""" )
# print ("Men \"Del\" markali noutbuk oldim")
# matn="Nexia", "Tico", 'Damas'+ " ko'rganlar qilar havas."
# print(matn)
# 5 ning 4-darajasini hisoblash dasturi
# print(5**4)
# print (22%4)
#Kvadratning yuzini hisoblash dasturi
# print(125*125)
# #Kvadratning perimetirini hisoblash dasturi
# print(4*125)
# print (3.14*6**2)
# a=6
# b=7
# print (a**2+b**2)
# matn="Hello world!"
# print(matn)
# xabar="Bugun juda yoqimli kun"
#----------------------------------------------------------------
# ismlar=["Xasan", "Xusan", "Otabek", "Oybek", "Elbek"]
# for ism in ismlar:
#     print(f"Salom o'rtoq {ism}" , "20 aprel kuni")
#     print("Seni to'yda kutaman")
#----------------------------------------------------------------
# ismlar=["Xasan", "Xusan", "Otabek", "Oybek", "Elbek"]
# for ism in ismlar:
#     print(f"Salom o'rtoq {ism}" , "20 aprel kuni")
#     print("Seni to'yda kutaman")
# print("Kod" , (len(ism)), "marta takrorlandi")
#----------------------------------------------------------------
# sonlar=list(range(9,100,2))
# for kub in sonlar:
#     print(f"{kub} sonning kubi {kub**3}", "ga teng")
#----------------------------------------------------------------
# kino=[]
# print("5 ta sevimli kinongizni kiriting")
# for n in range(5):
#     kino.append(input(f"{n+1}-kino nomini kiriting: "))
#     print(kino)
#----------------------------------------------------------------
# n=int(input("Nechta odam bilan suxbatlashdingiz? "))
# suxbat=[]
# for k in range(n):
#     suxbat.append(input(f"{k+1}-suxbatdosh ismini kiriting: "))
#     print(suxbat)
#----------------------------------------------------------------
# sozlar=["gul", "avtomobil", "traktor", "mashina", "kompyuterlar"]
# uzun_soz=max(sozlar)
# print(uzun_soz)
#----------------------------------------------------------------

