import numpy as np
x = input("Enter a number greater than 10 :")
y= int(x)
if y>10:
	random_numbers=np.random(low=0,high=x,size=10)       
    print(random_numbers[random_numbers>5])
else:
    print("Enter valid number")