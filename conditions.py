# 1.  Check Even or Odd Write a program to check whether a given number is even or odd.

"""num=int(input("Enter a number :"))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is odd")
    """

# 2.  Positive, Negative or Zero Write a program to check if a number is positive, negative or zero.

"""
num=int(input("Enter a number :"))
if num>=0:
    print("Number is +ve")
else:
    print("Number is -ve")"""

# 3.  Find the Largest of Two Numbers Take two numbers from the user and print the larger one.

"""num1=int(input("Enter fisrt number :"))
num2=int(input("Enter Second number :"))
if num1>num2:
    print("Largest=",num1)
else:
    print("Largest=",num2)"""


# 4 .Find the Largest of Three Numbers Take three numbers and print the largest among them.

"""a=int(input("Enter fisrt number :"))
b=int(input("Enter Second number :"))
c=int(input("Enter third number :"))

if a>b and a>c:
    print("Largest number is",a)
elif b>a and b>c:
    print("Largest number is",b)
else:
    print("Largest number is ",c)"""


# 5.  Check Eligibility to Vote Ask the user for their age and check if they are eligible to vote (18 or above).

"""age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible for vote")
else:
    print("You are eligible Not for vote")"""

# 6.  Pass or Fail Ask the user for their mark and print Pass if mark is 40 or above, otherwise Fail.

"""mark=int(input("Enter your Mark:"))
if mark>40:
    print("Pass")
else:
    print("Fail")"""

# 7.  Grade System Input marks and display grade: 90+ : A 80-89 : B 70-79: C 60-69 : D Below 60 : Fail

"""mark=int(input("Enter your Mark:"))
if mark>=90:
    print("Grade:A")
elif mark>=80:
    print("Grade:B")
elif mark>=70:
    print("Grade:C")
elif mark>=60:
    print("Grade:D")
else:
    print("Fail")"""

# 8.  Leap Year Checker Input a year and check whether it is a leap year or not.

"""year=int(input("Enter a Year:"))
if (year % 4 == 0 and year % 100 !=0) or( year % 400==0):
    print("Leap year")
else:
    print("Not a leap year")"""

# 9.  Divisible by 5 and 11 Check whether a number is divisible by both 5 and 11.

"""num=int(input("Enter a number :"))
if num%5==0 and num%11==0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")"""


# 10. Check Character Type Input a character and check if it is a vowel or consonant.

"""char=input("Enter a character:")
if char in "aeiou":
    print("Its a vowel")
else:
    print("Its constant")"""


# 11. Simple Login System Ask for username and password. If both are correct, print Login Successful, else Login Failed.

"""user="Admin_123"
pswd="Admin@1212"
username=input("Enter your username :")
password=input("Enter your password :")
if user==username and pswd==password:
    print("Login is successfull")
else:
    print("Login Failed")"""


# 12. Number Comparison Game Take two numbers. If first is greater print “First is greater”, else print “Second is greater”.

"""num1=int(input("Enter fisrt number :"))
num2=int(input("Enter Second number :"))
if num1>num2:
    print("First is greater")
else:
    print("Second is greater")
"""


# 13. Check Temperature If temperature > 30 print Hot, if between 20 and30 print Warm, else Cold.


"""
temp=int(input("Enter the Temprature :"))
if temp > 30:
    print("hot")
elif temp>20 and temp<30:
    print("Warm")
else:
    print("cold")"""

# 14. Check Salary Bonus If salary > 50000, give bonus 5000 else bonus 2000. Print total salary.

"""salary=int(input("Enter the salary :"))
if (salary >50000):
    print("Total salary=",salary+5000)
else:
    print("Total salary=",salary+2000)"""


# 15. Check Shopping Discount If bill amount > 1000, give 10% discount else no discount.

"""bill_amount=int(input("Enter the bill amount :"))
if bill_amount>1000:
    print("Total Bill :",bill_amount-bill_amount*0.10)
else:
    print("Total Bill :",bill_amount)"""


# 16. Age Category If age < 13 print Child If age between 13 and 19 print Teen Else print Adult

"""Age=int(input("Enter Age :"))
if Age < 13:
    print("Child")
elif Age>13 and Age<19:
    print("Teen")
else:
    print("Adult")"""

# 17. Electricity Bill Calculator (Simple) If units <= 100 charge 2 per unit If 101-200 charge 3 per unit Above 200 charge 5 per unit

"""unit=int(input("Enter the unit :"))
if unit <=100:
    print("Total Bill=",unit*2)
elif unit>100 and unit<=200:
    print("Total Bill=",unit*3)
else:
    print("Total Bill=",unit*5)

"""

# 18. Check Number is Multiple of 3 or 7 Input a number and check if it is multiple of 3 or 7.

"""number=int(input("Enter a number:"))
if number%3==0:
    print("Multiple of 3")
elif number%7==0:
    print("Multiple of 7")
else:
    print("Not multiple by 3 or 7")"""

# 19. Check Password Strength If password length >= 8 print Strong Password else Weak Password.

"""password=input("Enter a password:")
l=len(password)
if l >=8:
    print("Strong Password ")
else:
    print("Weak Password")
"""


# 20. Find Smallest of Two Numbers Take two numbers and print the smaller one.

"""num1=int(input("Enter fisrt number :"))
num2=int(input("Enter Second number :"))
if num1<num2:
    print("Smallest=",num1)
else:
    print("Smallest=",num2)"""