# class Student:
#     school_name="QIS"
#     course="Python Full stack"

#     def __init__(self,s_id,name,age,email):       #Constructor Created
#         print("Comstructor Created")

# Aslam=Student(10,"Muhammed",22,"abx@gmail.com")
# shamil=Student(10,"Muhammed",22,"abx@gmail.com")


# class Student:
#     school_name="QIS"
#     course="Python Full stack"

#     def __init__(self,s_id,name,age,email):             #constructor
#         self.Student_id=s_id
#         self.S_name= name                               #Passed values is called instances attribute.
#         self.age= age
#         self.email=email

#     def get_details(self):
#         print(f"Student_id : {self.Student_id}\nStudent_name : {self.S_name}")
#         print(f"Age : {self.age}\nEmail :{ self.email}")


# Niyas=Student(s_id=101,name="Niyas",age=20,email="niyas@gmail.com")
# Niyas.get_details()

# class Employee:
#     Company_name="Mahindra Logistics"
#     Branch_name="FCJD"

#     def __init__(self,emp_id,emp_name,emp_salary,emp_email):
#         self.Employee_id=emp_id
#         self.Employee_name=emp_name
#         self.Salary=emp_salary
#         self.Email=emp_email

#     def get_details(self):
#         print(f"Employee_id : {self.Employee_id}\nEmployee_name : {self.Employee_name}")
#         print(f"Salary : {self.Salary}\nEmail :{ self.Email}")

#     def update_salary(self):
#         if self.Salary > 100000:
#             self.Salary = self.Salary + self.Salary * 15 / 100

#     def resign(self):
#         self.Company_name="Amazon"
#         self.Branch_name="MPMD"
#         self.Employee_id=205
#         self.Salary=20000

# Nasif=Employee(emp_id=101,emp_name="Nasif.V",emp_salary=100010,emp_email="2005nasifv@gmail.com\n")
# print(Nasif.Company_name)
# print(Nasif.Branch_name)

# Nasif.update_salary()
# Nasif.get_details()
# Shakir=Employee(emp_id=105,emp_name="Muhammed Shakir Mp",emp_salary=17000,emp_email="shakirfcjd@gmail.com")

# Shakir.update_salary()
# Shakir.resign()
# print(Shakir.Company_name)
# print(Shakir.Branch_name)

# Shakir.get_details()


# class Employee:
#     Company_name="Mahindra Logistics"
#     Branch_name="FCJD"

#     def __init__(self,emp_id,emp_name,emp_salary,emp_email):
#         self.Employee_id=emp_id
#         self.Employee_name=emp_name
#         self.Salary=emp_salary
#         self.Email=emp_email

#     def get_details(self):
#         print(f"Employee_id : {self.Employee_id}\nEmployee_name : {self.Employee_name}")
#         print(f"Salary : {self.Salary}\nEmail :{ self.Email}")

#     def update_salary(self):
#         if self.Salary > 100000:
#             self.Salary = self.Salary + self.Salary * 15 / 100

#     def resign(self):
#         self.Company_name="Amazon"
#         self.Branch_name="MPMD"
#         self.Employee_id=205
#         self.Salary=20000

#     def __del__(self):
#         print("Constructor Deleted")                    #Destructor called

# Nasif=Employee(emp_id=101,emp_name="Nasif.V",emp_salary=100010,emp_email="2005nasifv@gmail.com\n")
# # print(Nasif.Company_name)
# # print(Nasif.Branch_name)

# # Nasif.update_salary()
# # Nasif.get_details()
# Shakir=Employee(emp_id=105,emp_name="Muhammed Shakir Mp",emp_salary=17000,emp_email="shakirfcjd@gmail.com")

# # Shakir.update_salary()
# # Shakir.resign()
# # print(Shakir.Company_name)
# # print(Shakir.Branch_name)

# # Shakir.get_details()

# class Employee:
#     Company_name="Mahindra Logistics"
#     Branch_name="FCJD"

#     def __init__(self,emp_id,emp_name,emp_salary,emp_email):
#         self.Employee_id=emp_id
#         self.Employee_name=emp_name
#         self.Salary=emp_salary
#         self.Email=emp_email


# Shakir=Employee(emp_id=105,emp_name="Muhammed Shakir Mp",emp_salary=17000,emp_email="shakirfcjd@gmail.com")

# Nasif=Employee(emp_id=101,emp_name="Nasif.V",emp_salary=100010,emp_email="2005nasifv@gmail.com\n")

# print(getattr(Nasif,'Employee_name'))                    # in-built Function(To Access the attribute of an object)


# setattr(Nasif,'Phone',808050107)
# print(Nasif.Phone)

# setattr(Nasif,'emp_email','nasiffcjd@gmail.com')         #in-built Fuction(To add new attribute or to update an esisting attribute)
# print(Nasif.emp_email)

# print(hasattr(Nasif,'Employee_name'))
# print(hasattr(Nasif,'Employee_place'))                    #in-built Function(To check if an attribute is exist or not)

# delattr(Nasif,'Employee_name')
# print(Nasif.emp_name)                                     #in-built Function(To delete an attribute in an object)


class Bank:
    Bank_name="State Bank Of India"


    def __init__(self,acc_no,name,ifsc,balance,):
        self.Account_no=acc_no
        self.Name=name
        self.IFSC=ifsc
        self.Balance=float(balance)

    def get_details(self):
        print(f"Account_no : {self.Account_no}\nName : {self.Name} ")
        print(f"IFSC CODE : {self.IFSC}")

    def get_balance(self):
        print(f"Account_no : {self.Account_no}\nBalance :{self.Balance}")

    def withdraw(self):
        a = float(input("Enter Amount to Withdraw : "))

        if a > self.Balance:
            print("Insufficient Fund....!!!")
        else:
            self.Balance -= a
            print("Balance Amount =", self.Balance)
            
    def Deposit(self):
        b = float(input("\nEnter Amount to Deposit : "))
        Total=self.Balance + b
        print("\nTransaction Successfull .Current Balance =",Total)


Abdulla=Bank(acc_no=20405060,name="Abdulla K",ifsc="SBIN007Z500",balance="250000")
Abdulla.get_details()
Abdulla.get_balance()
Abdulla.withdraw()
Abdulla.Deposit()