# avtomobil={'model':'spark', 'rang':'oq', 'yil':'2010'}
# print(avtomobil['rang'])
#----------------------------------------------------------------
# talaba={'ism':'Salimov Olim', 'yosh':25, 't_yil': '2000'}
# print(f"{talaba['ism'].title()},\
#       {talaba['t_yil']}-yilda tug'ilgan,\
#       {talaba['yosh']} yoshda")
#----------------------------------------------------------------
# talaba={'ism':'Salimov Olim', 'yosh':25, 't_yil': '2000'}
# talaba['kurs']=4
# talaba['fakultet']='Axborot texnologiyalar'
# print(talaba)
#----------------------------------------------------------------
# otam={'otam':'mamatov olim', "tugilgan yili":1965, 'shahri':'surxondaryo'}
# print(f"{otam['otam'].title()},\
#       {otam['tugilgan yili']}-yilda tug'ilgan,\
#        {otam['shahri'].title()} viloyatida yashaydi")
# onam={'onam':'imamova halima', "tugilgan yili":1965, 'shahri':'surxondaryo'}
# print(f"{onam['onam'].title()},\
#       {onam['tugilgan yili']}-yilda tug'ilgan,\
#        {onam['shahri'].title()} viloyatida yashaydi")
#----------------------------------------------------------------
# ism=str(input("Otangizni F.I.Oni kiriting: "))
# ism1=str(input("Onangizni F.I.Oni kiriting: "))
# ism=ism.title()
# ism1=ism1.title()


# print(f"Mening otam {ism}\
# \nMening onam {ism1}")
#----------------------------------------------------------------
# men={'nomi':'manti', 'miqdori':'10 dona', 'turi':'xonim'}
# ukam={'nomi':'osh', 'miqdori':'1 pors', 'turi':'uzbekcha'}
# akam={'nomi':'qovurma', 'miqdori':'1 pors', 'turi':'shurva'}
# print (f"{men['nomi']},\
#        {men['miqdori']}-shunchaga tuyadi,\
#        {men['turi']}-yaxshi ko'radi")
# print (f"{ukam['nomi']},\
#        {ukam['miqdori']}-shunchaga tuyadi,\
#        {ukam['turi']}-yaxshi ko'radi")
# print (f"{akam['nomi']},\
#        {akam['miqdori']}-shunchaga tuyadi,\
#        {akam['turi']}-yaxshi ko'radi")
#----------------------------------------------------------------

# python_lugat={'print':'konsolga chiqaradiga funksiya hisoblanadi', "f-string":"o'zgaruvchilarni birlashtirish uchun ishlatiladi",
# 'upper':"har bir harfni bosh harfa o'zgartiradi", "lower":"har bir harfni kichik harga o'zgartiradi",
# "title": "har bir so'zning birinchi harfini bosh harfga o'tkazadi", "capitalize":"so'zning birinchi harfini katta bilan yozad",
# "lstrip":"matn boshidagi bo'shliqni oladi", "rstrip":"matn oxiridagi bo'shliqni oladi", "strip": "matn boshi va oxiridagi bo'shliqni oladi",
# "input": "kirituvchi funksiya hisoblanadi"}

# soz=input("Lug'aviy so'z kiriting: ").lower()
# print(python_lugat.get(soz,"Bunday soz mavjud emas"))
# soz=input("Lug'aviy so'z kiriting: ").lower()
# tarjima=python_lugat.get(soz)

# if tarjima==None:
#     print("Bunday soz mavjud emas")
# else:
#     print(f"{soz.title()} so'z {tarjima} deb tarjima qilinadi")
#----------------------------------------------------------------
# talaba={
#     'ism':'Olim',
#     'familya':'salimov',
#     'yosh': 22,
#     'fakultet':'Matematika va informatika',
#     'kurs':4
# }
# for kalit, qiymat in talaba.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}")
#----------------------------------------------------------------
# mahsulotlar={
#     'olma': 10000,
#     'anor': 20000,
#     'uzum': 40000,
#     'anjir':25000,
#     'shaftoli':30000
# }
# bozorlik=['anor', 'uzum', 'non', 'baliq']
# for m in mahsulotlar:
#     if m in bozorlik:
#         print(f"{m.title()} {mahsulotlar[m]} so'm")
#----------------------------------------------------------------
# telefonlar={
#     'ali': 'ipone x',
#     'xasan':'samsung 51a',
#     'xusan':'honor x10',
#     'aloviddin':'samsung 10s',
#     'jafar': 'samsung 51a',
#     'madina': 'samsung 10a',
#     'guli': 'homor 7x'
# }
# for tel in set(telefonlar.values()):
#     print(tel.title())
#----------------------------------------------------------------
