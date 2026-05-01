"""""""""""""""""""STRING SLICING IN PYTHON – LAB PRACTICAL QUESTIONS"""""""""""""""""""

# 1.  Write a Python program to take a string from the user and print the first character using slicing ?

# string=input("Enter a string :")
# print(string[0:1])

# 2.  Write a program to display the last character of a string using slicing?

# string=input("Enter a string :")
# print(string[4:])

# 3.  Given a string, print the first 5 characters using slicing.

# string="Hello World"
# print(string[:5])

# 4.  Write a program to print all characters of a string except the first one.

# string="Hello World"
# print(string[1:])


# 5.  Write a program to print all characters of a string except the last one.

# string="Hello World"
# print(string[:-1:])

# 6.  Given a string, print characters from index 2 to index 6.

# string="Hello World"
# print(string[2:7])

# 7.  Write a program to print every character at even index positions using slicing.

# string="Hello World"
# print(string[::2])

# 8.  Write a program to print every character at odd index positions using slicing.

# string="Hello World"
# print(string[1::2])

# 9.  Write a program to reverse a string using slicing.

# string="Python"
# print("Reversed string=",string[::-1])

# 10. Given a string, print the middle character(s) using slicing (assume length can be even or odd).

# s = input("Enter a string: ")
# n = len(s)

# print(s[(n-1)//2 : n//2 + 1])