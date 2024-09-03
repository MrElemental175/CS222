
PackOfDogs = 10
PackOfBuns = 8

NumOfPeople = int(input("How many people are going to be at the cookout?"))
NumOfDogs = int(input("How many Hotdogs will each person be given?"))

TotalDogs = NumOfDogs * NumOfPeople

RequiredDogs = TotalDogs / PackOfDogs
RequiredBuns = TotalDogs / PackOfBuns

