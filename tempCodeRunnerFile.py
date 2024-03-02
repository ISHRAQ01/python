class Test:
    x=10
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
print("FOR T1",t1.x,t1.y)
print("for T2",t2.x,t2.y)
t1.x=888
t2.y=999
print("FOR T1",t1.x,t1.y)
Print("FOR T2",t2.x,t2.y)
    