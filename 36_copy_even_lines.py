
with open("source.txt", "r") as source:
    lines = source.readlines()

with open("destination.txt", "w") as destination:
    for number, line in enumerate(lines, start=1):
        if number % 2 == 0:
            destination.write(line)

print("Even-numbered lines copied successfully!")
