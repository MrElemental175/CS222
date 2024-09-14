class Power():
    defaultExponent = 2
    def __init__(self, exponent = defaultExponent):
        self.exponent = exponent
    def of(self, x):
        return x ** self.exponent

def main():
    number0 = Power(3)
    number1 = Power(.5)
    print(number1.of(.25))
    

main()