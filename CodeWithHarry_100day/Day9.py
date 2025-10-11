

a = "5"
b = "6"

print(a + b)     # 5 + 6 = 11 (expected), but output is 56 because both are strings
print(int(a) + int(b))  # This is Explicit Conversion (Typecasting) to get accurate result 5 + 6 = 11

a = 5.6
b = 6

print(a + b)     # This is Implicit Conversion (Typecasting)
# Here 5.6 is a float number and 6 is an integer.
# Python automatically converts 6 into float for accurate result.






#Summary Of Day 9
# Typecasting in Python
# Two Type Of Typecasting in Python
# 1. Explicit Conversionn
# 2. Implicit Conversion 