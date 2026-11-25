
def calculate_interest(p, r, t):
    simple_interest = (p * r * t) / 100

    compound_amount = p * (1 + r / 100) ** t
    compound_interest = compound_amount - p

    return simple_interest, compound_interest


p = 10000
r = 10
t = 2

si, ci = calculate_interest(p, r, t)

print("Simple Interest:", si)
print("Compound Interest:", ci)
