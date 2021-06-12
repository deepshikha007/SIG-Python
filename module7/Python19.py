print("Deepshikha 1803010075")
def check_range(a,b,n):
    isRange = range(min(a,b),max(a,b))
    if n in isRange:
        print(n, "is within the range")
    else:
        print(n, "is not within the range")

check_range(4,10,7)