

#program 1 (Input) ---------------
a = input()
b = input()

print( a + b)
#program end ---------------


#program 2 (Input) ---------------
first_name = input( "Enter Your First Name")
second_name = input( "Enter Your Second Name")

print( first_name,second_name )
#program end ---------------





'''Task:
Test all Arithmetic Operators in Python by taking values from the user.
Check what happens when inputs are strings, and what happens when they are converted to integers.
Print the results directly without using any extra validation.'''

#program 3 (Take user input and test all arithmetic operators as string and as integer to compare outputs.) ---------------
a = input ("First Number" )
b = input ("Second Number")
print(a + b)
print(int (a) + int (b)) 

# print( a - b) error because we can,t minus string
print(int (a) - int (b)) 

# print( a * b) error because we can,t Multiply string
print(int (a) * int (b)) 

# print( a / b) error because we can,t divide string
print(int (a) / int (b)) 
print(int (a) // int (b)) 
print(int (a) % int (b)) 

# print( a ** b) error because we can,t multiply string
print(int (a) ** int (b)) 
#program End ---------------


#Summary Of Day 9
# Learn about input function
# and complete task
