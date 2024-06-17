from account import Account, SavingsAccount, CurrentAccount, BusinessAccount
from person import Person

# class CustomerAccount(Person):
#     def __init__(self, fname, lname, address, accounts):
#         super().__init__(fname, lname, address)
#         self.accounts = accounts
#
#     def get_accounts(self):
#         return self.accounts
#
#     def get_account_by_no(self, account_no):
#         for account in self.accounts:
#             if account.get_account_no() == account_no:
#                 return account
#         return None
#
#     def deposit(self, account_no, amount):
#         account = self.get_account_by_no(account_no)
#         if account:
#             account.deposit(amount)
#             print(f"Deposit successful. New balance for account {account_no}: {account.get_balance()}")
#         else:
#             print("Account not found.")
#
#     def withdraw(self, account_no, amount):
#         account = self.get_account_by_no(account_no)
#         if account:
#             if amount > (account.get_balance() + account.get_overdraft_limit()):
#                 print("Insufficient balance")
#             else:
#                 account.withdraw(amount)
#                 print(f"Withdrawal successful. New balance for account {account_no}: {account.get_balance()}")
#         else:
#             print("Account not found.")
#
#     def print_balance(self, account_no):
#         account = self.get_account_by_no(account_no)
#         if account:
#             print(f"The account balance for account {account_no} is {account.get_balance():.2f}")
#         else:
#             print("Account not found.")
#
#     def print_details(self):
#          print(f"Name: {self.get_first_name()} {self.get_last_name()}")
#          print(f"Address: {', '.join(self.get_address())}")
#          for account in self.accounts:
#              print(f"Account No: {account.account_no}")
#              if isinstance(account, SavingsAccount):
#                  print(f"Account Type: Savings Account")
#                  print(f"Balance: {account.get_balance():.2f}")
#                  print(f"Interest Rate: {account.get_interest_rate()}")
#                  print(f"Overdraft Limit: {account.get_overdraft_limit()}")
#              elif isinstance(account, CurrentAccount):
#                  print(f"Account Type: Current Account")
#                  print(f"Balance: {account.get_balance():.2f}")  # Adjust based on actual method in CurrentAccount
#                  print(f"Interest Rate: {account.get_interest_rate()}")
#                  print(f"Overdraft Limit: {account.get_overdraft_limit()}")
#              elif isinstance(account, BusinessAccount):
#                  print(f"Account Type: Business Account")
#                  print(f"Balance: {account.get_balance():.2f}")  # Adjust based on actual method in BusinessAccount
#                  print(f"Interest Rate: {account.get_interest_rate()}")
#                  print(f"Overdraft Limit: {account.get_overdraft_limit()}")
#              else:
#                  print(f"Account Type: Unknown")
#
#     def account_menu(self):
#         print("1) Deposit money")
#         print("\nYour Transaction Options Are:")
#         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         print("2) Withdraw money")
#         print("3) Check balance")
#         print("4) Update customer name")
#         print("5) Update customer address")
#         print("6) Show customer details")
#         print("7) Deposit money")
#         print("8) Back")
#         print(" ")
#         option = input("Choose your option: ")
#         try:
#             return int(option)
#         except ValueError:
#             print("Invalid input, please enter a number.")
#             return -1
#
#     def run_account_options(self):
#         loop = 1
#         while loop == 1:
#             choice = self.account_menu()
#             if choice == 1:
#                 account_no = input("Enter account number to deposit into: ")
#                 amount = input("Enter amount to deposit: ")
#                 try:
#                     account_no = int(account_no)
#                     amount = float(amount)
#                     self.deposit(account_no, amount)
#                 except ValueError:
#                     print("Invalid account number or amount.")
#             elif choice == 2:
#                 account_no = input("Enter account number to withdraw from: ")
#                 amount = input("Enter amount to withdraw: ")
#                 try:
#                     account_no = int(account_no)
#                     amount = float(amount)
#                     self.withdraw(account_no, amount)
#                 except ValueError:
#                     print("Invalid account number or amount.")
#             elif choice == 3:
#                 account_no = input("Enter account number to check balance: ")
#                 try:
#                     account_no = int(account_no)
#                     self.print_balance(account_no)
#                 except ValueError:
#                     print("Invalid account number.")
#             elif choice == 4:
#                 fname = input("Enter new first name: ")
#                 lname = input("Enter new last name: ")
#                 self.update_first_name(fname)
#                 self.update_last_name(lname)
#             elif choice == 5:
#                 addr = input("Enter new address (comma separated): ").split(",")
#                 self.update_address(addr)
#             elif choice == 6:
#                 self.print_details()
#             elif choice == 7:
#                 loop = 0
#             else:
#                 print("Invalid option, please try again.")
#         print("\nExit account operations")



