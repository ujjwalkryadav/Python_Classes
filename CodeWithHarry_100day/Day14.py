# Today I Learn and know about  If, Elif, Else Keywords..
# age = int(input ("Enter Your age"))
# print("Your Age Is =",age)

# if(age > 18):
#     print("You Can Drive")

# elif(age == 18):
#     print( "Must Be 18+ for diving licacnce")
     
# else:
#     print("No! You Can't Drive")

# With the help of [If], [elif], [else] I Make A my First Assistant "Dl Chat Bot"

print("Hi, I am 'DL-Bot'. Do you want to make a driving license?")
Decision1 = input("Y for Yes and N for No:-> ")


if( Decision1 == "y" or Decision1 == "Y" ):
   age =int(input ("Enter Your Age"))
   if age >= 18:
        print("You are eligible for a driving license!")
        Decision2 = input("Are you want to apply ''driving license'' ")
        if( Decision2 == "y" or Decision2 == "Y" ):
            print("Go to 'parivahan.gov.in' Portal ")
        if( Decision2 == "n" or Decision2 == "N" ):
            print("Ok But, you are eligible. You can aaply in future")
            print("Thank You")
   else:
        print("You are not eligible. You must be at least 18 years old.")

elif Decision1 == "n" or Decision1 == "N":
    print('Soory, we are only here for "diving Lincance reletted services"')

else:
    print("Invalid input! Please enter Y or N.")



