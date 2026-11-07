class Father:
    def work(self):
        print("father work in IT")


class Mother:
    def cook(self):
        print("mother cooks")


class Child(Father, Mother):
    def study(self):
        print("child study")


c = Child()
c.work()
c.cook()
