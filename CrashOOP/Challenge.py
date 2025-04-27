class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}\n"

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted\n")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Accepted\n")
        else:
            print('Funds Unavailable!\n')


# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

