class Animal:
    def eat(self):
        print("Animal eats")

    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


d = Dog()
d.eat()
d.speak()
d.sound()
