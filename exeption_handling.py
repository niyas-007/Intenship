"""raise using in python"""

# try:
#     mark=500
#     if mark < 200:
#         raise ValueError("value must be less than or equal to 200")
# except Expataion as e:
#     print(e)




# print("Hello")


# try:
#     mark="500"
#     if int(mark) > 200:
#         raise ValueError("value must be less than or equal to 200")
#     elif isinstance(mark,int):
#         raise TypeError("Value must be given in String")
# except Exception as e:
#     print(e)

"""Custom Exception Error Handling """

# class VoteError(Exception):
#     pass

# age = 20
# if age < 18:
#     raise VoteError("Age must be Greater than or Equal to 18")
# print("You are Eligible for Vote")

# """Example - 1"""
# age=-5

# if age < 0:
#     raise ValueError("Age cannot be negatiev")

# print("Valid age")


# num = int(input("Enter a positive number: "))
# if num <= 0:
#     raise ValueError("Number must be positive")


# print("Square:",num*num)

