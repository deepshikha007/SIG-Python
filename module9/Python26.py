print("Deepshikha 1803010075")
file = open("file2.txt","r")
Count = 0
  
Content = file.read()
List = Content.split("\n")
  
for i in List:
    if i:
        Count += 1
          
print(Count)
