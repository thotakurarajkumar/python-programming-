class Demo:
    a = 1
    b = 2

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
print(s.c)
print(s.d)
s.abc()
s.cde()
