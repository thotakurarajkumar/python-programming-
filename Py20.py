class Rectangle:
    length = 10
    breadth = 5
    height = 2

    def area(self):
        print(self.length * self.breadth)

    def volume(self):
        print(self.length * self.breadth * self.height)


r = Rectangle()
r.area()
r.volume()
