# # 🗓️ DAY 8 NOTES 
# Input Function

#program 1 ( INPUT FUNCTION SUM ) ---------------
first_value = int(input("Enter first value: "))
second_value = int(input("Enter second value: "))
sum = first_value + second_value
print("The sum of first value and second value is:", sum)
#program END  ---------------


#program 2 ( INPUT FUNCTION COMBINE TWO STRINGS ) ---------------
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Your full name is:", full_name)
#program END ---------------



#program 3 ( Logical Operators ) ---------------
A = 10
B = 20

print("A < B and A == 10:", A < B and A == 10)
print("A > B and A != B:", A > B and A != B)
print("A < B or A == 10:", A < B or A == 10)
print("A < B or A > 50:", A < B or A > 50)
#program END ---------------


#program 3 ( Bitwise Operators ) ---------------
a = 5      # binary: 0101
b = 3      # binary: 0011

print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 1 =", a << 1) # Left Shift
print("a >> 1 =", a >> 1) # Right Shift
#program END ---------------



#program 3 ( PRACTICE ) ---------------
# Check if a number is between 10 and 50
num = int(input("Enter a number: "))
if num > 10 and num < 50:
    print("Number is between 10 and 50")
else:
    print("Number is out of range")
#program END ---------------

'''
🧾 Day 8 Summary
✅ Today I practiced:
Taking input from user and typecasting it.
Performing addition and string concatenation.
Using logical operators (and, or, not).
Performing bitwise operations (&, |, ^, ~, <<, >>).
Applied conditions using if-else with logical operators.
💡 Main concept learned:
Difference between logical and bitwise operations, and how input() always returns string by default.
'''