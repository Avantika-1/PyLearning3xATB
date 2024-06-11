#devlp a program to take two numbers as input and print which numer is greater

#method1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("The first number is greater")
else:
    print("The second number is greater")

#method2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("num1 is greater" if num1 > num2 else "num2 is greater")