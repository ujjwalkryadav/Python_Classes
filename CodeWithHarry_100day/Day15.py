# Print Time Using Datetime Module

#program 1 (METHOD 1 TO GET TIME) ---------------
from datetime import datetime
import time
current_hour =  datetime.now().hour
current_hour2 = datetime.now().minute
current_hour3 = datetime.now().second
print("Current Time:", current_hour ,"Hours" , current_hour2,"Minutes", current_hour3,"Seconds")
#--------------END------------------------------




#program 2 (METHOD 2 TO GET TIME) ---------------
Time =(time.strftime('%M:%H:S'))
print(current_hour)
#--------------END------------------------------



# Mini Project: Greeting Based on Time
#program 3 (METHOD 2 TO GET TIME) ---------------
Time2 =int((time.strftime('%M')))

if 5< Time2 < 12:
    print("Good Morning")
elif 12 <= Time2 < 18:
    print("Good Afternoon") 
elif 18 <= Time2 < 20:
    print("Good Evening")
else:
    print("Good Night")

#--------------END------------------------------


# Summery
'''
Today I learned how to get the current time in Python using datetime and time modules.
I understood how to extract hours, minutes, and seconds using strftime and datetime.now().
I learned to use type conversion (int()) to convert strings into numbers.
I practiced using if-elif-else to print greetings based on the time.
Mini project application: generating and printing time-based greetings.
'''