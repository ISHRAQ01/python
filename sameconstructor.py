class Dog:
    def __init__(self,breed,color,weight):
        print("FIRST CONSTRUCTOR WORKING")
        self.breed=breed
        self.color=color
        self.weight=weight
        print("FIRST CONSTRUCTOR WORKING")
    def __init__(self,breed,color,weight):
        print("SECOND CONSTRUCTOR WORKING")
        self.breed=breed
        self.color=color
        self.weight=weight
    def s(self):
        print("ALL DOGS BARK")

d=Dog('labra','white',54)
print("CONSTRUCTOR PRINTING:",d.breed,d.color,d.weight)


