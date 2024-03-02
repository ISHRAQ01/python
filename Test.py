class Test:
    x=10
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
print(id(t1))
print(id(t2))
print(id(Test))
print("FOR T1",t1.x,t1.y)
print("for T2",t2.x,t2.y)
t1.x=888
t2.y=999
print(id(t1.x))
print(id(Test.x))
print("FOR T1",t1.x,t1.y)
print("FOR T2",t2.x,t2.y)
print(t1.__dict__)
print(t2.__dict__)
    