print("Deepshikha 1803010075")
class Student:
    def __init__(self, name,roll_no): 
        self.name=name
        self.roll_no=roll_no
    def display(self): 
        print("Name ",self.name)
        print("Roll No ",self.roll_no)
        print("Age ",self.age)
        print("Marks ",self.marks)
        
    def setAge(self): 
        self.age=int(input("Enter age : "))
    def setMarks(self): 
        self.marks=int(input("Enter marks : "))

obj1=Student("Mani",78) 
obj1.setAge()
obj1.setMarks()
obj1.display()
