import numpy as np
n=input("Enter Number : ")

array=np.random.randint(0,n,10)
print("Random numbers between 0 and",n)
print(array)
print("Numbers, which is greater than Five are : ", array[array>5])



