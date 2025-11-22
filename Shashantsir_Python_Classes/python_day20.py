# 🗓️ DAY 20 NOTES
# Topic: For Loop
"""
🏫 Program 1: For Loop in C
// Basic for loop in C → runs from 0 to 4
for(int i = 0; i < 5; i++){
    printf("%d", i);   // prints value of i
}
"""
# 🏫 Program 2: 
# range(5) → 0 to 4
for i in range(5):
    print(i)

# 🏫 Program 3: Range (0,5)
# same output → 0 to 4
for i in range(0,5):
    print(i)

# 🏫 Program 4: Range (13,18)
# prints 13 to 17
for i in range(13,18):
    print(i)

# 🏫 Program 5: Range (22,27)
# prints 22 to 26
for i in range(22,27):
    print(i)

# 🏫 Program 6: List Slicing
# slice index 0 to 2
listt = [22,21,23,33,44,55]
print(listt[0:3])

# 🏫 Program 7: Slicing With Step
# step = 2 (skip alternate elements)
print(listt[0:5:2])

# 🏫 Program 8: Even Numbers Using Range
# even numbers from 2 to 20
for i in range(2,21,2):
    print(i)

# 🏫 Program 9: Multiples of 5
# multiples of 5 → 5 to 50
for i in range(5,51,5):
    print(i)

# 🏫 Program 10: Negative to Positive Range
# -2 to 4
for i in range(-2,5):
    print(i)

# 🏫 Program 11: Two Loop Methods
# method 1 → step 1
for i in range(9,23,1):
    print("first output", i)

# method 2 → default step 1
for i in range(9,23):
    print("second output", i)

# 🧾 DAY 20 SUMMARY
# Learned C and Python for loop structure
# Understood start, stop, step in Python ranges
# Practiced printing different number sequences
# Learned list slicing and step slicing
# Loops run until the condition becomes false
# range(end) → starts from 0
# range(start, end, step) → full control of loop