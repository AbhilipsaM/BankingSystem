class Account:
    def __init__(self, account_number, customer, initial_balance=0.0):
        self.account_number = account_number
        self.customer = customer
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount > 0.0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> bool:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.balance
    

