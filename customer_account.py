from account import Account, SavingsAccount, CurrentAccount, BusinessAccount
from person import Person

class CustomerAccount(Person):

    def __init__(self, fname, lname, address, account_no, balance, account_type):
        self._fname = fname
        self._lname = lname
        self._address = address
        self._account_no = account_no
        if account_type == "savings":
            self._account = SavingsAccount(balance)
        elif account_type == "current":
            self._account = CurrentAccount(balance)
        elif account_type == "business":
            self._account = BusinessAccount(balance)
        else:
            raise ValueError("Invalid account type")
        self._account_type = account_type

    def deposit(self, amount):
        # self._balance += amount
        self._account.deposit(amount)

    def withdraw(self, amount):
        if amount > self._account.get_balance():
            print("Insufficient balance")
        else:
            self._account.withdraw(amount)
            return self._account.get_balance()

    def get_account_type(self):
        return self._account_type

    def get_interest_rate(self):
        # return self._account.get_interest_rate
        return self._account.get_interest_rate()

    def get_overdraft_limit(self):
        return self._account.get_overdraft_limit()

    def print_balance(self):
        print("\n The account balance is %.2f" % self._account.get_balance())

    def get_balance(self):
        return self._account.get_balance()

    def get_account_no(self):
        return self._account_no

    def print_details(self):
        print(f"Name: {self._fname} {self._lname}")
        print(f"Address: {', '.join(self._address)}")
        print(f"Account No: {self._account_no}")
        print(f"Account Type: {self._account_type}")
        print(f"Balance: {self._account.get_balance()}")
        print(f"Interest Rate: {self._account.get_interest_rate()}")
        print(f"Overdraft Limit: {self.get_overdraft_limit()}")

    def account_menu(self):
        print("\n Your Transaction Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Deposit money")
        print("2) Withdraw money")
        print("3) Check balance")
        print("4) Update customer name")
        print("5) Update customer address")
        print("6) Show customer details")
        print("7) Back")
        print(" ")
        option = input("Choose your option: ")
        try:
            return int(option)
        except ValueError:
            print("Invalid input, please enter a number.")
            return -1

    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                amount = input("Enter amount to deposit: ")
                try:
                    amount = float(amount)
                    self.deposit(amount)
                except ValueError:
                    print("Invalid amount.")
            elif choice == 2:
                amount = input("Enter amount to withdraw: ")
                try:
                    amount = float(amount)
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid amount.")
            elif choice == 3:
                self.print_balance()
            elif choice == 4:
                fname = input("Enter new first name: ")
                lname = input("Enter new last name: ")
                self.update_first_name(fname)
                self.update_last_name(lname)
            elif choice == 5:
                addr = input("Enter new address (comma separated): ").split(",")
                self.update_address(addr)
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
            else:
                print("Invalid option, please try again.")
        print("\n Exit account operations")
