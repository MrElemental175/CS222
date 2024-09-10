class LightSwitch():
    def __init__(self):
        self.switchIsOn = False
    def turnOn(self):
        self.switchIsOn = True
    def turnOff(self):
        self.switchIsOn = False

def main():
    l0 = LightSwitch()
    l1 = LightSwitch()
    #l1.switchIsOn = True
    l1.turnOn
    print(l0.switchIsOn)
    print(l1.switchIsOn)
main()