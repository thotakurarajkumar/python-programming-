class Dog:
    def sound(self):
        print("dog bark")


class Cat(Dog):
    def sound(self):
        print("cat mewwow")


c = Cat()
c.sound()
