
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = list1.copy()

for item in list2:
    if item not in result:
        result.append(item)

print("Merged List:", result)
