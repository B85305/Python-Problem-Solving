
income = 750000

if income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 0.05
elif income <= 900000:
    tax = (300000 * 0.05) + (income - 600000) * 0.10
else:
    tax = (300000 * 0.05) + (300000 * 0.10) + (income - 900000) * 0.15

print("Income:", income)
print("Income Tax:", tax)
