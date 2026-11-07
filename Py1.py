class Rectangle:
    def area(self, l, b):
        print(l * b)

    def volume(self, l, b, h):
        print(l * b * h)


r1 = Rectangle()
l = int(input("Enter l = "))
b = int(input("Enter b = "))
h = int(input("Enter h = "))

r1.area(l, b)
r1.volume(l, b, h)
