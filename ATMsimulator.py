# ATM Simulator Project
print("****************************Welcome to our ATM services!*******************")

# Sample data for user accounts
users = {
    "1234567890": {"pin": "1234", "balance": 5000},
    "9876543210": {"pin": "4321", "balance": 10000}
}

def login():
    print("Welcome to Python ATM")
    card = input("Enter your card number: ")
    pin = input("Enter your PIN: ")

    if card in users and users[card]["pin"] == pin:
        print("Login successful.\n")
        atm_menu(card)
    else:
        print("Invalid card number or PIN.\n")

def atm_menu(card):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your current balance is ₹{users[card]['balance']}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹")) 
            users[card]["balance"] += amount
            print("Amount deposited successfully.")
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= users[card]["balance"]:
                users[card]["balance"] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
login()
