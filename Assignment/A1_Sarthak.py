import numpy as np
x = int(input())
arr = np.random.randint(low=0, high=x, size=10)
l = []

def findList(lst):
    if(len(lst) != 0):
        if lst[0] > 5: 
            l.append(lst[0])
        return findList(lst[1:])
    else:
        return 0
        
findList(arr)
print(l)