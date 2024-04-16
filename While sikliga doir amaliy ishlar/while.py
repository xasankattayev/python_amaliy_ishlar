# print("Kiritilgan sonning kvadratini hisoblaydi:")
# savol="Istalgan son kiriting"
# savol+="(To'xtatish uchun 'exit' deb yozing):"
# qiymat=''
# while qiymat !='exit':
#     qiymat =input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
#-----------------------------------------------------------
# son=1
# while son<=5:
#     print (son, end=' ')
#     son=son+1
# print("Dastur tugadi")
#---------------------------------------------------------
# print("Kitoblarning ro'yxatini yozing")
# kitob="Siz yoqtirgan kitoblarni kiriting: "
# kitob1=''
# while kitob1 !='stop':
#     kitob1 =input(kitob)
#     if kitob1 !='stop':
#         print(kitob1.title())
#---------------------------------------------------------
# print("Muzeyga kirish uchun chipta narxlar quyidagicha")
# yosh="Yoshingizni kiriting: "
# yosh1=''
# while yosh1 !='stop':
#     yosh1 =int(input(yosh))
#     if yosh1 !='stop':
#         
#         if yosh1<=7:
#             print("Muzeyga kirish uchun 2 000 so'm")
#         elif 7<yosh1<=18:
#             print("Muzeyga kirish uchun 3 000 so'm")
#         elif 18<yosh1<=65:
#             print("Muzeyga kirish uchun 10 000 so'm")
#         elif yosh1>65:
#             print("Muzeyga kirish bepul")
# print('Yoshingizni qayta kiriting')
#----------------------------------------------------------
# savol="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol+="Musbat son kiriting: "
# savol="(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat =float(input(savol))
#     if qiymat <0:
#         continue
#     elif qiymat =='exit':
#         break
#     else:
#         ildiz=round(float((qiymat)**(0.5)),2)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
#---------------------------------------------------------
# ismlar=[]
# print("Yaqin dos'stlaringiz ro'yxatini tuzamiz")
# n=1
# while True:
#     savol=f"{n}-do'stingiz ismini kiriting: "
#     ism=input(savol)
#     ismlar.append(ism)
#     javob=input("Yana ism qo'shasizmi? (ha/yo'q): ")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Ro'yxat tuzildi")
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
#--------------------------------------------------------
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar={}
# ishora=True
# while ishora:
#     ism=input("Do'stingiz ismini kiriting: ")
#     yosh=input(f"{ism.title()} ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)
#     javob=input("Yana ma'lumot qo'shasizmi (ha/yo'q): ")
#     if javob =="yo'q":
#         ishora=False
#     for ism,yosh in dostlar.items():
#         print(f"{ism.title()} {yosh} yoshda")
#----------------------------------------------------------------
# talabalar=['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba.title()} ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba]=baho
#----------------------------------------------------------------

# buyurtma=[]
# n=1
# while True:
#     buyurtma1=(f"{n}-buyurtma nomini kiriting: ")
#     mahsulot=input(buyurtma1.title())
#     buyurtma.append(mahsulot)
#     text=input(f"Yana buyurtma berasizmi?")
#     if text=="ha":
#         n+=1
#         continue
#     else:
#         break
# for mahsulot in buyurtma:
#     print(mahsulot)
#----------------------------------------------------------------






