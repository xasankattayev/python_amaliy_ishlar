# with open ('pi.txt') as fayl:
#     pi=fayl.read
#     print(pi)
#     fayl.close()
# file=open('pi.txt')
# pi=file.read()
# print(pi)
# file.close()
#-----------------------------------------------------------
# with open('text/matn.txt') as fayl:
#     matn=fayl.read()
#     print(matn)
#     fayl.close()
#-----------------------------------------------------------
# faylname='text/matn.txt'
# with open(faylname) as fayl:
#     nomlar=fayl.readlines()
#     print(nomlar)
#-----------------------------------------------------------
# faylnomi='kolektivlar.txt'
# with open(faylnomi,'w') as fayl:
#     fayl.write("Assalomu alaykum")

# faylnomi='yangi_file.txt'
# ism="Xasan Kattayev"
# tyil=1996
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism+'\n')
#     fayl.write(str(tyil)+'\n')
# #------------------------------------------------------------
# with open(faylnomi,'a') as fayl:
#     fayl.write('Xusan Kattayev'+'\n')
#     fayl.write('1996'+'\n')
#----------------------------------------------------------
# with open('pi.txt') as fayl:
#     pi=fayl.read()
#     print(pi)
#     fayl.close()
#----------------------------------------------------------
# bdate = '31122000'
# pi=3.14151715874622148
# print(bdate in pi)

# pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz

# with open('amaliyot/pi_float.dat','wb') as file:
#     pickle.dump(pi,file)
#----------------------------------------------------------------
# faylnomi='yangi_file.txt'
# ism=input("Ism familyangizni kiriting: ")
# tyil=int(input("Tug'ilgan yilingizni kiriting:"))
# with open(faylnomi, 'a') as fayl:
#     fayl.write(ism+'\n')
#     fayl.write(str(tyil)+'\n')
#----------------------------------------------------------------
# matn1={'ism':'Xasan', 'familiya':'KAttayev', 'tyil':'1996'}


# with open('text1.txt','w') as file:
#     file.write("Assalomu alaykum Admin sahifaga hush kelibsiz"+'\n  ')
#     file.write(str(matn1))
#----------------------------------------------------------------
# while True:
#     matn=input("So'z kiriting: ")
#     if matn =='exit':
#         break
#     with open('text1.txt', 'a') as file:
#         file.write(matn +'\n')
#-----------------------------------------------------------------
# matn1="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789 "
# with open('text2.txt',mode='r', encoding='utf-8') as f:
#     content=f.read()

# for i in matn1:
#     c=0
#     for j in content:
#         if i==j:
#             c+=1
#     print(i,c) 
#------------------------------------------------------------------
# matn1="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789 "
# with open('text2.txt',mode='r', encoding='utf-8') as f:
#     content=f.read()
# with open('text2.txt',mode='w', encoding='utf-8') as f:
#     f.write(' ')

# for i in matn1:
#     c=0
#     for j in content:
#         if i==j:
#             c+=1
#     with open('report.txt',mode='a', encoding='utf-8') as f:
#         f.write(f"{i}={c} \n")
#-----------------------------------------------------------------
# import json
# import googleamps
# from apikey import APIKEY

# gmaps=googlemaps.Client(key=APIKEY)
# geocode_result=gmaps.geocode('Termiz, Surxondaryo, Uzbekistan').


# g=json.dumps(geocode_result[0], indent=4, sort_keys=True)
# print(g)
#----------------------------------------------------------------
# import json
# data1={"MOdel":"Malibu", "Rang": "Qora", "Yil": 2020, "Narx": 40000}

# data1_json=json.dumps(data1, indent=4)
# print(data1_json)
#----------------------------------------------------------------
# import random as r
# sonlar=r.randint(0,10)
# print(sonlar)
# import random
# numb=['997552-03-96','99890225-58-88','99897244-48-04','99895-244-85-85','9987741225']

# sonlar=random.choice(numb)

# print(sonlar)
#--------------------------------------------------------------------
# import random
# numb=[2,3,8,9,7,4,5,22,112,147,15,52]

# sonlar=random.shuffle(numb)

# print(sonlar)
#-----------------------------------------------------------------
import random

def pincode():
    pincode=""
    for _ in range(9):
        pincode+=random.choice('0123456789')
    return pincode

card1=pincode()
print(card1)
                #------------------
# dfs = pd.read_html('https://www.google.com/finance?q=NASDAQ%3AGOOGL&fstype=ii&ei=9YBMWIiaLo29e83Rr9AM', flavor='html5lib')
# xlWriter = pd.ExcelWriter(output.xlsx, engine='xlsxwriter')

# for i, df in enumerate(dfs):
#         df.to_excel(xlWriter, sheet_name='Sheet{}'.format(i))
#     xlWriter.save()
# # Versions of Pandas >= 1.3.0:
# writer = pd.ExcelWriter('output.xlsx',
#                         engine='xlsxwriter',
#                         engine_kwargs={'options': {'strings_to_numbers': True}})

# # Versions of Pandas < 1.3.0:
# writer = pd.ExcelWriter('output.xlsx',
#                         engine='xlsxwriter',
#                         options={'strings_to_numbers': True})import pandas as pd
# import numpy as np

# dfs = pd.read_html('https://www.google.com/finance?q=NASDAQ%3AGOOGL' +
#                    '&fstype=ii&ei=9YBMWIiaLo29e83Rr9AM', flavor='html5lib')
# xlWriter = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter')
# workbook = xlWriter.book

# for i, df in enumerate(dfs):
#     for col in df.columns[1:]:                  # UPDATE ONLY NUMERIC COLS 
#         df.loc[df[col] == '-', col] = np.nan    # REPLACE HYPHEN WITH NaNs
#         df[col] = df[col].astype(float)         # CONVERT TO FLOAT   

#     df.to_excel(xlWriter, sheet_name='Sheet{}'.format(i))

# xlWriter.save()
# #Export the DataFRame (df) to XLS
# xlsFile = "Preco20102019.xls"
# df.to_excel(xlsFile)

# #Export the DataFRame (df) to CSV
# csvFile = "Preco20102019.csv"
# df.to_csv(csvFile)

#------------------------------------------------------------------
# import random

# def pincode():
#     pincode=""
#     for _ in range(7):
#         pincode+=str(random.randint(0,9))
#     return pincode

# card1=pincode()
# print(card1)
#----------------------------------------------------------
# import random

# def generate_password(count):
#     password=""
#     for _ in range(count):
#         password+=random.choice('0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm')
#     return password
# print(generate_password(10))
# print(generate_password(8))
# print(generate_password(7))
# print(generate_password(6))
# print(generate_password(10))
#-----------------------------------------------------
#    Xatolar bilan ishlash
# while True:
#     yosh = input ("Yoshingizni kiriting: ")
#     break

# # yosh = input ("Yoshingizni kiriting: ")

# try:
#     yosh=int(yosh)
# except:
#     print("Iltimos yoshingizni to'g'ri kiriting")
# else:
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz")

# print("Mazkur dastur davom etyapti")
# while True:
#     for i in yosh:
#         i += i
#--------------------------------------------------------
# from tkinter import *
# window=Tk()
# window.title("Mening birinchi grafik oynam")
# label1=Label(window, text="Salom dasturchi", font=("Arial",25))
# label1.grid(column=2, row=0)
# window.mainloop()


    




