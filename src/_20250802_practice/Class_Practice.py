class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def get_name(self):
        print(('Name is %s' % self.name))

    def get_age(self):
        print('Age is %i' % self.age)

    def get_info(self):
        print('Name is %s and age is %i' % (self.name, self.age))

    def birthday(self):
        self.age += 1
        print('Happy birthday %s. You are now %i years old.' % (self.name, self.age))

maisam = Person('Maisam', 40)
amir = Person('Amir',37)
# maisam.get_name()
# maisam.get_age()
maisam.get_info()
maisam.birthday()
amir.get_info()
amir.birthday()
print('There are %i students in class!' % Person.count)
