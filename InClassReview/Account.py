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
    def show(self):
        print(self.number)
        print(self.balance)
def main():
    alice = Account("0001", 1000.50, "bsu")
    bob = Account("0002", 100, "iu")
    alice.deposit(200, "bsu")
    bob.show()
    alice.show()

main()