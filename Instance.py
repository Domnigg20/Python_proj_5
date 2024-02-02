class computer:
    #arrow specifies return type
    #self is the first parameter of __init__, and it represents the instance of the class being created.
    
    def __init__(self, Cpu, RAM):
        self.Cpu = Cpu
        self.RAM = RAM
    def config(self):
        print("Config is :", self.Cpu, self.RAM)


#instances of class computer
com1 = computer("Intel", "12gb")
com2 = computer("AMD", "8gb")

com1.config()
com2.config()
