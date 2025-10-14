# STRING METHODS

name = "ujjwal yadav"
name2 = "           ujjwal yadav    "
name3 = "Ujjjwal ////"
name4 = "Raushan See Balloon"

print(name.upper())  # Out = UJJWAL YADAV
print(name.lower()) # Out = ujjwal yadav
print(name2.strip()) # Out = ujjwal yadav.  removve white spaces
print(name3.rstrip("/")) # Out = Ujjjwal      [remove "////"]
print(name4.replace("Ball", "M")) 
print(name4.split())
print(name.capitalize())
print(name.center(100))
print(name.center(50,"."))
print(len(name.center(50,".")))

name5 = "Ajit Is My Fraiend And Ajit Play Cricket"
print(name5.count(""))
print(name5.count("Ajit"))





