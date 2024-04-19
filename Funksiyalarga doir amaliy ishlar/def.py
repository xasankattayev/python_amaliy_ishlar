# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")
# salom_ber()
#--------------------------------------------------------
# def salom_ber(ism):
#     """Foydalanuvchiga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum hurmatli!, {ism.title()}")
# salom_ber('hasan')
#--------------------------------------------------------
# def toliq_salom(ism,familiya):
#     """Foydalanuvchining ism va familiyasiga orqali salom beruvchi funksiya"""
#     print(f"Foydalanuvchi ismi:  {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_salom('olim', 'hakimov')
# def tugilgan_yil(ism,yosh, joriy_yil=2024):
#     """Foydalanuvch ismi va yoshini so'rab, 
#     uning tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f"Siz {joriy_yil-yosh}-yilda tug'ilgansiz")
    
# tugilgan_yil('xasan',32)
#--------------------------------------------------------
# def son_funk(son):
#     """Sonlarning kvadrati va kubini hisoblaydigan funksiya"""
#     print(f"Sonning kvadrati: {son**2}\n"
#           f"Sonning kubi: {son**3}")
# son_funk(10)
#--------------------------------------------------------
# def son_turi(son):
#     """Soning juft yoki toqligini tekshiruvchi funksiya"""
#     if son%2==0:
#         print("Juft son")
#     elif son%2==1:
#         print("Toq son")
    
# son_turi(11)
#--------------------------------------------------------
# def son_turi(son1, son2):
#     """Soning juft yoki toqligini tekshiruvchi funksiya"""
#     if son1>son2:
#         print (son1)
#     elif son2>son1:
#         print(son2)
#     else:
#         print("Sonlar teng")
      
      
# son_turi(3,12)
#---------------------------------------------------------
# def son_turi(x,n):
#     """x ning n-darajasini konsolga chiqaruvchi funksiya"""
#     print(f" {x} ning {n}-darajasi {x**n} ga teng")
# son_turi(5,3)
#--------------------------------------------------------
# def son_qabul(son1):
#     """ Sonning 2 dan 10 gacha bo'lgan sonlarga 
#     qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     for i in range(1,11):
#         if son1%i:
#             print(f"{son1} soni {i} ga qoldiqsiz bo'linadi")
# son_qabul(70)
#---------------------------------------------------------
# print ("Foydalanuvchi haqida to'liq ma'lumot")
# malumot=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni to'ldiring")
#     ism=input('Ismizni kiriting: ')
#     familiya=input("Familya kiriting: ")
#     tugilagan_yil=input("Tug'ilgan yilini kiriting: ")
#     tugilgan_joyi=input("Tug'ilgan joyini kiriting: ")
#     elektron_manzil=input("Elektron manzilini kiriting: ")
#     tel=int(input("Telefon raqamni kiriting: "))
#     yosh=int(input("Yoshingizni kiriting: "))
#     malumot.append(malumot1(ism,familiya,tugilagan_yil,tugilgan_joyi,elektron_manzil,tel,yosh))
#     text=input("Yana ma'lumot kiritasizmi? (yes/no):")
#     if text=="no":
#         break
#-----------------------------------------------------------------
# def katta(*args):
#     c=0
#     for i in args:
#         if i>c:
#             c=i
#     return c
   
# print(katta(3,5,8,7,9,10,17,25,325))
# #----------------------------------------------------------------
# def uzunligi(soz):
#     """Uzunligi sonlarni aniqlovchi funksiya"""
    
#     print ((len(soz)))

# uzunligi([5,8,9,8,9,2,15])
#----------------------------------------------------------------
def avg(*args):
    return sum(args)/len(args)
   
print(avg(3,5,5,2,5,8,5),2)

    


