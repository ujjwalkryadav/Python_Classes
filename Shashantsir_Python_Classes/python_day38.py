# -------------------------------
# Types of Inheritance in Python
# -------------------------------

# Python supports:
# Single, Multiple, Multilevel, Hierarchical, Hybrid inheritance


# ---------- Single Inheritance ----------

class Grandfather:
    grendfather_Assets = "Grand Complex"

class Father(Grandfather):
    father_Assets = "Father Complex"

father_obj = Father()
print(father_obj.grendfather_Assets)
print(father_obj.father_Assets)


# ---------- Multiple Inheritance ----------

class Father:
    father_property = "House"

class Mother:
    mother_property = "Jewellery"

class Child(Father, Mother):
    child_property = "Bike"

child_obj = Child()
print(child_obj.father_property)
print(child_obj.mother_property)
print(child_obj.child_property)


# ---------- Multilevel Inheritance ----------

class Grandfather:
    grendfather_Assets = "Grand Complex"

class Father(Grandfather):
    father_Assets = "Father Complex"

class Son(Father):
    son_Assents = "Son Complex"

class Grandson(Son):
    Grandson_Assets = "Grandson Complex"

grandson_obj = Grandson()
print(grandson_obj.grendfather_Assets)
print(grandson_obj.father_Assets)
print(grandson_obj.son_Assents)
print(grandson_obj.Grandson_Assets)


# ---------- Hierarchical Inheritance ----------

class Father:
    father_assets = "Bharat Petroleum"

class Child1(Father):
    child1_assets = "BMW"

class Child2(Father):
    child2_assets = "Fortuner"

child1_obj = Child1()
print(child1_obj.father_assets)
print(child1_obj.child1_assets)

child2_obj = Child2()
print(child2_obj.father_assets)
print(child2_obj.child2_assets)


# ---------- Hybrid Inheritance ----------

class Grandfather:
    grendfather_Assets = "Grand Complex"

class Father(Grandfather):
    father_Assets = "Father Complex"

class Son(Father):
    son_Assents = "Son Complex"

class Grandson(Grandfather, Father):
    Grandson_Assets = "Grandson Complex"

grandson_obj = Grandson()
print(grandson_obj.Grandson_Assets)
