
class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self._balance = float(balance)

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance + self.get_overdraft_limit() >= amount:
            self._balance -= amount
        else:
            print("Withdrawal amount exceeds balance and overdraft limit")

    def get_interest_rate(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_overdraft_limit(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_account_no(self):
        return self.account_no

    def get_account_type(self):

        raise NotImplementedError("This method should be overridden by subclasses")

    # def get_account_by_no(self, account_no):
    #         for account in self.accounts:
    #             if account.get_account_no() == account_no:
    #                 return account
    #         return None


class SavingsAccount(Account):
    def __init__(self, account_no, balance):
        super().__init__(account_no, balance)
        self._interest_rate = 0.01
        self._overdraft_limit = 0.0

    def get_interest_rate(self):
        return self._interest_rate

    def get_overdraft_limit(self):
        return self._overdraft_limit
    def get_account_type(self):

        return "Savings"    


class CurrentAccount(Account):
    def __init__(self, account_no, balance):
        super().__init__(account_no, balance)
        self._interest_rate = 0.0
        self._overdraft_limit = 1000.0

    def get_interest_rate(self):
        return self._interest_rate

    def get_overdraft_limit(self):
        return self._overdraft_limit

    def get_account_type(self):
        return "Current"


class BusinessAccount(Account):
    def __init__(self, account_no, balance):
        super().__init__(account_no, balance)
        self._interest_rate = 0.02
        self._overdraft_limit = 5000.0

    def get_interest_rate(self):
        return self._interest_rate

    def get_overdraft_limit(self):
        return self._overdraft_limit
    def get_account_type(self):

        return "Business"
