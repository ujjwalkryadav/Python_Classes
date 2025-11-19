# Today I Learn While loop
i = int(input("Enter the number: "))
print(i)
while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")


count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")



# Play With While Loops

# ✅ TASK 1: Create While Loop Based Password Checker
password = " "
while password != "123":
  password = input("Enter Your Password")
print("Login Succesfuly")


# ✅ TASK 2: Counting from 1 to 10 (while loop)
i = 1

while i <= 10:
    print(i, end=" ")
    i += 1

# ✅ TASK 3: Number Guessing Game

num = " "
while num != "5":
 num = input("Guess The Number")
 if(num != "5"):
      print("Sorry You are Wrong")

print("You Guss Right Number")

# ------------------------------------------------------------

# 🏧 ATM Machine Program (Using While Loop)
balance = 5000  # Starting balance
pin = "1234"

# Step 1: PIN Check
user_pin = input("Enter ATM PIN: ")

while user_pin != pin:
    print("Wrong PIN! Try again.")
    user_pin = input("Enter ATM PIN: ")

print("Login Successful!\n")

# Step 2: ATM Menu
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    # Option 1 → Balance
    if choice == "1":
        print("Your Balance:", balance)

    # Option 2 → Deposit
    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Amount Deposited Successfully!")
        print("Updated Balance:", balance)

    # Option 3 → Withdraw
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdraw Successful!")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance!")

    # Option 4 → Exit
    elif choice == "4":
        print("Thank You for using ATM 🙂")
        break

    else:
        print("Invalid Option! Please choose again.")



