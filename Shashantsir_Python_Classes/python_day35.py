# -------------------------------
# OOPs Programming Revision
# -------------------------------

# ---------- Variable with Function (Normal Way) ----------

x = 10
print(x)

def print_my_name():
    print("this is Shashant")

print_my_name()


# ---------- Class Variable (Wrong Way) ----------

class Student:
    std_name = "Aditya"

# print(std_name)   # ERROR: class variable cannot be accessed directly


# ---------- Class Variable (Correct Way Using Object) ----------

class Student:
    std_name = "Aditya"

my_obj = Student()
print(my_obj.std_name)


# ---------- Class Method Without Object (Wrong) ----------

class Student:
    def student_info(self):
        print("here is all about student info")

# student_info()   # ERROR: method needs object


# ---------- Class Method With Object (Correct) ----------

class Student:
    def student_info(self):
        print("here is all about student info")

my_obj = Student()
my_obj.student_info()


# ---------- Another Class Example ----------

class Father:
    hotel = "Gupta Sweets"
    restaurant = "Veenu Restaurant"

my_obj = Father()
print(my_obj.restaurant)
print(my_obj.hotel)


# ---------- Private Variables in Class ----------

class Aakansha_Bank_details:
    bank_name = "SBI"
    account_no = 11111111
    __bank_balance = 99999   # private
    __atm_pin = 9898         # private

my_obj = Aakansha_Bank_details()
# print(my_obj.__atm_pin)   # ERROR: private variable


# ---------- Simple Class Example ----------

class Cricket:
    number_of_players = 11
    oneday_overs = 50
    t20_overs = 20


# ---------- Final Example Class ----------

class Aditya:
    hotel = "Gupta Sweets"

    def aditya_assets(self):
        print("aditya assets")

my_obj = Aditya()
print(my_obj.hotel)
my_obj.aditya_assets()

# print(hotel)   # ERROR: must use object or class name
