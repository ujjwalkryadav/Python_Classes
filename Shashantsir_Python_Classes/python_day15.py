# 🗓️ DAY 15 NOTES
# Topic: List Slicing in Python


# 1️⃣ List Basics
my_list = [111, 222, 444, 44, 55, 66]

# Positive Indexing
#  0    1    2    3    4    5
# 111  222  444   44   55   66

# Negative Indexing
# 111  222  444   44   55   66
# -6   -5   -4   -3   -2   -1
#program END ---------------


# 2️⃣ Two-Parameter Slicing
# Syntax: list[start:end] (end excluded)
print("Without using starting point:", my_list[:])      # All elements
print("First four elements:", my_list[:4])            # 0 to 3
print("Using slicing [2:4]:", my_list[2:4])          # 2 to 3
print("Using slicing [0:5]:", my_list[0:5])          # 0 to 4
#program END ---------------


# 3️⃣ Three-Parameter Slicing (start:end:step)
my_new_list = [11,22,33,44,55,66,77,88,99,100]

# Default step = 1
print("Using gap 1:", my_new_list[1:8:1])
print("Without gap (two params):", my_new_list[1:8])

# Step = 2 (skip 1 element)
print("Gap of 2:", my_new_list[0:9:2])   # 11,33,55,77,99

# Step = 3
print("Gap of 3:", my_new_list[::3])     # 11,44,77,100

# Reversing list using negative step
print("Reversed list:", my_new_list[::-1])

# Negative slicing with start > end
print("Custom reverse slice [4:1:-1]:", my_new_list[4:1:-1])  # 55,44,33
#program END ---------------


# 4️⃣ Accessing elements with positive & negative index
print("Original list:", my_list)
print("Second element:", my_list[1])
print("Second last element:", my_list[-2])
#program END ---------------


# 5️⃣ Mixed type list slicing
rohit_list = [1.1, 22, "Coffee", False, 55.5]
print("Accessing element in mixed list:", rohit_list[2])   # Coffee

# Using negative slicing
print(my_list[0:-1])   # Exclude last element
print(my_list[-5:-1])  # From -5 to -2
#program END ---------------


'''
🧾 DAY 15 SUMMARY

✅ Today I practiced:
- List indexing (positive and negative)
- Two-parameter slicing (start:end)
- Three-parameter slicing (start:end:step)
- Using step to skip elements
- Reversing a list with negative step
- Slicing in mixed-type lists

💡 Main Concept:
- List slicing allows extracting sublists efficiently.
- Step parameter can control skipping elements or reversing list.
- Negative indices traverse list from right to left.
'''
