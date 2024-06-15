# account.py
class Account:
    def __init__(self, balance):
        self._balance = float(balance)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            return "Insufficient balance"
        else:
            self._balance -= amount
            return self._balance

    def get_balance(self):
        return self._balance

    def get_interest_rate(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_overdraft_limit(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        self._interest_rate = 0.01
        self._overdraft_limit = 0.0

    def get_interest_rate(self):
        return self._interest_rate

    def get_overdraft_limit(self):
        return self._overdraft_limit


class CurrentAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        self._interest_rate = 0.0
        self._overdraft_limit = 1000.0

    def get_interest_rate(self):
        return self._interest_rate

    def get_overdraft_limit(self):
        return self._overdraft_limit


class BusinessAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        self._interest_rate = 0.02
        self._overdraft_limit = 5000.0

    def get_interest_rate(self):
        return self._interest_rate

    def get_overdraft_limit(self):
        return self._overdraft_limit
