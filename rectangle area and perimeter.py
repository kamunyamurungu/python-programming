#area and perimeter of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def rectarea(self):
        area=self.length*self.width
        return area
    def rectperimeter(self):
        perimeter=(self.length+self.width)*2
        return perimeter
rectangle=Rectangle(10,8)
print("the area of the rectangle =",rectangle.rectarea())
print("the perimeter of the rectangle =",rectangle.rectperimeter())
