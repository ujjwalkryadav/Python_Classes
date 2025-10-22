# 🗓️ DAY 12 NOTES
# Topic: String Indexing, Negative Indexing, and Slicing


# 1️⃣ String and Indexing (Positive & Negative)
language = "Programming"

# Positive Indexing
#  P   r   o   g   r   a   m   m   i   n   g
#  0   1   2   3   4   5   6   7   8   9   10

# Negative Indexing
#  P     r     o     g     r     a     m     m     i     n     g
# -11  -10   -9    -8    -7    -6    -5    -4    -3    -2    -1

#program END ---------------


# 2️⃣ Basic Slicing (Two Parameters)
# Syntax: string[start:end]
# Note: End index is excluded.

language = "Programming"
print(language[0:8])    # Output: "Programm"
print(language[2:9])    # Output: "ogrammi"
print(language[0:])     # Output: "Programming"
print(language[:])      # Output: "Programming"
print(language[4:-1])   # Output: "rammin"
print(language[-8:])    # Output: "ogramming"
#program END ---------------


# 3️⃣ Slicing with Three Parameters (start:end:gap)
# Syntax: string[start:end:gap]
# Default gap = 1

language = "Programming"
print("With gap the output is:", language[0:7:1])
print("Without gap the output is:", language[0:7])
# Both outputs are same: "Program"
#program END ---------------


# 4️⃣ Example with Custom Step (Gap)
language2 = "javascript"
#  j  a  v  a  s  c  r  i  p  t
#  0  1  2  3  4  5  6  7  8  9
print(language2[0:9:2])   # Output: "jvsrp"
print(language2[0:11:2])  # Output: "jvsrp"
#program END ---------------


# 5️⃣ Practice Examples
language = "Programming"
print(language)          # Programming
print(language[9])       # n
print(language[8])       # i
print(language[-2])      # n
print(language[-6])      # a
print(language[0:8])     # Programm
print(language[2:9])     # ogrammi
print(language[0:])      # Programming
print(language[:])       # Programming
print(language[4:-1])    # rammin
print(language[-8:])     # ogramming
print("With gap:", language[0:7:1])
print("Without gap:", language[0:7])
#program END ---------------


'''
🧾 DAY 12 SUMMARY

✅ Today I practiced:
- Positive & Negative String Indexing.
- String Slicing (start:end).
- String Slicing with step (start:end:gap).
- How slicing excludes the ending index.
- Using default start, end, and step values.

💡 Main Concept:
String slicing allows us to extract a specific portion (substring) from a larger string.
Default behavior:
  start → 0
  end → last index
  step → 1
'''
