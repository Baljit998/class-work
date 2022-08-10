from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    def area(self):
        pass
class Rectangle(Polygon):
    def perimeter(self,length,breadth):
        return 2*(length+breadth)

    def area(self,length,breadth):
        return length*breadth

class Square(Polygon):
    def perimeter(self,length,sides):
        return sides*length
    def area(self,length):
        return length*length

class pentagon(Polygon):
    def perimeter(self,length,sides):
        return sides*length
    def area(self,length,sides):
        return 1/2*sides*length*length
length=int(input("Enter length of polygon "))
breadth=int(input("Enter breadth of polygon "))
sidesR=int(input("Enter sides of rectangle "))
sidesS=int(input("Enter sides of square "))
sidesP=int(input("Enter sides of pentagon "))

R=Rectangle()
print("Perimeter and Area of Rectangle are ")
print(R.perimeter(length,breadth))
print(R.area(length,breadth))

S=Square()
print("Perimeter and Area of square are ")
print(S.perimeter(length,sidesS))
print(S.area(length))

P=pentagon()
print("Perimeter and Area of regular pentagon are ")
print(P.perimeter(length,sidesP))
print(P.area(length,sidesP))



