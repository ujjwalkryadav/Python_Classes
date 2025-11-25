# Tuple Based Mini Project: Student Marks Analyzer
# Features used:
# => for loop
# => while loop
# => input()
# => slicing
# => tuple operations

print("----- Student Marks Analyzer -----")

# Step 1: Take student names as comma-separated input
names = input("Enter student names (comma separated): ").split(',')
names = tuple([n.strip() for n in names])

print("\nStudents Registered:")
for n in names:
    print("-", n)

# Step 2: Take marks for each student and store in a tuple
marks_list = []
for n in names:
    m = int(input(f"Enter marks for {n}: "))
    marks_list.append(m)
marks = tuple(marks_list)

# Step 3: Show first 3 students using slicing
print("\nFirst 3 Students:")
print(names[:3])

# Step 4: Calculate total marks using while loop
total = 0
i = 0
while i < len(marks):
    total += marks[i]
    i += 1
print("\nTotal Marks of Class:", total)

# Step 5: Highest and Lowest marks
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

# Step 6: Check if a student's marks exist
check = int(input("\nEnter marks to search: "))
if check in marks:
    print("Marks found!")
else:
    print("Marks not found.")

# Step 7: Create a tuple of Pass/Fail
# Pass = >= 33

mood = input("Do You want to get summery of test (Y/N)")

if mood == "Y":
 result = ()
 for m in marks:
     if m >= 33:
         result += ("Pass",)
     else:
         result += ("Fail",)

 print("\nPass/Fail Result:")
 for i in range(len(names)):
     print(names[i], "-", result[i])

 print("\n----- END OF PROJECT -----")

else:
    print("\n----- END OF PROJECT -----")
