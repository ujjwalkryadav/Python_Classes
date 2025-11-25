# Sum of tuple elements using while loop
my_tuple = (3, 6, 9, 12)
i = 0
total = 0
while i < len(my_tuple):
 total += my_tuple[i]
 i += 1
print(total)