# ===============================
# Day 31 Practice
# Topic: Function (Revision + Practice)
# ===============================

# What is a Function?
# A function is a block of code that performs a specific task when called.
# Advantages:
# - Code reusability
# - Better readability
# - Saves time


# ---------- Function Definition & Call ----------

def sum_of_numbers(a, b, c):
    print("The sum is :", a + b + c)

sum_of_numbers(9, 2, 1)


# ---------- Function with Multiple Statements ----------

def interview_process():
    print("Interview start")
    print("First round: Introduction")
    print("Second round: Machine coding round")
    print("Third round: HR round")
    print("Now, YOU are selected")

interview_process()


# ---------- Function Syntax Example ----------

def my_function_name(parameters):
    print("This is function body")

my_function_name("arguments")


# ---------- Taking Input from User ----------

a = int(input("Enter a number: "))
print("You entered:", a)


# ---------- Task: Check Even or Odd (Without return) ----------

def check_even_odd(num):
    if num % 2 == 0:
        print("This is even number:", num)
    else:
        print("This is odd number:", num)

print("Hiii, Start")

check_even_odd(77)

print("Loop Testing:")
for i in range(0, 12):
    if i == 7:
        continue
    print(i)

check_even_odd(89)

my_listt = ["Ravi", "rohit", 44, 55, 88]
for i in my_listt:
    if i == 44:
        break
    print(i)

check_even_odd(90)


# ---------- Task: Check Even or Odd (With return - Recommended) ----------

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))

result = check_even_odd(number)
print(f"The number {number} is {result}.")