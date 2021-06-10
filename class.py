
class Person:
    __total = 0

    def __init__(self, name, age, address): # this di js
        self.nama = name
        self.umur = age
        self.role = "user"

        # private attribute
        self.__address = address

    def get_address(self):
        return f"address : {self.__address}"

    def set_address(self, new_address):
        self.__address = new_address

    # private method
    def __name(self):
        return self.nama

    def private_method(self):
        return self.__name()

    def greeting(self):
        return f'hello, {self.nama}'

    def private_variable(self):
        return f"total orang : {Person.__total}"

    def __str__(self):
        return f"name: {self.nama}, umur : {self.umur}, role : {self.role}" 


class Student(Person):
    def __init__(self, name,age, address, batch):
        super(Student, self).__init__(name, age, address)
        self.batch = batch

    # def greeting(self):
    #     return f'hello, {self.nama}, dari batch {self.batch}'

    def greeting(self):
        return super(Student, self).greeting()

    def __str__(self):
        return f"name: {self.nama}, umur : {self.umur}, role : {self.role}, batch: {self.batch}"

p1 = Person('pratama', 23, 'malang')
s1 = Student('pratama', 23, 'malang', 'excellent echo')


print(p1)
print(s1)

# print(p1.greeting())
# print(s1.greeting())

# person1 = Person('pratama', 23, "jember")

# print(person1.__address)
# person1.set_address('malang')

# print(person1.get_address())
# print(person1.private_method())

# print(person1.private_variable())


# print(person1.nama)
# print(person1.umur)
# print(person1.greeting())
# print(Person.total)


# encapsulation
# class Car:
#     turbo_speed = 140

#     def __init__ (self,km):
#         self.km = km

#     def count_hour(self):
#         return Car.turbo_speed / self.km


# car1 = Car(100)

# print(car1.count_hour())