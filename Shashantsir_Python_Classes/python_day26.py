# ===============================
# Day 26 Practice
# Topic: Set Methods + Typecasting + #Dictionary
# ===============================

# ---------- SET METHODS ----------

# pop() -> removes random element
my_set = {11, 22, 33, "rahul", "ravi", 8.8}
print("before pop:", my_set)

my_set.pop()
print("after pop:", my_set)


# discard() -> no error if element not found
my_set = {11, 22, 33, "rahul", "ravi", 8.8}
print("before discard:", my_set)

my_set.discard(224565432)
print("after discard:", my_set)


# clear() -> removes all elements
my_set = {11, 22, 33, "rahul", "ravi", 8.8}
print("before clear:", my_set)

my_set.clear()
print("after clear:", my_set)


# ---------- TYPECASTING ----------

# String -> Integer (Explicit)
my_variable = "23"
print(type(my_variable))

my_new_variable = int(my_variable)
print(my_new_variable)
print(type(my_new_variable))


# Integer -> String
my_variable = 23
print(type(my_variable))

my_new_variable = str(my_variable)
print(my_new_variable)
print(type(my_new_variable))


# Boolean -> Integer
my_variable = True
print(type(my_variable))

my_new_variable = int(my_variable)
print(my_new_variable)
print(type(my_new_variable))


# Integer -> Boolean
my_variable = 1
print(type(my_variable))

my_new_variable = bool(my_variable)
print(my_new_variable)
print(type(my_new_variable))


# Boolean rule check
my_variable = 0
print(type(my_variable))

my_new_variable = bool(my_variable)
print(my_new_variable)
print(type(my_new_variable))


# ---------- IMPLICIT TYPECASTING ----------

my_variable = 6.7
my_second_variable = 4

print(type(my_variable))
print(type(my_second_variable))

print("after implicit typecasting:", my_variable + my_second_variable)


# ---------- DICTIONARY INTRODUCTION ----------

my_dict = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(my_dict)


# List vs Dictionary (practice)
my_listt = [11, 22, 33, [5, 6, 7], 55]
print(my_listt)