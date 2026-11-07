class Animal:
    def eat(self):
        print("animal eat")


class Mammals(Animal):
    def sleep(self):
        print("mammals sleep")


class Dog(Mammals):
    def sound(self):
        print("dog sound")


d = Dog()
d.sound()
d.sleep()
d.eat()
