class Computer:
    count = 0

    def __init__(self, ram, hard, cpu):
        Computer.count += 1
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def __del__(self):
        Computer.count -= 1

    def value(self):
        return self.ram + self.hard + self.cpu


class Laptop(Computer):
    def __init__(self, ram, hard, cpu):
        super().__init__(ram, hard, cpu)
        self.size = None

    def value(self):
        return self.ram + self.hard + self.cpu + self.size


pc1 = Computer(8, 2, 4)
print(pc1.value())
del pc1
print(Computer.count)

laptop1 = Laptop(16, 2, 4)
laptop1.size = 13
print(laptop1.value())
