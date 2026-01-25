# -------------------------------
# Inheritance in Python
# -------------------------------

# Inheritance means child class inherits properties of parent class
# It helps in code reusability and avoids duplication


# ---------- Before Inheritance (Problem Case) ----------

class Father:
    father_property = "Bhardwaj Empire"

class Son:
    son_property = "Mohit Pan Dukan"

son_obj = Son()
print(son_obj.son_property)
# print(son_obj.father_property)   # ERROR: Son does not inherit Father


# ---------- Single Inheritance (Correct Way) ----------

class Father:
    father_property = "Bhardwaj Empire"

class Son(Father):
    son_property = "Mohit Pan Dukan"

son_obj = Son()
print(son_obj.son_property)
print(son_obj.father_property)


# ---------- Another Simple Inheritance Example ----------

class Company:
    cmp_name = "TCS"
    number_of_emp = 600

    def comp_info(self):
        print("It's all about this company")

my_obj = Company()
print(my_obj.cmp_name)
my_obj.comp_info()


# ---------- Class Without Object (Wrong) ----------

class Virat_Kohli:
    jersey_no = 18
    bat_brand = "MRF"

# print(jersey_no)   # ERROR: must use object or class name


# ---------- Class With Object (Correct) ----------

class Virat_Kohli:
    jersey_no = 18
    bat_brand = "MRF"

virat_obj = Virat_Kohli()
print(virat_obj.jersey_no)
