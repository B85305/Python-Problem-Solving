
numbers = [1, 2, 3, 4, 5]
k = 2

if numbers:
    k = k % len(numbers)
    result = numbers[k:] + numbers[:k]
else:
    result = []

print("Rotated List:", result)
