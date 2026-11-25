
numbers = [10, 20, 30, 40, 50, 10]

unique_numbers = sorted(set(numbers))

if len(unique_numbers) >= 2:
    print("Second Smallest:", unique_numbers[1])
    print("Second Largest:", unique_numbers[-2])
else:
    print("Not enough distinct elements")
