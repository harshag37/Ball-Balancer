

#importing numpy
import numpy as np
x=input("enter the number")

random=np.random.randint(0,x,10)
print("random numbers between 0 and",x)
print(random)
#printing elements above 5
print("elements above 5")
#random>5
print(random[random>5])

 
