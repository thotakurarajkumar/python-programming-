class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def read(self):
        print(self.name)
        print(self.age)


s1 = Student("kprit", 21)
s2 = Student("age", 31)

s1.read()
s2.read()
