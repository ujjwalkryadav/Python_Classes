# ===============================
# Day 32 Practice
# Topic: Loop + Function Based Programs
# ===============================

# ---------- Program 1: Print Even Numbers from 10 to 100 ----------

for i in range(10, 101):
    if i % 2 == 0:
        print(i)


# ---------- Program 2: Print Even Numbers Using Function ----------

def print_even_number(start, end):
    for i in range(start, end):
        if i % 2 == 0:
            print(i)

print_even_number(10, 21)


# ---------- Program 3: Simple Sum Function ----------

def summ(a, b):
    print(a + b)

summ(99, 3)


# ---------- Program 4: Create a List Using Input Function ----------

my_listt = []

for i in range(5):
    elements = int(input("enter the elements: "))
    my_listt.append(elements)
    print(my_listt)


# ---------- Program 5: Store Friends Name Using Function ----------

def print_my_friends_name():
    my_friend_list = []

    for i in range(4):
        friends = input("enter your friends name: ")
        my_friend_list.append(friends)
        print(my_friend_list)

print_my_friends_name()


# ---------- Program 6: Average of Three Subjects (Without Function) ----------

maths_marks = int(input("enter the maths marks: "))
science_marks = int(input("enter the science marks: "))
english_marks = int(input("enter your english marks: "))

total = maths_marks + science_marks + english_marks
average = total / 3

print(average)


# ---------- Program 7: Average of Marks Using Function ----------

def find_average_of_all_subject_marks(number_of_sub):

    maths_marks = int(input("enter the maths marks: "))
    science_marks = int(input("enter the science marks: "))
    english_marks = int(input("enter your english marks: "))

    total = maths_marks + science_marks + english_marks
    average = total / number_of_sub

    print(average)

find_average_of_all_subject_marks(3)