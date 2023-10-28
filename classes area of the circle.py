class Circle:
    def __init__(self,r,pi):
        self.r=r
        self.pi=pi
    def getarea(self):
        area=self.pi*self.r*self.r
        return area
    def getperimeter(self):
        perimeter=self.pi*self.r*2
        return perimeter
circle=Circle(7, 22/7)
print("the area of the circle =",circle.getarea())
print("the perimeter of the circle=",circle.getperimeter())

