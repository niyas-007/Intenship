# Section 1: Beginner Level


"""1. Create a list of five integers and print all elements using a for loop."""

# a=[10,20,30,40,50]
# for i in a:
#     print(i)

""" 2. Write a program to find the length of a list without using len()."""

# num=[20,40,30,50]
# count =0
# for i in num:
#     count+=1
# print(count)

""" 3. Create a list of numbers and print the maximum and minimum values"""

# num=[44,22,50,20,30]
# print(max(num))
# print(min(num))

"""4. Write a program to append a new element to a list entered by the user."""

# fruits=["Apple","Orange","Banana"]
# print(fruits)
# n=input("Enter a fruit name: ")
# fruits.append(n)
# print(fruits)

"""5. Insert an element at a specific position in a list."""

# cars=["Audi","BMW","Fortuner"]
# cars.insert(2,"Maruthi")
# print(cars)

"""6. Remove an element from a list using remove() and pop()."""

# fruits=["Apple","Orange","Banana"]
# fruits.remove("Apple")
# print(fruits)
# fruits.pop()
# print(fruits)

"""7. Write a program to check whether a given element exists in a list."""

# fruits=["Apple","Orange","Banana"]
# print("Apple" in fruits)

""" 8. Reverse a list without using reverse()."""

# cars=["Audi","BMW","Fortuner"]
# print(cars[::-1])

""" 9. Sort a list of numbers in ascending and descending order."""

# num=[10,100,1000,1,10000]
# """ascending"""
# num.sort()
# print(num)
# """descending"""
# num.sort(reverse=True)
# print(num)

""" 10. Create a list of numbers and print only the even numbers"""

# num=[0,1,2,3,4,5,6,7,8,9]
# num1=[n for n in num if n % 2==0]
# print(num1)

""" 11. Count how many times a specific element appears in a list."""

# num=[20,30,20,40,50,40,30]
# print(num.count(20))

""" 12. Write a program to copy one list into another list."""

# cars=["Audi","BMW","Fortuner"]
# cars1=[cars.copy()]
# print("Copied list=",cars1)

"""13. Concatenate two lists using the + operator."""

# num1=[10,20,30]
# num2=[40,50,60]
# print(num1+num2)

""" 14. Repeat a list three times using the * operator"""

# cars=["Audi","BMW","Fortuner"]
# print(cars*3)

""" 15. Demonstrate positive and negative indexing in a list"""

# cars=["Audi","BMW","Fortuner","Porshe"]
# print(cars[-1])
# print(cars[2])


"""-------Section 2: Intermediate Level----"""

""" 16. Write a program to remove duplicates from a list."""

# num=[10,20,30,10,20,50]
# new_list=set(num)
# print(list(new_list))

# num=[10,20,30,10,20,50]
# unique_list=[]
# for i in num:
#     found = False
#     for j in unique_list:
#         if i == j:
#             found = True
#             break
#     if not found:
#         unique_list.append(i)
# print(unique_list)

# num=[1,2,3,4,4,3,2,1]
# unique_list=[]
# for i in num:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)



