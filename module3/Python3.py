print("Deepshikha 1803010075")
s1 =int(input())
s2 =int(input())
s3 =int(input())
if s1 == s2 == s3:
    print("Equilateral Triangle") 
elif s1 == s2 or s2 == s3 or s3 == s1: 
    print("Isoceles Triangle") 
else:
    print("Scalene Triangle")