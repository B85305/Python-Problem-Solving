
def find_factors(n):
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors


num = 12

print("Factors:", find_factors(num))
