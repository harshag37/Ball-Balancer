import numpy as np
x=input("enter the range")
arr=np.random.randint(0,x,10)
new_arr=np.array([i for i in arr if i>5])
print(new_arr)