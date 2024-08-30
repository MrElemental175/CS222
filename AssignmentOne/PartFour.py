
MarketPrice = int(input("What is the target price?"))
CurrentPrice=int(input("What is the current share price?"))
while CurrentPrice < MarketPrice:
    CurrentPrice = CurrentPrice + 1
    print(CurrentPrice)
    print("You should wait to sell your stocks")

print("Your shares can now be sold")
