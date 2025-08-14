# Exercise: Zoo Animal Management

# Description:
# Create a Python program that simulates managing animals in a zoo.
# You will practice OOP concepts including classes, constructors, destructors,
# instance and class attributes, inheritance, method overriding, and instance manipulation.

# Tasks:

# 1. Define a base class called Animal with:
#    - Class attribute: total_animals (to count all Animal instances)
#    - Instance attributes: name (string), age (int), species (string)
#    - Constructor (__init__) to initialize the attributes and increment total_animals
#    - Destructor (__del__) that prints a message when an animal instance is deleted
#    - Method get_info(self) that returns a string describing the animal
class Animal:
    total_animals = 0

    def __init__(self, name, age, species):
        Animal.total_animals += 1
        self.name = name
        self.age = age
        self.species = species

    def __del__(self):
        Animal.total_animals -= 1
        print('Animal instance is deleted.')

    def get_info(self):
        return f'Name: {self.name} | Age: {self.age} | Species: {self.species}'


# 2. Create a subclass called Lion that inherits from Animal:
#    - Override get_info(self) to include "I am a Lion" in the description
#    - Add method roar(self) that prints "[name] is roaring!"
class Lion(Animal):
    def get_info(self):
        return super().get_info() + '. I am a Lion.'

    def roar(self):
        print(f'{self.name} is roaring!')


# 3. Create another subclass called Elephant:
#    - Override get_info(self) to include "I am an Elephant" in the description
#    - Add method trumpet(self) that prints "[name] is trumpeting!"
class Elephant(Animal):
    def get_info(self):
        return super().get_info() + '. I am an Elephant.'

    def trumpet(self):
        print(f'{self.name} is trumpeting!')


# 4. In the main block:
#    - Create several instances of Lion and Elephant  <- suggested variable names: simba, nala, dumbo, ellie
#    - Print their information using get_info()
#    - Call their specific methods (roar/trumpet)
#    - Modify some instance attributes (like age or name) and print updated info
#    - Delete at least one instance and observe destructor message
#    - Print the total number of animals using Animal.total_animals

simba = Lion('Simba', 16, 'Panthera leo persica')
nala = Lion('Nala', 8, 'Panthera leo leo')
dumbo = Elephant('Dumbo', 27, 'African bush elephant')
ellie = Elephant('Ellie', 20, 'Asian elephant')

print(f'Total Animals: {Animal.total_animals}')

print(simba.get_info())
print(nala.get_info())
print(dumbo.get_info())
print(ellie.get_info())

simba.roar()
nala.roar()
dumbo.trumpet()
ellie.trumpet()

simba.age = 18
simba.name = 'Simbi'
print(simba.get_info())

del ellie
print(f'Total Animals: {Animal.total_animals}')