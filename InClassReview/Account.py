class Account():
    def __init__(self, number, balance, password):
        self.number = number
        self.balance = balance
        self.password = password
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        if amountToDeposit < 0:
            print("Error - You cannot deposit a negative amount")
        self.balance += amountToDeposit
        return self.balance
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Incorrect Password")
            return None
        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None
        if amountToWithdraw > self.balance:
            print("You canot withdraw more than your balance")
            return None
        self.balance -= amountToWithdraw
        return self.balance
    def show(self):
        print(self.number)
        print(self.balance)
def main():
    alice = Account("0001", 1000.50, "bsu")
    bob = Account("0002", 100, "iu")
    bob.withdraw(150, "iu")
    bob.show()
    alice.show()

main()