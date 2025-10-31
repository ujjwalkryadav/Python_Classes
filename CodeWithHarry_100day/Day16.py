# Print Time Using Datetime Module

# Day 16 — match-case in Python
# What I Learned

# The match-case statement is used for pattern matching.
# It works similar to switch statements in other languages.
# case _ is the default case.
# ---------------------------------------------
x = int(input("Enter the value of x: "))

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



# Practice Code-------------------------
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


# Revision Program---------------------------
day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")
# ---------------------------------------------


# Revision Program---------------------------
num = int(input("Enter a number: "))
match num:
    case 0:
        print("Zero is neither even nor odd")

    case _:
        match num % 2:
            case 0:
                print(num, "is Even")
            case 1:
                print(num, "is Odd")

# ---------------------------------------------


'''
Summary
match checks the value
case defines conditions
case _ acts as default
'''