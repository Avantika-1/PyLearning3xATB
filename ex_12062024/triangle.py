#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).

side1= int(input("enter the first side:"))
side2= int(input("enter the second side:"))
side3=int(input("enter the third side:"))

if side1==side2 and side2==side3:
    print("equilateral triangle")
elif side1==side2 or side2 == side3 or side1==side3:
    print("isosceles triangle")
elif side1!=side2 and side2!=side3:
    print("scalene triangle")


