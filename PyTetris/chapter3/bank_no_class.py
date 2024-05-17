account1_name = "Alice"
account1_balance = 100

account2_name = "Bob"
account2_balance = 50

while True:
    user_name = input("名前をどうぞ: ")
    command = input("+ or -: ")
    amount = int(input("いくらにしますか: "))
    if user_name == account1_name:
        if command == "+":
            account1_balance += amount
        elif command == "-":
            if account1_balance < amount:
                print("残高が足りません")
                continue
            account1_balance -= amount
    elif user_name == account2_name:
        if command == "+":
            account2_balance += amount
        elif command == "-":
            if account2_balance < amount:
                print("残高が足りません")
                continue
            account2_balance -= amount
    print(f"{account1_name}: {account1_balance}")
    print(f"{account2_name}: {account2_balance}")
