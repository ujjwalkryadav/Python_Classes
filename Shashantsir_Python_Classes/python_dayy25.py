# Day 25 Practice
# Topic: Set in Python
# Practicing basic set concepts taught in class

# Creating a set with mixed data types
my_set = {11, 22, 33, 44, 55, "Ujjwal", "Ravi", 5.2}
print("Initial set:", my_set)

# Checking how set removes duplicate values automatically

practice_set = {11, 22, 33, 44, 55, 11, 22, 33}
print("Set after removing duplicates:", practice_set)

# Practice of add() method (adding one element)

my_set = {11, 22, 33, 55, 44, 2}
print("Before add():", my_set)

my_set.add(77)   # adding new element
print("After add():", my_set)

# Practice of update() method (adding multiple elements)

my_set = {11, 22, 33, 55, 44, 2}
print("Before update():", my_set)

my_set.update({77, 999, 102})
print("After update():", my_set)

# Practice of remove() method

my_set = {11, 22, 33, 55, 44, 2}
print("Before remove():", my_set)

my_set.remove(22)   # removing specific element
print("After remove():", my_set)

# Sets do not support indexing (just checking)

my_set = {11, 22, 33, "rahul", "ravi", 8.8}
print("Current set:", my_set)

# Uncommenting below line will give error
# print(my_set[2])

# Looping through a set to print all elements

my_set = {11, 22, 33, "rahul", "ravi", 8.8}
print("Looping through set:")

for item in my_set:
    print(item)