
def second_largest(numbers):
    unique_numbers = sorted(set(numbers))

    if len(unique_numbers) < 2:
        return "Second largest does not exist"

    return unique_numbers[-2]


my_list = [10, 20, 40, 30, 40, 20]

print("Second Largest:", second_largest(my_list))
