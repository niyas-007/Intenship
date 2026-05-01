"""WHILE LOOP"""

# i = 1
# while i<=3:
#     print("Niyas")
#     i=i+1



# i=1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i=i+1


# i=1
# sum=0
# while i<=10:
#     print("Sum=",sum)
#     sum+=i
#     i=i+1

# i=20
# while i>=1:
#     print(i)
#     i=i-1

# count=0
# limit=int(input("Enter a limit:"))
# x=1
# while x<=limit:
#     if x%3==0:
#         print(x)
#         count+=1
#     x+=1

# i=1
# num=2
# while i<=10:
#     print(f"{i}x2=",i*2)
#     i=i+1


# i=int(input("Enter a number :"))
# num=1
# while num<=10:
#     print(f"{num}x{i}=",num*i)
#     num+=1




"""______________FOR LOOP________________"""



# Syntax:
"""     
        for var in iterable:
        Body
"""


# name="Niyas"
# for char in name:
#     print(char)


# for i in range(10):
#     print(i)

# ph=9539032586
# for int in ph:
#     print(ph)   


# for i in range(10):
#     print(i)

# for x in range(1,11):
#     print(x)

# for x in range(0,11,1):
#     print(x)


"""To get even numbers"""
# for x in range(0,11,2):
#     print(x)

"""TO get odd  numbers"""
# for x in range(1,11,2):
#     print(x)

"""To get multiple of a number"""

# for x in range(0,101,5):
#     print(x)

"""To print reverse as 10-0"""

# for i in range(10,0,-1):
#     print(i)

# s=0
# for x in range(0,11):
#     s+=x
# print(s)


# for i in range(1,11):
#     print(f"{i}x2=",i*2)


# n=int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{n}x{i}=",i*n)


# 1.  Write a program to print numbers from 1 to 10 using a for loop.


"""for i in range(1,11):
    print(i)"""

# 2.  Write a program to print numbers from 1 to 20 using range().

"""for i in range(1,20):
    print(i)"""

# 3.  Write a program to print even numbers from 1 to 50.

"""for i in range(0,50,2):
    print(i)"""

# 4.  Write a program to print odd numbers from 1 to 50.

"""for i in range(1,50,2):
    print(i)
"""

# 5.  Write a program to print numbers from 10 to 1 in reverse order.

"""for i in range(10,0,-1):
    print(i)"""


# 6.  Write a program to print the multiplication table of a given number.

"""for i in range(1,11):
    print(f"{i}x2=",i*2)"""

# Nested loop

# for i in range(1,4):
#     for j in range(i):
#         print(j,end="")
#     print()


# row=3
# for i in range(row):
#     for j in range(row):
#         print("*",end="  ")
#     print()



# length=5
# breadth=10
# for i in range(length):
#     for j in range(breadth):
#         print("*",end="  ")
#     print()

# row=3
# n=5
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row==1 or row==n or col==1 or col==n:
#             print("*",end="  ")
#         else:
#             print(" ",end="  ")

#     print()

# row=3
# col=3
# count=5

# for i in range(row):
#     for j in range(col):
#         print(count,end="  ")
#         count+=5
#     print()


# for i in range(1,6):
#     for j in range(i):
#         print("*",end="  ")
#     print()

# row=6
# for i in range(row):
#     for j in range(i):
#         print(i,end="  ")

#     print()

# row=6
# count=1
# for i in range(row):
#     for j in range(i):
#         print(count,end="  ")
#         count+=1

#     print()

# row=5
# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end="  ")

#     print()

