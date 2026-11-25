
my_tuple = (1, 2, 3, 2, 1, 4, 2, 3)

frequency = {}

for item in my_tuple:
    frequency[item] = frequency.get(item, 0) + 1

print("Frequency:", frequency)
