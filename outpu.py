# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         del self.a

# t1=Test()
# t2=Test()
# del t1.b
# print(t1.__dict__)
# print(t2.__dict__)

# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20

# t1=Test()
# t2=Test()
# t1.a=888
# t1.b=999
# print(t1.__dict__)
# print(t2.__dict__)

# class Test:
#     def __init__(self):
#         self.a=10
#     def m1(self):
#         self.a=20
#         self.b=30

# t=Test()
# t.m1()
# t.a=40
# t.b=60
# print(t.__dict__)

class Test:
    def __init__(self,a,b):
        print(self.a)
        print(self.b)
    def m1(self):
         print(self.a)
         print(self.b)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        print(Test.a)

t=Test(7,6)
t.m1(5,6)
Test.m2()
Test.m3()
print(Test.a)
print(t.a)