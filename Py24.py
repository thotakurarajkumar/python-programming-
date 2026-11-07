class Parent:
    def display(self):
        print("Parent")


class Child(Parent):
    def display(self):
        print("Child")


c = Child()
c.display()
