def bal(balance):
    print(balance)

def credit(balance, value):
    transactions.append(value)
    balance += value
    return balance

def debit(balance, value):
    transactions.append(-value)  # record debit as a negative value
    balance -= value
    return balance

transactions = []

def last_transactions():
    print("Last 5 transactions:")
    for t in transactions[-5:]:
        if t < 0:
            print(f"Debited: {t}")
        else:
            print(f"Credited: {t}")

balance = 0
print("1. Credit")
print("2. Debit")
print("3. Show Balance")
print("4. Show Last 5 Transactions")
print("5. Exit")

while True:
    try:
        a = int(input("Enter the option: "))
        if a == 1:
            x = int(input("ENTER THE AMOUNT TO BE CREDITED: "))
            balance = credit(balance, x)
            print("Balance is ", end="")
            bal(balance)
        elif a == 2:
            y = int(input("ENTER THE AMOUNT TO BE DEBITED: "))
            balance = debit(balance, y)
            print("Balance is ", end="")
            bal(balance)
        elif a == 3:
            print("Balance is ", end="")
            bal(balance)
        elif a == 4:
            last_transactions()
        elif a == 5:
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 5.")
    except ValueError:
        print("Please enter a valid number.")