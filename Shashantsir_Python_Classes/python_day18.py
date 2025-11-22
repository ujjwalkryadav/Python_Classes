# 🗓️ DAY 18 — NOTES 
# Topic: If–Else, Elif, Nested If, Comparisons
# 🏫 Program 1: Check Positive / Negative / Zero
#   x > 0  -> Positive
#   x < 0  -> Negative
#   x == 0 -> Zero

my_num = int(input("Enter the number: "))

if my_num > 0:
    print("It is a positive number")
elif my_num == 0:
    print("It is zero")
else:
    print("It is a negative number")

# 🏫 Program 2: Check Greater (Two Numbers)

my_1st_num = int(input("Enter the first number: "))
my_2nd_num = int(input("Enter the second number: "))

if my_1st_num > my_2nd_num:
    print("First number is greater")
else:
    print("Second number is greater")

# 🏫 Program 3: Check Greatest (Three Numbers)

my_1st_num = int(input("Enter the first number: "))
my_2nd_num = int(input("Enter the second number: "))
my_3rd_num = int(input("Enter the third number: "))

if my_1st_num > my_2nd_num and my_1st_num > my_3rd_num:
    print("First number is greatest")
elif my_2nd_num > my_1st_num and my_2nd_num > my_3rd_num:
    print("Second number is greatest")
else:
    print("Third number is greatest")

# 🏫 Program 4: Create Login Credential using If–Else

username = input("Enter Yor Id")
password = input("Enter Password")

if username == "ujwal@123" and password == "12345678":
    print("Login Successfully")

elif username == "ravi@123" and password == "12345678":
    print("Your username is incorrect")

else:
    print("Invalid Credential")

# 🏫 Program 5: Revise If / Else / Elif (Traffic Light)

traffic_light = "yellow"

if traffic_light == "red":
    print("Please Stop")

elif traffic_light == "yellow":
    print("Ready to go")

elif traffic_light == "green":
    print("Go")

else:
    print("Invalid color")

# Nested If — Notes
# Nested If = If inside another If
# Nested Box Concept

# 🏫 Program 1: Check Voting Eligibility Using Nested If

age = int(input("Hi, Shivam! Please enter your age: "))
resident = "Bihar"

if age > 18:
    if resident == "Bihar":
        print("You are eligible to vote")
    else:
        print("Sorry, you are not eligible because you are not a resident of Bihar")
else:
    print("You are not eligible to vote")

# 🏫 Program 2: Check DRCC Loan Eligibility Using Nested If

resident = input("Enter your residence: ")
is_12th_pass_out = True
have_bonafide_certificate = True

if resident.lower() == "bihar":
    if is_12th_pass_out == True:
        print("Okay, now please apply for bonafide certificate")

        if have_bonafide_certificate == True:
            print("Congrats, You can apply for DRCC loan")
        else:
            print("Sorry, you need to apply for bonafide certificate first")

    else:
        print("First, you have to complete 12th")
else:
    print("Sorry, You can't get a loan from DRCC")

# 🏫 Program 3: Check Home Loan Eligibility Using Nested If

civil_score = int(input("Hi, Ravi! Please enter your civil score: "))
income = int(input("Hi, Ravi! Enter your income: "))

if civil_score > 750:
    if income > 350000:
        print("Congrats, You can apply for a home loan from SBI Bank")
    else:
        print("Sorry, your income is too low for loan approval")
else:
    print("According to Bank policy, your account is not eligible for a loan")



# Notes
'''
✅ Today I learned:

-> How to check positive / negative / zero using if-elif-else
-> Comparing numbers using conditions (>, <, ==)
-> Finding the greatest number among two and three values
-> Creating a simple login system using if–else
-> Traffic light program using multiple elif
-> Concept of Nested If (if inside another if)
-> Using nested conditions to check:
    #  Voting eligibility
    #  DRCC loan eligibility
    # Home loan eligibility (civil score + income)'''