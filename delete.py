#how to delete the static variable
#delete the static variable out side a class
#del clssname.variablename
#delete inside a class method
#delete inside a class method
#del cls.variable name
class Test:
    a=20    #static variable
    b=40
    c=40
    d=50
    @classmethod    #class method
    def m1(cls):
        del Test.a   #deleting inside the class method with cls or class name
        del cls.b
    @staticmethod
    def m2():          
        x=35
        y=49
        print(x)
        print(y)
    @staticmethod
    def m3():
        x=56
        print(x)
Test.m2()
Test.m3()
print(Test.__dict__)
del Test.c
# del Test.a         #deleting with help of class name out the class 
Test.m1()           
print(Test.__dict__)

#local or temporary variables:


