import json
from admin import Admin
from customer_account import CustomerAccount
from account import Account, SavingsAccount, CurrentAccount, BusinessAccount


class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()

    def load_bank_data(self):
        try:
            with open('customers.json', 'r') as file:
                customers_data = json.load(file)
                for data in customers_data:
                    customer = CustomerAccount(
                        data['fname'], data['lname'], data['address'], data['account_no'],
                        data['balance'], data['account_type']
                    )
                    self.accounts_list.append(customer)
        except FileNotFoundError:
            print("No customer data file found. Starting with empty data.")

        # Create admins (hard-coded for now)
        admins = [
            ("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True),
            ("Cathy", "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        ]

        for fname, lname, address, user_name, password, full_rights in admins:
            admin = Admin(fname, lname, address, user_name, password, full_rights)
            self.admins_list.append(admin)

    def save_bank_data(self):
        customers_data = [{
            'fname': customer.get_first_name(),
            'lname': customer.get_last_name(),
            'address': customer.get_address(),
            'account_no': customer.get_account_no(),
            'balance': customer.get_balance(),
            'account_type': customer.get_account_type()
        } for customer in self.accounts_list]

        with open('customers.json', 'w') as file:
            json.dump(customers_data, file)

    def search_admins_by_name(self, admin_username):
        for admin in self.admins_list:
            if admin.get_username() == admin_username:
                return admin
        return None

    def search_customers_by_name(self, customer_lname):
        for customer in self.accounts_list:
            if customer.get_last_name() == customer_lname:
                return customer
        return None

    def main_menu(self):
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to the Python Bank System")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Admin login")
        print("2) Quit Python Bank System")
        print(" ")
        option = input("Choose your option: ")
        try:
            return int(option)
        except ValueError:
            print("Invalid input, please enter a number.")
            return -1

    def run_main_options(self):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input("\n Please input admin username: ")
                password = input("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj is not None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
            elif choice == -1:
                continue
        print("\n Thank-You for stopping by the bank!")

    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        sender = self.search_customers_by_name(sender_lname)
        receiver = self.search_customers_by_name(receiver_lname)
        if sender and receiver and receiver.get_account_no() == int(receiver_account_no):
            if sender.get_balance() >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds in sender's account.")
        else:
            print("Invalid sender or receiver details.")

    def admin_login(self, username, password):
        admin = self.search_admins_by_name(username)
        if admin and admin.get_password() == password:
            return "Login successful", admin
        else:
            return "Invalid username or password", None

    def admin_menu(self, admin_obj):
        print(" ")
        print("Welcome Admin %s %s : Available options are:" % (admin_obj.get_first_name(), admin_obj.get_last_name()))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Transfer money")
        print("2) Customer account operations & profile settings")
        print("3) Delete customer")
        print("4) Print all customers detail")
        print("5) Print report")
        print("6) Sign out")
        print(" ")
        option = input("Choose your option: ")
        try:
            return int(option)
        except ValueError:
            print("Invalid input, please enter a number.")
            return -1

    def run_admin_options(self, admin_obj):
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")
                amount = input("\n Please input the amount to be transferred: ")
                try:
                    amount = float(amount)
                except ValueError:
                    print("Invalid amount.")
                    continue
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                try:
                    receiver_account_no = int(receiver_account_no)
                except ValueError:
                    print("Invalid account number.")
                    continue
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)
            elif choice == 2:
                customer_lname = input("\n Please input customer surname: ")
                customer = self.search_customers_by_name(customer_lname)
                if customer:
                    customer.run_account_options()
                else:
                    print("Customer not found.")
            elif choice == 3:
                customer_lname = input("\n Please input customer surname to delete: ")
                customer = self.search_customers_by_name(customer_lname)
                if customer:
                    self.accounts_list.remove(customer)
                    print("Customer account deleted.")
                else:
                    print("Customer not found.")
            elif choice == 4:
                self.print_all_accounts_details()
            elif choice == 5:
                loop = 0
                self.generate_management_report()
            elif choice == 6:
                loop = 0
            elif choice == -1:
                continue
        print("\n Exit account operations")

    def print_all_accounts_details(self):
        i = 0
        for c in self.accounts_list:
            i += 1
            print('\n %d. ' % i, end=' ')
            c.print_details()
            print("------------------------")

    # def generate_management_report(self):
    #     total_customers = len(self.accounts_list)
    #     total_balance = sum(customer.get_balance() for customer in self.accounts_list)
    #     total_interest = sum(customer.get_balance() * customer.get_interest_rate() for customer in self.accounts_list)
    #     total_overdrafts = sum(
    #         max(0, customer.get_balance() - customer.get_overdraft_limit())
    #         for customer in self.accounts_list
    #     )
    #
    #     report = {
    #         "total_customers": total_customers,
    #         "total_balance": total_balance,
    #         "total_interest_payable": total_interest,
    #         "total_overdrafts": total_overdrafts
    #     }
    #
    #     print("Management Report:")
    #     print(f"Total Customers: {report['total_customers']}")
    #     print(f"Total Balance: {report['total_balance']}")
    #     print(f"Total Interest Payable: {report['total_interest_payable']}")
    #     print(f"Total Overdrafts: {report['total_overdrafts']}")
    #
    #     return report
    def generate_management_report(self):
        total_customers = len(self.accounts_list)
        total_balance = sum(customer.get_balance() for customer in self.accounts_list)
        total_interest = sum(customer.get_balance() * customer.get_interest_rate() for customer in self.accounts_list)
        total_overdrafts = sum(
        max(0, customer.get_balance() - customer.get_overdraft_limit())
        for customer in self.accounts_list
        )
        report = {
             "total_customers": total_customers,
             "total_balance": total_balance,
             "total_interest_payable": total_interest,
             "total_overdrafts": total_overdrafts
        }

        print("Management Report:")
        print(f"Total Customers: {report['total_customers']}")
        print(f"Total Balance: {report['total_balance']}")
        print(f"Total Interest Payable: {report['total_interest_payable']}")
        print(f"Total Overdrafts: {report['total_overdrafts']}")

        return report


app = BankSystem()
app.run_main_options()
