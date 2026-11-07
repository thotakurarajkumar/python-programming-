class Student:
    name = "KPRIT"
    age = 20


class CSEStudent(Student):
    branch = "CSE"


s = CSEStudent()
print(s.name)
print(s.age)
print(s.branch)
