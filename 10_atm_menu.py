
balance = 5000

print("1. Withdraw")
print("2. Deposit")
print("3. Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter withdrawal amount: "))
    if 0 < amount <= balance:
        balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Invalid amount or insufficient balance")

elif choice == 2:
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print("Deposit successful")
        print("Updated balance:", balance)
    else:
        print("Invalid amount")

elif choice == 3:
    print("Available balance:", balance)

else:
    print("Invalid choice")
