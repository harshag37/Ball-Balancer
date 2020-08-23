import numpy as np
x=input("enter the range")
arr=np.random.randint(0,x,10)
print(arr[arr>5])