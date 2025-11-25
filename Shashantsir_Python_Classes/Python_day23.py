# 🗓️ DAY 23 NOTES
# Topic: WHILE LOOP + INCREMENT CONCEPT


# PROGRAM 1 — Basic While Loop
i = 0  # initialization

while (i < 5):  # condition check
    print(i)     # task
    i += 1       # increment


# PROGRAM 2 — Python Increment Rule
# Python does NOT support i++ or ++i
# Must use: i = i + 1 or i += 1

i = 0
while (i < 3):
    print(i)
    i = i + 1


# PROGRAM 3 — Step-by-Step While Loop Working
# (Phase-based execution explained in theory)
i = 0
while (i < 5):
    print(i)
    i += 1


# PROGRAM 4 — While Loop From 1 to 6
# Simple increment-based loop
i = 1
while(i < 7):
    print(i)
    i = i + 1


# PROGRAM 5 — Even–Odd Check
# Checks if a number is even or odd
a = 15
if(a % 2 == 0):
    print("Even Num =", a)
else:
    print("Odd Number =", a)


# PROGRAM 6 — Print Even Numbers From 1 to 99
i = 1
while(i < 100):
    if(i % 2 == 0):
        print(i)
    i = i + 1


# PROGRAM 7 — Even Numbers Starting From User Input
i = int(input("Hii Ujjwal Enter Value Of i = "))
while(i < 100):
    if(i % 2 == 0):
        print(i)
    i = i + 1


# PROGRAM 8 — Even Numbers Between Start & End Points
# User selects range
start = int(input("Hii Ujjwal Enter Value Of Starting Point = "))
end = int(input("Enter The Value Of Ending Point = "))

while(start < end):
    if(start % 2 == 0):
        print(start)
    start = start + 1


"""
# 🧾 DAY 23 SUMMARY ->
-> while loop uses initialization → condition → task → increment.
-> Python does NOT allow i++ or ++i.
-> Must use i = i + 1 OR i += 1.
-> while loop runs until condition becomes FALSE.
-> Even/odd checking uses: number % 2.
-> User-defined ranges can be looped using while.
"""