# class CustomerAccount(Person):
#     def __init__(self, fname, lname, address, accounts):
#         super().__init__(fname, lname, address)
#         self.accounts = accounts
#
#     def get_accounts(self):
#         return self.accounts
#
#     def get_account_by_no(self, account_no):
#         for account in self.accounts:
#             if account.get_account_no() == account_no:
#                 return account
#         return None
#
#     def get_balance(self, account_no):
#         account = self.get_account_by_no(account_no)
#         if account:
#             return account.get_balance()
#         return None
#
#     def deposit(self, account_no, amount):
#         account = self.get_account_by_no(account_no)
#         if account:
#             account.deposit(amount)
#             print(f"Deposit successful. New balance for account {account_no}: {account.get_balance()}")
#         else:
#             print("Account not found.")
#
#     def withdraw(self, account_no, amount):
#         account = self.get_account_by_no(account_no)
#         if account:
#             if amount > (account.get_balance() + account.get_overdraft_limit()):
#                 print("Insufficient balance")
#             else:
#                 account.withdraw(amount)
#                 print(f"Withdrawal successful. New balance for account {account_no}: {account.get_balance()}")
#         else:
#             print("Account not found.")
#
#     def print_balance(self, account_no):
#         account = self.get_account_by_no(account_no)
#         if account:
#             print(f"The account balance for account {account_no} is {account.get_balance():.2f}")
#         else:
#             print("Account not found.")
#
#     def print_details(self):
#         print(f"Name: {self.get_first_name()} {self.get_last_name()}")
#         print(f"Address: {', '.join(self.get_address())}")
#         for account in self.accounts:
#             print(f"Account No: {account.get_account_no()}")
#             if isinstance(account, SavingsAccount):
#                 print(f"Account Type: Savings Account")
#             elif isinstance(account, CurrentAccount):
#                 print(f"Account Type: Current Account")
#             elif isinstance(account, BusinessAccount):
#                 print(f"Account Type: Business Account")
#             else:
#                 print(f"Account Type: Unknown")
#             print(f"Balance: {account.get_balance():.2f}")
#             print(f"Interest Rate: {account.get_interest_rate()}")
#             print(f"Overdraft Limit: {account.get_overdraft_limit()}")
#
#     def account_menu(self):
#         print("\nYour Transaction Options Are:")
#         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         print("1) Deposit money")
#         print("2) Withdraw money")
#         print("3) Check balance")
#         print("4) Update customer name")
#         print("5) Update customer address")
#         print("6) Show customer details")
#         print("7) Back")
#         print(" ")
#         option = input("Choose your option: ")
#         try:
#             return int(option)
#         except ValueError:
#             print("Invalid input, please enter a number.")
#             return -1
#
#     def run_account_options(self):
#         loop = 1
#         while loop == 1:
#             choice = self.account_menu()
#             if choice == 1:
#                 account_no = input("Enter account number to deposit into: ")
#                 amount = input("Enter amount to deposit: ")
#                 try:
#                     account_no = int(account_no)
#                     amount = float(amount)
#                     self.deposit(account_no, amount)
#                 except ValueError:
#                     print("Invalid account number or amount.")
#             elif choice == 2:
#                 account_no = input("Enter account number to withdraw from: ")
#                 amount = input("Enter amount to withdraw: ")
#                 try:
#                     account_no = int(account_no)
#                     amount = float(amount)
#                     self.withdraw(account_no, amount)
#                 except ValueError:
#                     print("Invalid account number or amount.")
#             elif choice == 3:
#                 account_no = input("Enter account number to check balance: ")
#                 try:
#                     account_no = int(account_no)
#                     self.print_balance(account_no)
#                 except ValueError:
#                     print("Invalid account number.")
#             elif choice == 4:
#                 fname = input("Enter new first name: ")
#                 lname = input("Enter new last name: ")
#                 self.update_first_name(fname)
#                 self.update_last_name(lname)
#             elif choice == 5:
#                 addr = input("Enter new address (comma separated): ").split(",")
#                 self.update_address(addr)
#             elif choice == 6:
#                 self.print_details()
#             elif choice == 7:
#                 loop = 0
#             else:
#                 print("Invalid option, please try again.")
#         print("\nExit account operations")


