class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


d1 = Demo("Yadar", 18)
d1.show()

d2 = Demo("Dhruva", 19)
d2.show()
