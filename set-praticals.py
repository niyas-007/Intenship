"""------------Section 1 – Basic Set Programs-------------"""

"""1. Create a set containing 5 numbers and print the set"""

# Numbers={1,2,3,4,5}
# print(Numbers)


"""2. Create a set with mixed data types and print each element."""

# a={10,"Apple",10.22,True}
# for i in a:
#     print(i)

"""3. Write a program to create a set from a list."""

# Fruits=["Apple","Orange","Banana","Kiwi"]
# new_set=set(Fruits)
# print(new_set)

"""4. Write a program to remove duplicate elements from a list using a set."""

# Fruits=["Apple","Orange","Banana","Kiwi","Apple","Orange"]
# new_set=set(Fruits)
# print(new_set)

"""6. Write a program to check if an element exists in a set"""

# a={10,"Apple",10.22,True}
# check=input("Enter the element to check :")
# print(check in a)


"""7. Create a set and print all elements using a for loop."""

# Fruits={"Apple","Orange","Banana","Kiwi"}
# for i in Fruits:
#     print(i)

"""8. Write a program to find the length of a set without using len()"""

# Fruits={"Apple","Orange","Banana","Kiwi"}
# count=0
# for i in Fruits:
#     count+=1
# print(count)

"""9. Write a program to convert a tuple into a set"""

# Fruits=("Apple","Orange","Banana","Kiwi")
# new_set=set(Fruits)
# print(new_set)

"""10. Write a program to convert a set into a list."""

# Fruits={"Apple","Orange","Banana","Kiwi"}
# new_list=list(Fruits)
# print(new_list)

"""--------------Section 2 – Adding and Removing Elements-------------"""



"""11. Create a set and add a new element using add()."""

# Fruits={"Apple","Orange","Banana","Kiwi"}
# Fruits.add("Mango")
# print(Fruits)


"""12. Write a program to add multiple elements to a set using update()."""

# Fruits={"Apple","Orange","Banana","Kiwi"}
# Fruits.update(["Mango","Watermelon","Grapes"])
# print(Fruits)

"""13. Write a program to remove an element using remove()."""

# Fruits={"Apple","Orange","Banana","Kiwi"}
# Fruits.remove("Kiwi")
# print(Fruits)

"""14. Write a program to remove an element using discard()"""

# Fruits={"Apple","Orange","Banana","Kiwi"}
# Fruits.discard("Kiwi")
# print(Fruits)

"""15. Write a program to remove a random element using pop()"""

# cars={"BMW","Audi","Ferrari","porshe"}
# cars.pop()
# print(cars)

"""16. Write a program to clear all elements from a set."""

# cars={"BMW","Audi","Ferrari","porshe"}
# cars.clear()
# print(cars)

"""17. Write a program to copy a set into another set."""

# cars={"BMW","Audi","Ferrari","porshe"}
# new_cars=cars.copy()
# print(cars)
# print(new_cars)

"""18. Write a program to add elements from a list into a set."""

# cars=["BMW","Audi","Ferrari","porshe"]
# my_set=set()
# for i in cars:
#     my_set.add(i)
# print(my_set)

"""19. Write a program to add elements from a tuple into a set"""

# cars=("BMW","Audi","Ferrari","porshe")
# my_list=list()
# for item in cars:
#     my_list.append(item)
# print(my_list)

"""20. Write a program to update a set with another set."""

# set1={1,2,3}
# set2={10,20,30}
# set1.update(set2)
# print(set1)