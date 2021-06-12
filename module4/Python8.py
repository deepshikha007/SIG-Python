print("Deepshikha 1803010075")
num1=int(input())
num2=int(input())
num3=int(input())
if(num2>num1 and num1>num3 or num3>num1 and num1>num2):
    print("Median = ", num1)
elif(num1>num2 and num2>num3 or num3>num2 and num2>num1):
    print("Median = ",num2)
else:
    print("Median = ",num3)
