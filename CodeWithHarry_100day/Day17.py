# Day17 For Loops
for i in range(5):
 print(i)


name = "Ujjwal"
for i in name:
    print(i)

name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")

for k in range(1, 20001):
  print(k)

Fruits = "Apple"
for i in Fruits:
    print(i)

Fruits = ["Apple", "Mango", "Bananna"]
for i in Fruits:
    print(i)

for k in range(1, 12, 3): #third parameter is space.
  print(k)

# Play With For Loop
# ✅ Task 1: Print all the numbers from 1 to 100

for i in range (1, 101):
  print(i)

# ✅ Task 2: Print only even numbers (1–50)

for i in range(2, 51 ,2):
    print(i)

# ✅ TASK 3: Print Any number table

for table in range(5, 51, 5): 
    print(table)

# ✅ TASK 4: List sum
list = [3, 6, 2, 9, 4]
total = 0

for num in list:
    total += num
print("Total Sum =", total)

#  ✅ TASK 5: Print 20 to 1 reverse counting
for i in range(20, 0, -1):
     print(i, end=",")









    


