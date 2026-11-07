class Demo:
    a = 1
    b = 3

    def abc(self):
        print("abc")


class Sample(Demo):
    c = 3
    d = 4

    def cde(self):
        print("cde")


s = Sample()
print(s.a)
print(s.b)
s.abc()
s.cde()
