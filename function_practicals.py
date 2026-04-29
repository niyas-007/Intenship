""" Write one function using `print()` and another using `return()` for adding two numbers Compare the outputs."""
# def sum_of_two(a,b):
#     return a+b
# result1=sum_of_two(20,30)
# print(result1)

# def sum_Two(a,b):
#     print(a+b)
# result=sum_Two(50,30)

""""Create a function `product_price(price, tax)` using return. Store the returned value in a variable and print it."""

# def Product_price(price,tax):
#     return price+tax
# Price=int(input("Enter the Price  :"))
# Tax=int(input("Enter the tax :"))
# Total=Product_price(Price,Tax)
# print("Total Amount Payable=",Total)

"""Write a function `greet_user(name)` using print. Try storing it in a variable and observe the output."""

# def greet_user(name):
#     print(name)
# name=input("Enter your Name :")
# user_name=greet_user(name)
# print(user_name)

""" Write a function `calculate_salary(basic, hra, bonus)` that returns gross salary."""

# def calculate_salary(basic,hra,bonus):
#     return basic+hra+bonus
# Basic_salary=int(input("Enter the Basic_salary  :"))
# Hra=int(input("Enter hra :"))
# Bonus=int(input("Enter th Bonus :"))
# Gross_salary=calculate_salary(Basic_salary,Hra,Bonus)
# print("Gross_Salary =",Gross_salary)

"""Create a function `student_result(mark1, mark2, mark3)` that returns total and average."""

# def student_result(mark1,mark2,mark3):
#     return mark1+mark2+mark3,mark1+mark2+mark3/3
# Mark1=int(input("Enter Mark1 :"))
# Mark2=int(input("Enter Mark2 :"))
# Mark3=int(input("Enter Mark3 :"))
# Total=student_result(Mark1,Mark2,Mark3)
# print("Total & Average =",Total)

"""Pass an integer to a function and try changing it inside. Check whether original changes."""

# def num_change(n):
#     n=n+10
#     print("Num IN:",n)
# num =5
# num_change(num)
# print("Num Out =", num)

"""Pass a string to a function and try changing it inside."""

# def change_text(text):
#     text="Hello  " + text
#     print("Inside: ",text)
# Name = "Niyas"
# change_text(Name)
# print("Outside :", Name)

"""Pass a list to a function and append values.Check whether original list changes."""

# def add_to_list(my_list):
#     my_list.append(100)
# num=[10,20,30]
# add_to_list(num)
# print(num)

""" Pass a dictionary to a function and update a key."""

# def update_key(My_dict):
#     My_dict["Varient"]="Blue"
# My_dict={"Model":"Access 125","Varient":"Black"}
# update_key(My_dict)
# print(My_dict)

"""Write a recursive function to print numbers from 1 to n."""

# def num(n):
#     if n == 0:
#         return
#     num(n-1)
#     print(n)
# num(5)

""'Write a recursive function to print numbers from n to 1.'""

# def num(n):
#     if n == 0:
#         return
#     print(n)
#     num(n-1)
# num(5)

"""Write a recursive function to find factorial."""

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

"""Write a recursive function to find Fibonacci series up to n terms."""

# def fibonacci(n):
#     if n<=1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)

# def print_fibonacci(n):
#     for i in range(n):
#         print(fibonacci(i),end="  ")

# print(print_fibonacci(6))

