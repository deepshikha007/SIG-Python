print("Deepshikha 1803010075")
num1=int(input())
num2=int(input())
if num1>num2: 
    min = num2
else: 
    min=num1 
for i in range(1,min+1): 
    if((num1%i == 0) and (num2%i == 0)): 
        gcd=i
print(gcd)
