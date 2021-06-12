print("Deepshikha  1803010075")

def oldlist(l1,n): 
    for i in range(n): 
        print(l1[i], end = " ")
def newlist(l1, n): 
    for i in range(n): 
        if ((i + 1) % 2 == 0): 
            l1[i] = "#"
    oldlist(l1, n)
l1 = [ 1, 2, 3, 4, 5 ] 
n = len(l1) 
  
newlist(l1, n) 


	