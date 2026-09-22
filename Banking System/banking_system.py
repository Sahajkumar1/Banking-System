import random
from datetime import datetime


accounts = {}



def generate_account_number():
    while True:

        account_number = str(random.randint(10000000, 99999999))




        if account_number not in accounts:
            return account_number



def create_account():
    print("\n:::: CREATE ACCOUNT ::::")

    name = input("Enter your name: ")

    phone = input("Enter phone number: ")
    pin = input("Create 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():

        print("PIN must contain exactly 4 digits.")
        return

    account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []


    }

    print("\nAccount created successfully!")
    print("Your Account Number is:", account_number)



def login():

    print("\n:::: LOGIN ::::")

    account_number = input("Enter account number: ")


    pin = input("Enter PIN: ")

    if account_number in accounts:
        if accounts[account_number]["pin"] == pin:

            print("\nLogin successful!")

            print("Welcome,", accounts[account_number]["name"])
            user_menu(account_number)

        else:


            print("Incorrect PIN.")
    else:
        print("Account not found.")



def check_balance(account_number):
    balance = accounts[account_number]["balance"]

    print("\n:::: ACCOUNT BALANCE ::::")

    print("Account Holder:", accounts[account_number]["name"])
    print("Account Number:", account_number)



    print("Current Balance: ₹", balance)


def deposit(account_number):
    print("\n:::: DEPOSIT MONEY ::::")

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:

            print("Enter a valid amount.")


            return

        accounts[account_number]["balance"] += amount

        transaction = {
            "type": "Deposit",

            "amount": amount,

            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        accounts[account_number]["transactions"].append(transaction)

        print("₹", amount, "deposited successfully.")


        print("New Balance: ₹", accounts[account_number]["balance"])

    except ValueError:

        print("Please enter a valid number.")



def withdraw(account_number):
    print("\n:::: WITHDRAW MONEY ::::")

    try:



        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:

            print("Enter a valid amount.")
            return

        if amount > accounts[account_number]["balance"]:
            print("Insufficient balance.")


            return

        accounts[account_number]["balance"] -= amount

        transaction = {


            "type": "Withdrawal",
            "amount": amount,

            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        accounts[account_number]["transactions"].append(transaction)

        print("₹", amount, "withdrawn successfully.")


        print("Remaining Balance: ₹", accounts[account_number]["balance"])

    except ValueError:
        print("Please enter a valid number.")



def transfer(account_number):
    print("\n:::: TRANSFER MONEY ::::")

    receiver = input("Enter receiver account number: ")



    if receiver not in accounts:


        print("Receiver account not found.")
        return

    if receiver == account_number:


        print("You cannot transfer money to your own account.")
        return

    try:
        amount = float(input("Enter amount to transfer: "))

        if amount <= 0:
            print("Enter a valid amount.")


            return

        if amount > accounts[account_number]["balance"]:
            print("Insufficient balance.")


            return

        accounts[account_number]["balance"] -= amount

        
        accounts[receiver]["balance"] += amount

        current_time = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"


        )

       
        accounts[account_number]["transactions"].append({
            "type": "Transfer",
            "amount": amount,

            "date": current_time,

            "details": "Transferred to " + receiver
        })

       
        accounts[receiver]["transactions"].append({
            "type": "Received",
            "amount": amount,

            "date": current_time,
            "details": "Received from " + account_number
        })

        print("₹", amount, "transferred successfully.")

    except ValueError:

        print("Please enter a valid amount.")



def transaction_history(account_number):

    print("\n:::: TRANSACTION HISTORY ::::")

    transactions = accounts[account_number]["transactions"]

    if len(transactions) == 0:
        print("No transactions found.")

        return

    for i, transaction in enumerate(transactions, start=1):

        print("\nTransaction", i)

        print("Type:", transaction["type"])

        print("Amount: ₹", transaction["amount"])
        print("Date:", transaction["date"])

        if "details" in transaction:


            print("Details:", transaction["details"])



def change_pin(account_number):
    print("\n:::: CHANGE PIN ::::")

    old_pin = input("Enter old PIN: ")



    if old_pin != accounts[account_number]["pin"]:
        print("Incorrect old PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ")


    confirm_pin = input("Confirm new PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():

        print("PIN must contain exactly 4 digits.")
        return

    if new_pin != confirm_pin:

        print("New PINs do not match.")
        return

    accounts[account_number]["pin"] = new_pin

    print("PIN changed successfully.")



def user_menu(account_number):

    while True:

        print("\n{/////////////////////////////")
        print("BANKING DASHBOARD")
        print("////////////////////////////////")
        print("1. Check Balance")

        print("2. Deposit Money")


        print("3. Withdraw Money")

        print("4. Transfer Money")


        print("5. Transaction History")
        print("6. Change PIN")

        print("7. Logout")

        print("//////////////////////////////////")

        choice = input("Enter your choice: ")

        if choice == "1":


            check_balance(account_number)

        elif choice == "2":

            deposit(account_number)

        elif choice == "3":



            withdraw(account_number)

        elif choice == "4":


            transfer(account_number)

        elif choice == "5":

            transaction_history(account_number)

        elif choice == "6":

            change_pin(account_number)

        elif choice == "7":


            print("\nLogged out successfully.")
            break


        else:
            print("Invalid choice. Please try again.")



def main():

    while True:

        print("\n")
        print("////////////////////////////////////////")
        print("BANKING SYSTEM")
        print("////////////////////////////////////////")
        print("1. Create Bank Account")
        print("2. Login")
        print("3. Exit")
        print("/////////////////////////////////////////")

        choice = input("Enter your choice: ")

        if choice == "1":


            create_account()

        elif choice == "2":
            login()



        elif choice == "3":
            print("\nThank you for using Banking System.")
            break

        else:

            print("Invalid choice.")



if __name__ == "__main__":
    main()