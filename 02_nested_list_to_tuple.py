
my_list = [[1, 2], [3, 4], [5, 6]]

result = tuple(tuple(item) for item in my_list)

print(result)
print(type(result))
