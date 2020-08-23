import random

def find(arr1,n,m):
    if(n<0):
        return
    else:
        find(arr1,n-1,m)
        if(arr1[n]>m):
             print(arr1[n])
g = int(input("Enter your number : ")) 
arr1=random.sample(range(0,g),10)
print(arr1)
n=len(arr1)
m=5;
	
	
find(arr1,n-1,m)
