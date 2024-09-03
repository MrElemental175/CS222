import math

PackOfDogs = 10
PackOfBuns = 8

NumOfPeople = float(input("How many people are going to be at the cookout?"))
NumOfDogs = float(input("How many Hotdogs will each person be given?"))

TotalDogs = NumOfDogs * NumOfPeople
print("You need a total of ", TotalDogs, " hotdogs.")

RequiredDogs = TotalDogs / PackOfDogs
RequiredBuns = TotalDogs / PackOfBuns

RemainderDogs = TotalDogs % PackOfDogs
if RemainderDogs != 0:
    RemainderDogs = PackOfDogs - RemainderDogs
RemainderBuns = TotalDogs % PackOfBuns
if RemainderBuns != 0:
    RemainderBuns = PackOfBuns - RemainderBuns

RequiredBuns = math.ceil(RequiredBuns)
RequiredDogs = math.ceil(RequiredDogs)

print("You will need ", RequiredDogs, "packs of hotdogs and ", RequiredBuns, "of hotdog buns.")
print("You will have ", RemainderDogs, "hotdogs left.")
print("You will have ", RemainderBuns, "hotdog buns left.")