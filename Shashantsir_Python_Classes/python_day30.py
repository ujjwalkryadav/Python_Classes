# ===============================
# Day 30 Practice
# Topic: For Loop, range(), break, continue
# ===============================

# ---------- For Loop with range() ----------

for i in range(5):
    print(i)


for i in range(0, 5):
    print(i)


# ---------- For Loop on List (Sequence) ----------

#              0       1       2   3   4
my_listt = ["Ravi", "rohit", 44, 55, 88]
print(my_listt)

for i in my_listt:
    print(i)


# ---------- break statement (range loop) ----------

for i in range(0, 12):
    if i == 7:
        break
    print(i)


# ---------- continue statement (range loop) ----------

for i in range(0, 12):
    if i == 7:
        continue
    print(i)


# ---------- break on list ----------

my_listt = ["Ravi", "rohit", 44, 55, 88]

for i in my_listt:
    if i == 44:
        break
    print(i)


# ---------- another break example ----------

my_listt = ["Ravi", "rohit", 101, 44, 55, 88]

for i in my_listt:
    if i == 101:
        break
    print(i)


# ---------- continue on list ----------

my_listt = ["Ravi", "rohit", 101, 44, 55, 88]

for i in my_listt:
    if i == 101:
        continue
    print(i)