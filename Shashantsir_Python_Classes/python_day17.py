# 🗓️ DAY 17 NOTES  
# Topic: Conditional Statements (Elif, Logical Operators, Modulus)

# ---------------------------------------------
# 1️⃣ Basic If-Else Example

number = 777

if (number < 500):
    print("This line runs when the condition is TRUE.")
else:
    print("This line runs when the condition is FALSE.")

# NOTE:
# Parentheses () around condition are optional in Python.

# OUTPUT:
# This line runs when the condition is FALSE.
# ---------------------------------------------


# 2️⃣ Modulus (%) Operator
# ➡️ Used to find the remainder after division

# Example:
# 12 % 2 = 0  (Even)
# 13 % 2 = 1  (Odd)

# Even numbers: divisible by 2 → remainder 0
# Odd numbers: not divisible by 2 → remainder 1

n = int(input("Enter any number: "))

if n % 2 == 0:
    print("This is an EVEN number.")
else:
    print("This is an ODD number.")

# ---------------------------------------------


# 🧮 Program 1: Check Positive or Negative
fav_number = int(input("Enter your favorite number: "))

if fav_number > 0:
    print("Your number is positive.")
else:
    print("Your number is negative.")

# OUTPUT:
# Enter your favorite number: 25
# Your number is positive.
# ---------------------------------------------


# 🔢 Program 2: Check Even or Odd
my_num = int(input("Enter any number: "))

if my_num % 2 == 0:
    print("Even number detected.")
else:
    print("Odd number detected.")

# OUTPUT:
# Enter any number: 7
# Odd number detected.
# ---------------------------------------------


# 🗳️ Program 3: Voting Eligibility Check
age = int(input("Enter your age: "))
place = input("Do you live in Bihar? (yes/no): ").lower()

if age >= 18 and place == "yes":
    print("✅ You are eligible to vote in Bihar.")
else:
    print("❌ You are not eligible to vote in Bihar.")

# OUTPUT:
# Enter your age: 20
# Do you live in Bihar? yes
# ✅ You are eligible to vote in Bihar.
# ---------------------------------------------



# 🏫 Program 4: Student Grading System
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 65:
    print("Grade: B")
elif score >= 55:
    print("Grade: C")
else:
    print("Grade: F")

print("Thank you for using the grading system.")

# OUTPUT:
# Enter your score (0-100): 50
# Grade: F
# Thank you for using the grading system.
# ---------------------------------------------



'''
🧾 DAY 17 SUMMARY

✅ Today I learned:
- Use of `if`, `elif`, and `else`
- How `modulus (%)` helps identify even and odd numbers
- Taking user input and checking conditions
- Logical operator “and” for combining conditions
- Importance of using `.lower()` for case-insensitive comparison

💡 Key Points:
- `if` checks one condition
- `elif` checks multiple conditions
- `else` executes when all conditions are false
- `n % 2 == 0` → even, otherwise odd
- Indentation and colon (:) define code blocks
'''
