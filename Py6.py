class Student:
    name = "kprit"
    age = 21


class CSEStudent(Student):
    branch = "cse g&f"


fg = CSEStudent()
print(fg.name)
print(fg.age)
print(fg.branch)
