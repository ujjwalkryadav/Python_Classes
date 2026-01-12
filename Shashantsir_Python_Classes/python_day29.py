# ===============================
# Day 29 Practice
# Topic: Function Definition, Call, Scope (Global & Local)
# ===============================

# ---------- Function Definition ----------
# A function is created using 'def' keyword

def ujwal_function():
    print("Hii Ujwal! how are u")

# Function Call
ujwal_function()


# ---------- Function with Multiple Statements ----------

def ujwal_function():
    print("Hii Ujwal! how are u")
    print("This is Python programming language")
    print("This is Java Programming Language")
    print("C++ is Programming language")

ujwal_function()


# ---------- Global Variable Example ----------

a = 3   # global variable
print(a ** 2)   # 3^2 = 9


# ---------- Local Variable + Function Call Multiple Times ----------

def print_sum_of_numbers(a, b):
    sum = a + b          # local variable
    print("Hii Ravi!, here is the sum of a & b:", sum)

print_sum_of_numbers(22, 5)

print("starting")
print("running")

print_sum_of_numbers(99, 1)

# global variable
my_variable = 10
print(my_variable)