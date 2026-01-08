# ===============================
# Day 27 Practice
# Topic: Dictionary Methods
# ===============================

# ---------- Accessing List inside Dictionary ----------

my_dict = {
    "name": ["Ujwal", "Ravi", "Rahul"],
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(my_dict["name"])
print(my_dict["name"][1])   # Ravi


# ---------- Dictionary Method: keys() ----------

my_dict = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(my_dict)
print(my_dict.keys())


# ---------- Dictionary Method: values() ----------

diwakar_dictionary = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(diwakar_dictionary)
print(diwakar_dictionary.values())


# ---------- Dictionary Method: items() ----------

diwakar_dictionary = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(diwakar_dictionary)
print(diwakar_dictionary.items())

# using value method on dictionary value
print(diwakar_dictionary["city"].upper())


# ---------- Dictionary Method: get() ----------

diwakar_dictionary = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(diwakar_dictionary.get("name"))


# ---------- Dictionary Method: update() ----------

diwakar_dictionary = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

diwakar_dictionary.update({"roll_no": 251})
print(diwakar_dictionary)


# ---------- Dictionary Method: pop() ----------

diwakar_dictionary = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

diwakar_dictionary.pop("age")
print(diwakar_dictionary)