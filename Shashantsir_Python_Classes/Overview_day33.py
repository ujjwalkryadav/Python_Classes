# ===============================
# Day 33 Practice
# Topic: Nested Loop
# ===============================

# A nested loop means a loop inside another loop
# Outer loop runs first
# Inner loop runs completely for each iteration of outer loop


# ---------- Example 1: Simple Nested Loop ----------

for i in range(0, 2):
    for i in range(0, 1):
        print("the value of i :", i)


# ---------- Example 2: Normal For Loop ----------

for i in range(0, 4):
    print(i)
    print("Shivam")


# ---------- How For Loop Works (Basic Example) ----------

for i in range(0, 4):
    print(i)


# ---------- Example 3: Nested Loop with i and j ----------

for i in range(0, 2):
    for j in range(0, 5):
        print("the value of i :", i, "the value of j", j)


# ---------- Example 4: Nested Loop Output Style ----------

for i in range(0, 2):
    for j in range(0, 1):
        print("the value of i :", i, "the value of j :", j)


# ---------- Example 5: Simple Loop (No Nesting) ----------

for i in range(0, 3):
    print("Nisha")
    print("this is normal for loop")


# ---------- Correct Nested Loop Example (Recommended) ----------

for i in range(0, 2):
    for j in range(0, 1):
        print("the value of i :", i, "the value of j", j)
