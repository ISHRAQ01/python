class Test:
    @classmethod
    def m1(cls):
        print(id(cls))
    @classmethod
    def m2(cls):
        print(id(cls))
    @staticmethod
    def get_average(a,b,c):
        return(a+b+c)/3

average=Test.get_average(4,6,10)
print(id(Test))
Test.m1()
Test.m2()
print("the average is=",average)
