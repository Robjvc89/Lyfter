
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}.")
        else:
            print("Insufficient funds.")


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        """Withdraw money from the savings account considering the minimum balance."""
        if self.balance - amount >= self.min_balance:
            super().withdraw(amount)
        else:
            print(f"Error: Cannot withdraw. Minimum balance of ${self.min_balance} must be maintained.")

# Example 
account = SavingsAccount(balance=1000, min_balance=200)
account.deposit(500)
account.withdraw(1200)  # Should succeed
account.withdraw(1500)  # Should fail 
