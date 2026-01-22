# -------------------------------
# OOPs Programming Basics
# -------------------------------

# OOPs = Object Oriented Programming System
# Programming flow:
# Variable -> Function -> Class


# -------------------------------
# Local Variable Example
# -------------------------------

def student_info():
    std_name = "Shivam"   # local variable
    print("here is the student information")
    print("inside this function:", std_name)

student_info()


# -------------------------------
# Local Variable Error Example
# -------------------------------

def student_info():
    std_name = "Shivam"

student_info()
# print(std_name)   # ERROR: local variable not accessible outside function


# -------------------------------
# Global Variable Example
# -------------------------------

default_std_name = "Ujwal"   # global variable

def student_info():
    std_name = "Shivam"      # local variable
    print("inside function global:", default_std_name)
    print("inside function local:", std_name)

student_info()
print("outside function:", default_std_name)


# -------------------------------
# Class Example (Wrong Way)
# -------------------------------

class Student:
    std_name = "Aditya"
    std_roll = "111"

# print(std_name)   # ERROR: cannot access class variable directly


# -------------------------------
# Class Example (Correct Way using Object)
# -------------------------------

class Student:
    std_name = "Aditya"
    std_roll = "111"

my_obj = Student()
print(my_obj.std_name)
print(my_obj.std_roll)


# -------------------------------
# Class with Method
# -------------------------------

class Student:
    def student_info(self):
        print("here is all about student info")

# student_info()   # ERROR: method needs object

our_obj = Student()
our_obj.student_info()
