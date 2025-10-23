# 🗓️ DAY 16 NOTES  
# Topic: Conditional Statements in Python


# 🧠 Definition:
# Conditional statements are used to perform actions based on conditions.
# They check whether a condition is True or False and execute code accordingly.

# ---------------------------------------------
# 1️⃣ Basic If-Else Example
rahul_reached = True

if rahul_reached:
    print("Rahul will attend the class.")
else:
    print("Rahul will not attend the class.")


# OUTPUT:
# Rahul will attend the class.
# ---------------------------------------------


# 2️⃣ Using Comparison Operators
x = 50
y = 40

if x > y:
    print("x is greater than y")
    print("This is code inside the IF block")
    print("Another statement in IF block")
else:
    print("y is greater than or equal to x")
    print("This is code inside the ELSE block")
    print("Another statement in ELSE block")

print("This line is outside of if-else block")


# OUTPUT:
# x is greater than y
# This is code inside the IF block
# Another statement in IF block
# This line is outside of if-else block
# ---------------------------------------------


# 📘 NOTES:
# In Python, colon (:) defines the start of a code block.
# Indentation (spacing) shows which statements belong inside that block.

# In C Language:
# Curly braces { } are used to define the body.
# Semicolon (;) is used to end each statement.

# Example in C:
# if (a > b) {
#     printf("a is greater");
# } else {
#     printf("b is greater");
# }
# ---------------------------------------------


# 3️⃣ Indentation in Python
# Indentation is the backbone of Python syntax.
# It defines code structure and readability.

if True:
    print("This line runs because condition is True")
else:
    print("This line runs because condition is False")

# ---------------------------------------------


# 4️⃣ Example: User Input Condition
num = int(input("Enter any number: "))

if num == 55:
    print("You have entered 55")
else:
    print("You have not entered 55")


# If user inputs 55 → Output: You have entered 55
# If user inputs any other number → Output: You have not entered 55
# ---------------------------------------------



'''
🧾 DAY 16 SUMMARY

✅ Today I learned:
- What conditional statements are.
- How to use if and else blocks.
- The role of colon (:) and indentation in Python.
- Comparison between Python and C syntax.
- Taking user input and checking conditions.

💡 Key Points:
- ":" defines the start of a block.
- Indentation decides which code belongs to which block.
- Python doesn’t use { } braces like C.
- if condition → executes when True
- else → executes when False
'''
