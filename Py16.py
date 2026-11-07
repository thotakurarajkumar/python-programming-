print("Yo")


class Parent:
    pass


class Child(Parent):
    pass


class Student:
    name = "Kprit"
    age = 20


class CSEStudent(Student):
    branch = "CSE"


fg = CSEStudent()
print(fg.name)
print(fg.age)
