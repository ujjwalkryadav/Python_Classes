# Print Time Using Datetime Module

# Day 16 — match-case in Python
# What I Learned

# The match-case statement is used for pattern matching.
# It works similar to switch statements in other languages.
# case _ is the default case.

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)



# Practice Code
x = int(input("Enter value: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x != 90:
        print(x, "is not 90")
    case _:
        print(x)

# Revision Program
num = int(input("Enter number: "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")



'''
Summary
match checks the value
case defines conditions
case _ acts as default
'''