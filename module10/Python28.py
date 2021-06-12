print("Deepshikha 1803010075")
class Circle():
    def __init__(self):
        self.radius = int(input("Enter the radius : "))

    def getArea(self):
        return self.radius**2*3.14
    
    def getCircumference(self):
        return 2*self.radius*3.14


obj = Circle()
print(obj.getArea())
print(obj.getCircumference())