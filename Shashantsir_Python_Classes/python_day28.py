# ===============================
# Day 28 Practice
# Topic: Function (Introduction)
# ===============================

# Function helps to:
# - save time
# - reuse code
# - improve readability


# ---------- Simple Function ----------

def greet():
    print("Hello, welcome to Python class")

greet()
greet()   # function reuse


# ---------- Function with parameter ----------

def say_hello(name):
    print("Hello", name)

say_hello("Ujwal")
say_hello("Ravi")


# ---------- Function for addition ----------

def add_numbers(a, b):
    print("Sum is:", a + b)

add_numbers(10, 20)
add_numbers(5, 7)


# ---------- Function returning value ----------

def square(num):
    return num * num

result = square(4)
print("Square is:", result)


# ---------- Function improves readability ----------

def student_info(name, city):
    print("Student Name:", name)
    print("City:", city)

student_info("Ujwal", "Bangalore")