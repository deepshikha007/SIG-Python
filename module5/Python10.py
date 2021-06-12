print("Deepshikha  1803010075")

def longest(a): 
    max1 = len(a[0]) 
    temp = a[0] 
  
    for i in a: 
        if(len(i) > max1): 
  
            max1 = len(i) 
            temp = i 
  
    print(temp)
         
   
a = ["Delhi", "Mumbai", "Jaipur", "Mizoram"] 
longest(a) 