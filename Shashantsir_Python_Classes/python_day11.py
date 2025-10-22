# 🗓️ DAY 11 NOTES
# Topic: Bitwise Operators and Membership Operators

# 1️⃣ Bitwise AND Operator (&)
a = 10
b = 4
x = 5
y = 3

print(a & b)   # 0
print(x & y)   # 1
print(5 & 6)   # 4
#program END ---------------



# 2️⃣ Bitwise AND Explanation
# Returns 1 if both bits are 1, else 0

a = 10  # 1010
b = 4   # 0100
print(a & b)   # 0000 => 0

x = 5   # 0101
y = 3   # 0011
print(x & y)   # 0001 => 1

# Example: 5 & 6
# 5 => 0101
# 6 => 0110
# Result => 0100 => 4
#program END ---------------


# 4️⃣ Bitwise OR Operator (|)
A = 5
B = 6
print(A | B)
# 5 = 0101
# 6 = 0110
# OR = 0111 => 7
#program END ---------------


# 5️⃣ Bitwise XOR Operator (^)
A = 5
B = 6
print(A ^ B)
# 5 = 0101
# 6 = 0110
# XOR = 0011 => 3
#program END ---------------


# 6️⃣ Membership Operators
# Used to test whether a value exists in a sequence (like list, string, tuple, etc.)

Ravi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(5 in Ravi)        # True  -> 5 is present
print(15 not in Ravi)   # True  -> 15 is not present
#program END ---------------


'''
📝 DAY 11 SUMMARY

✅ Today we learned:
- Bitwise AND (&): Returns 1 if both bits are 1.
- Bitwise OR (|): Returns 1 if at least one bit is 1.
- Bitwise XOR (^): Returns 1 if bits are different.
- Binary Number Representation (0–15).
- Membership Operators (in, not in):
    -> "in" checks if a value exists.
    -> "not in" checks if a value doesn’t exist.

💡 Key Idea:
Bitwise operators work at the **binary level** (bit-by-bit comparison),
while membership operators work at the **sequence level** (list, string, etc.).
'''
