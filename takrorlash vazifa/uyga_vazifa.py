print("Hurmatli foydalanuvchi Mexmonxona narxlari bilan tanishing")

qavat=int(input("HUrmatli mijoz qavatni kiriting: "))

if 1 <= qavat <= 4:
    print(f"{qavat} - qavat narxi 300 $")
elif 5 <= qavat <= 8:
    print(f"{qavat} - qavat narxi 600 $")
elif 8 < qavat <= 10:
    print(f"{qavat} - qavat narxi 1000 $")

elif qavat > 10:
    print("Hurmatli mijoz Siz kiritgan qavat mavjud emas")
