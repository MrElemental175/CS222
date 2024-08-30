NumOne= int(input("Give me a number"))
NumTwo = int(input("Give me a number larger than the first"))
Sum = 0
for Num in range(NumOne, NumTwo + 1):
    if Num %2 !=0:
        Sum = Sum + Num
        print(Num)

print(Sum)
