#take the 2 int number from the user and ada them
#we need to use input() function

a = input("Enter the first number:")
b = input("Enter the second number:")
result = a + b
print("addition of a & b:",result)

#this program give result as a+b ex 1011 insted of its addition
#so we need to convert the variable into int
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
result = a + b
print("addition of a & b:",result)

#another method
a = input("Enter the first number:")
b = input("Enter the second number:")
result = int(a)+ int(b)
print("addition of a & b:",result)

# if + -> int will do sum operation
# for str it will concanitae strings

#conver int to str = str()
#conver str to int = int()
print(type(int(a)))


