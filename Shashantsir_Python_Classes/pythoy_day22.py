# 🗓️ DAY 22 NOTES
# Topic: LIST METHODS (insert, remove, pop, index, count, sort, reverse, copy, clear)

# PROGRAM 1 — insert()
my_list = [11, 22, 33, 44]
print("Before:", my_list)

my_list.insert(2, 999)  # insert element at a specific index
print("After:", my_list)


# PROGRAM 2 — remove()
my_list = [11, 22, 22, 33, 44]
print("Before:", my_list)

my_list.remove(22)  # removes first occurrence of element
print("After:", my_list)


# PROGRAM 3 — pop()
my_list = [11, 22, 24, 33, 44]
print("Before:", my_list)

my_list.pop(1)  # removes element at index 1
print("After:", my_list)


# PROGRAM 4 — index()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100]
print("Index of 24:", my_list.index(24))  # returns index of element


# PROGRAM 5 — count()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100]
print("Count of 100:", my_list.count(100))  # counts occurrences


# PROGRAM 6 — sort()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100, 77]
print("Before:", my_list)

my_list.sort()  # sorts list ascending
print("After:", my_list)


# PROGRAM 7 — reverse()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100, 77]
print("Before:", my_list)

my_list.reverse()  # reverses list
print("After:", my_list)


# PROGRAM 8 — copy()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100, 77]
copied_list = my_list.copy()  # creates copy

print("Copied list:", copied_list)


# PROGRAM 9 — clear()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100, 77]
copied_list = my_list.copy()

print("Copied list:", copied_list)
print("Before:", my_list)

my_list.clear()  # clears entire list
print("After:", my_list)

'''
🧾 DAY 22 SUMMARY ->
-> insert() adds element at specific index.
-> remove() deletes first matching element.
-> pop() removes element by index (default last).
-> index() returns position of element.
-> count() returns frequency of element.
-> sort() arranges list ascending.
-> reverse() flips the list order.
-> copy() duplicates list.
-> clear() empties list completely.
'''