class Person:
    def __init__(self, name, last_name, age):
        self._name = name
        self.last_name = last_name
        self.age = age

    @property
    def name(self):
        print('Calling method get name')
        return self._name

    @name.setter
    def name(self, name):
        print('Calling method set name')
        self._name = name

    def show_details(self):
        print(f'Person: {self._name} {self.last_name} {self.age}')

person1 = Person('Juan', 'Perez', 28)
person1.name = 'Juan Carlos'
print(person1.name)
# person1._name = 'Cambio'
# print(person1._name)