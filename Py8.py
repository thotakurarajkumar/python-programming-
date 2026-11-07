class Dog:
    def sound(self):
        print("dog sound")

    def eat(self):
        print("dog eat")


class Cat(Dog):
    def sound(self):
        print("cat sound")


c = Cat()
c.sound()

d = Dog()
d.sound()
