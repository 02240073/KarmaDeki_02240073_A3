import random

# Exceptions
class BankingError(Exception): pass
class LoginError(BankingError): pass

# Bank Account
class BankAccount:
    def __init__(self, account_id, passcode, category, funds=0):
        self.id = account_id
        self.passcode = passcode
        self.category = category
        self.funds = funds

    def deposit(self, amount):
        if amount > 0:
            self.funds += amount
            return "Your deposit was successful."
        return "OH HO! Invalid amount."

    def withdraw(self, amount):
        if 0 < amount <= self.funds:
            self.funds -= amount
            return "Your withdrawal was successful."
        return "SORRY! Insufficient funds."

    def transfer(self, amount, recipient):
        if self.withdraw(amount) == "Your withdrawal was successful.":
            recipient.deposit(amount)
            return "Successfully transfered."
        return "OOPS! Transfer failed."

    def topup_mobile(self, number, amount):
        if len(number) >= 8 and amount > 0 and amount <= self.funds:
            self.funds -= amount
            return f"Mobile {number} topped up with {amount}."
        return "Invalid number or amount."


class PersonalAccount(BankAccount):
    def __init__(self, acc_id, passcode, funds=0):
        super().__init__(acc_id, passcode, "Personal", funds)

class BusinessAccount(BankAccount):
    def __init__(self, acc_id, passcode, funds=0):
        super().__init__(acc_id, passcode, "Business", funds)


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_type):
        acc_id = str(random.randint(10000, 99999))
        passcode = str(random.randint(1000, 9999))
        acc = PersonalAccount(acc_id, passcode) if acc_type == "1" else BusinessAccount(acc_id, passcode)
        self.accounts[acc_id] = acc
        return acc

    def login(self, acc_id, passcode):
        acc = self.accounts.get(acc_id)
        if acc and acc.passcode == passcode:
            return acc
        raise LoginError("Opps, Login failed.")


def main():
    bank = BankingSystem()
    while True:
        print("\n1. Open Account\n2. Account Login\n3. Exit")
        choice = input("Please enter your choice: ")

        if choice == "1":
            t = input("1. Personal 2. Business: ")
            acc = bank.create_account(t)
            print(f"Account ID: {acc.id}, Passcode: {acc.passcode}")

        elif choice == "2":
            acc_id = input("Enter your ID: ")
            code = input("Enter Passcode: ")
            try:
                acc = bank.login(acc_id, code)
                while True:
                    print("\n1. Check Balance\n2. Deposit \n3. Withdraw\n4. Transfer\n5. Top-Up\n6. Logout")
                    act = input("Action: ")

                    if act == "1": print(f"Your balance is: {acc.funds}")
                    elif act == "2": print(acc.deposit(float(input("Amount you want to deposite: "))))
                    elif act == "3": print(acc.withdraw(float(input("Amount you want to withdraw: "))))
                    elif act == "4":
                        to = input("To ID: ")
                        amt = float(input("Transfer Amount: "))
                        if to in bank.accounts:
                            print(acc.transfer(amt, bank.accounts[to]))
                        else:
                            print("Sorry! Recipient not found.")
                    elif act == "5":
                        num = input("Mobile number: ")
                        amt = float(input("Amount: "))
                        print(acc.topup_mobile(num, amt))
                    elif act == "6": break
                    else: print("Sorry invalid input, enter between 1 and 5.")
            except LoginError as e:
                print(e)

        elif choice == "3": break
        else: print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
