# ranglar={'oq', 'qora', 'qizil'}
# ranglar.add('kul rang')
# ranglar.update(['sariq', 'malla', 'yashil'])
# print (ranglar)
#----------------------------------------------------------------
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# set3=set1-set2
# print(set3)
#----------------------------------------------------------------
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# set3=set1^set2

# print(set3)
#----------------------------------------------------------------
# bozorlik={'choy', 'non', 'kartoshka', 'tuxum', 'sut'}
# mahsulotlar={'non', 'sut', 'tuxum', 'olma', 'un', 'tuz'}
# list=bozorlik&mahsulotlar
# print(list)
#----------------------------------------------------------------
# bozorlik={'choy', 'non', 'kartoshka', 'tuxum', 'sut'}
# mahsulotlar={'non', 'sut', 'tuxum', 'olma', 'un', 'tuz'}
# print("Do'konda mavjud bo'lmagan mahsulotlar ro'yxati")

# list = bozorlik - mahsulotlar
# print(list)
#----------------------------------------------------------------
# bozorlik={'choy', 'non', 'kartoshka', 'tuxum', 'sut'}
# mahsulotlar={'non', 'sut', 'tuxum', 'olma', 'un', 'tuz'}


# mahsulotlar.update(['choy', 'kartoshka'])
# print(mahsulotlar)
#----------------------------------------------------------------
# car0={
#     'model':'lacetti', 'rang':'oq',
#     'yil':2018, 'narx':13000,
#     'km':50000, 'karobka':'avtomat'
# }
# car1={
#     'model':'nexia 3', 'rang':'qora',
#     'yil':2015, 'narx':9000,
#     'km':89000, 'karobka':'mexanika'
# }

# car2={
#     'model':'gentra', 'rang':'qizil',
#     'yil':2019, 'narx':15000,
#     'km':20000, 'karobka':'mexanika'
# }
# cars=[car0, car1, car2]
# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")
#----------------------------------------------------------------
# malibus=[]
# for n in range(10):
#     new_car={
#         'model':'malibus',
#         'rang':None,
#         'yil':2020,
#         'narx':None,
#         'km':0,
#         'karobka':'avto'
#     }
#     malibus.append(new_car)
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
# print(malibus)
#----------------------------------------------------------------
# adabiyot1={
#     'nomi': 'Alisher Navoiy',
#     'tugilgan_joyi': 'Hirot',
#     'yil': 1441,
# }
# adabiyot2={
#     'nomi': 'Bobur',
#     'tugilgan_joyi': 'Andijon',
#     'yil': 1378,
# }
# adabiyot3={
#     'nomi': 'Temur',
#     'tugilgan_joyi': 'samarqand',
#     'yil': 1336,
# }

# fan=[adabiyot1, adabiyot2, adabiyot3]
# for fan1 in fan:
#     print(f"{fan1['nomi'].title()}, "
#         f"{fan1['tugilgan_joyi']} joyda tavvalud topgan, "
#         f"{fan1['yil']}-yilda tug'ilgan.")
#----------------------------------------------------------------
# adabiyot1={
#     'nomi': 'Alisher Navoiy',
#     'tugilgan_joyi': 'Hirot',
#     'yil': 1441,
#     'asar nomi': 'Xamza'
# }
# adabiyot2={
#     'nomi': 'Bobur',
#     'tugilgan_joyi': 'Andijon',
#     'yil': 1378,
#     'asar nomi': 'Boburnoma'
# }
# adabiyot3={
#     'nomi': 'Temur',
#     'tugilgan_joyi': 'samarqand',
#     'yil': 1336,
#     'asar nomi': 'Temur tuzuklari'
# }

# fan=[adabiyot1, adabiyot2, adabiyot3]
# for fan1 in fan:
#     print(f"{fan1['nomi'].title()}, "
#         f"{fan1['asar nomi']} asarlari mavjud.")
#----------------------------------------------------------------

