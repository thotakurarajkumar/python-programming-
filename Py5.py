class Animal:
    def eat(self):
        print("animal eat")

    def speak(self):
        print("animal speaks")


class Dog(Animal):
    def sound(self):
        print("dog bark")


d = Dog()
d.eat()
d.speak()
d.sound()
