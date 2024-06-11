#Program :-> Calculate the area of circle.
#Input:-> radius
#data type
#input->float
#Output:-> float
#core Logic:-> area = pi*r*r or  pi*r^2
import math
radius = float(input("Enter the radius \n "))
print(math.pi)
area = math.pi*radius*radius
area1 = math.pi*pow(radius,2)
area2 = math.pi*(radius**2)
print(area)
print(area1)
print(area2)

#another method
print(float(input("enter the radius\n"))**2)

#another method

#another method

print(3.14*(float(input("enter the radius\n"))**2))

