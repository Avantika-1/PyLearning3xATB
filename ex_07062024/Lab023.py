#List- shopping List
# milk, bread, butter, poha
#Add item
#remove item
#udate item
#remove item
#view item

shopping_list = ["milk", "bread", "butter", "poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("juice") #for add item in the end
print(shopping_list)
shopping_list.insert(1,"paneer") #for add item in the middle
print(shopping_list)
shopping_list.remove("poha") #for remove item
print(shopping_list.pop())
shopping_list.sort()
shopping_list.reverse()
print(shopping_list)
shopping_list[1] = "avantika"
print(shopping_list)

shopping_list.extend(["chips","salt"]) #Add multiple items in the end
print(shopping_list)


my_list = [1,2,3,4, True,3.14, "Avantika"]
print(type(my_list))
