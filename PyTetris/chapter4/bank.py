class Account: # Account = 口座
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance # balance = 残高

    def deposit(self, amount): # deposit = 預ける
        self.balance += amount

    def withdraw(self, amount): # withdraw = 引き出す
        if amount > self.balance:
            print("残高が足りません")
            return
        self.balance -= amount # amount = 金額

    def show(self):
        print(f"{self.name}: {self.balance}")

account1 = Account("Alice", 100)
account2 = Account("Bob", 50)

while True:
    user_name = input("名前をどうぞ: ")
    command = input("+ or -: ")
    amount = int(input("いくらにしますか: "))
    if user_name == account1.name:
        if command == "+":
            account1.deposit(amount)
        elif command == "-":
            account1.withdraw(amount)
    elif user_name == account2.name:
        if command == "+":
            account2.deposit(amount)
        elif command == "-":
            account2.withdraw(amount)
    account1.show()
    account2.show()