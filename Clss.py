class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.d=40
    def m1(self):
        del self.d
    
t=Test()
print(t.__dict__)
t.m1()
del t.b
t.c=301
print(t.__dict__)

