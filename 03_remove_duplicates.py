
my_list = [10, "Python", 20, 10, "Java", True, 20, "Python"]

result = []

for item in my_list:
    if item not in result:
        result.append(item)

print(result)
