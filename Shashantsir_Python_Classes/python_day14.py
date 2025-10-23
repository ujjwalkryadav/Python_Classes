# 🗓️ DAY 14 NOTES
# Topic: String Methods and List Indexing in Python


# 1️⃣ String Methods
# A string is a sequence of characters enclosed in single (' '), double (" "), or triple (''' ''' or """ """) quotes.

sample_text = "    Hello Python "
print("Original String: '", sample_text)
print("After strip(): '", sample_text.strip())
# Output:
# Original String: '     Hello Python 
# After strip(): ' Hello Python
#program END ---------------


# Other String Methods
username = "Aditya"
nickname = "codeMaster"

print("Length of username:", len(username))
print("Lowercase username:", username.lower())
print("Uppercase username:", username.upper())
print("Title Case sample_text:", sample_text.title())
print("Capitalized nickname:", nickname.capitalize())
#program END ---------------


# Using replace, count, index, split
course_name = "python development"
student_name = "Rahul"

print("Original String:", course_name)
print("After replace 'python' with 'java':", course_name.replace("python", "java"))
print("Count of 'e' in course_name:", course_name.count("e"))
print("Index of 'a' in student_name:", student_name.index("a"))

special_text = "Welcommmmmme"
print("Original String:", special_text)
print("After strip():", special_text.strip())
print("After split():", course_name.split(" "))
print("Index of 'm' in special_text:", special_text.index("m"))
#program END ---------------


# 2️⃣ List Basics
# A list can store multiple types of data: integers, strings, floats, booleans, even other lists

my_letters = ['A', 'B', 'C']
my_mixed_list = [10, 'Python', 3.14, True]
nested_list = [[1,2,3], ['X', 'Y', 'Z'], [False, True]]
#program END ---------------


# 3️⃣ List Indexing (Positive)
students = ['Ankit', 'Rohit', 'Sneha', 'Priya']
print(students)
print("First student:", students[0])
print("Second student:", students[1])
print("Third student:", students[2])
print("Fourth student:", students[3])
# Output:
# ['Ankit', 'Rohit', 'Sneha', 'Priya']
#program END ---------------


# 4️⃣ List Indexing (Negative)
students = ['Ankit', 'Rohit', 'Sneha', 'Priya']
print("Last student:", students[-1])
print("Second last student:", students[-2])
print("Third last student:", students[-3])
print("Fourth last student:", students[-4])
# Output:
# Last student: Priya
# Second last student: Sneha
# Third last student: Rohit
# Fourth last student: Ankit
#program END ---------------
print( "\n" + "🧾 DAY 14 SUMMARY" + "\n")

'''
🧾 DAY 14 SUMMARY

✅ Today I practiced:
- Using various string methods: len(), lower(), upper(), title(), strip(), replace(), capitalize(), find(), count(), index(), split().
- Understanding lists and storing multiple types of data.
- List indexing (positive and negative).

💡 Main Concept:
- Strings are sequences of characters that can be manipulated using built-in methods.
- Lists are ordered collections that allow easy access via positive or negative indexing.
- Unique variable names help avoid confusion and make the code readable.
'''