class CustomerAccount(Person):
    def __init__(self, fname, lname, address, accounts):
        super().__init__(fname, lname, address)
        self.accounts = accounts

    def get_accounts(self):
        return self.accounts

    def get_account_by_no(self, account_no):
        for account in self.accounts:
            if account.get_account_no() == account_no:
                return account
        return None

    def get_balance(self, account_no):
        account = self.get_account_by_no(account_no)
        if account:
            return account.get_balance()
        return None

    def deposit(self, account_no, amount):
        account = self.get_account_by_no(account_no)
        if account:
            account.deposit(amount)
            print(f"Deposit successful. New balance for account {account_no}: {account.get_balance()}")
        else:
            print("Account not found.")

    def withdraw(self, account_no, amount):
        account = self.get_account_by_no(account_no)
        if account:
            if amount > (account.get_balance() + account.get_overdraft_limit()):
                print("Insufficient balance")
            else:
                account.withdraw(amount)
                print(f"Withdrawal successful. New balance for account {account_no}: {account.get_balance()}")
        else:
            print("Account not found.")

    def print_balance(self, account_no):
        account = self.get_account_by_no(account_no)
        if account:
            print(f"The account balance for account {account_no} is {account.get_balance():.2f}")
        else:
            print("Account not found.")

    def print_details(self):
        print(f"Name: {self.get_first_name()} {self.get_last_name()}")
        print(f"Address: {', '.join(self.get_address())}")
        for account in self.accounts:
            print(f"Account No: {account.get_account_no()}")
            if isinstance(account, SavingsAccount):
                print(f"Account Type: Savings Account")
            elif isinstance(account, CurrentAccount):
                print(f"Account Type: Current Account")
            elif isinstance(account, BusinessAccount):
                print(f"Account Type: Business Account")
            else:
                print(f"Account Type: Unknown")
            print(f"Balance: {account.get_balance():.2f}")
            print(f"Interest Rate: {account.get_interest_rate()}")
            print(f"Overdraft Limit: {account.get_overdraft_limit()}")

    def account_menu(self):
        print("\nYour Transaction Options Are:")
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
                account_no = input("Enter account number to deposit into: ")
                try:
                    account_no = int(account_no)
                    account = self.get_account_by_no(account_no)
                    if account:
                        print(f"Account Type: {self.get_account_type(account)}")
                        amount = input("Enter amount to deposit: ")
                        try:
                            amount = int(amount)
                            if amount > 0:
                                self.deposit(account_no, amount)
                            else:
                                print("Please enter a positive amount.")
                        except ValueError:
                            print("Invalid amount. Please enter a positive integer.")
                    else:
                        print("Account not found.")
                except ValueError:
                    print("Invalid account number.")
            elif choice == 2:
                account_no = input("Enter account number to withdraw from: ")
                try:
                    account_no = int(account_no)
                    account = self.get_account_by_no(account_no)
                    if account:
                        print(f"Account Type: {self.get_account_type(account)}")
                        amount = input("Enter amount to withdraw: ")
                        try:
                            amount = int(amount)
                            if amount > 0:
                                self.withdraw(account_no, amount)
                            else:
                                print("Please enter a positive amount.")
                        except ValueError:
                            print("Invalid amount. Please enter a positive integer.")
                    else:
                        print("Account not found.")
                except ValueError:
                    print("Invalid account number.")
            elif choice == 3:
                account_no = input("Enter account number to check balance: ")
                try:
                    account_no = int(account_no)
                    self.print_balance(account_no)
                except ValueError:
                    print("Invalid account number.")
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
        print("\nExit account operations")

    def get_account_type(self, account):
        if isinstance(account, SavingsAccount):
            return "Savings Account"
        elif isinstance(account, CurrentAccount):
            return "Current Account"
        elif isinstance(account, BusinessAccount):
            return "Business Account"
        else:
            return "Unknown"
