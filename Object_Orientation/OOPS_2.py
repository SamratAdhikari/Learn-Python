
# __init__ method

class Computer:
    def __init__(self, cpu, ram, memory):
        self.cpu = cpu
        self.ram = ram
        self.memory = memory

    def config(self):
        print("Config is", self.cpu, self.ram, self.memory)

com1 = Computer("i5", "16gb", "1tb")
com2 = Computer("nvidia", "4gb", "1tb")

com1.config()
com2.config()
