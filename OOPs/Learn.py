class Computer:

    type = 'PC'

    def __init__(self, p, r, s):
        self.processor = p
        self.ram = r
        self.storage = s

    def printconfig(self):
        print("Processor = " + self.processor)
        print("Ram = " + self.ram)
        print("Storage = " + self.storage)


com1 = Computer('i5', '8GB', '1TB')
com1.printconfig()
print(com1.type)

com2 = Computer('i7', '4GB', '500GB')
Computer.type = 'laptop'
print(com1.type)
print(com2.type)