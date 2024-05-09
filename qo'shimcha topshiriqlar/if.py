son = int(input("Son kiriting: "))

if 0<=son<=50:
    print("F")
elif 50<=son<=59:
    print("E")
elif 60<=son<=69:
    print("D")
elif 70<=son<=79:
    print("C")
elif 80<=son<=89:
    print("B")
elif 90<=son<=100:
    print("A")
else:
    print("Boshqa son kiriting")
#----------------------------------------------------------------
son = int(input("Son kiriting: "))
if son%2==0:
    print(f"{son} bu juft son")
else:
    print(f"{son} bu toq son")