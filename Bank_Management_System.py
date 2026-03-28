accounts = []

def create_account():
    print("Select the type of account to be created:")
    print("1. Savings Account")
    print("2. Current Account")
    choice = input("Enter the type of account to be created (1-2): ")
    if choice == "1":
        savings_account()
    elif choice == "2":
        current_account()
    else:
        print("Invalid choice")

def savings_account():
    print("You have selected Savings Account")
    print("This account yields an interest of 7.25%")

    acc_number = int(input("Enter Account Number: "))
    for acc in accounts:
        if acc[0] == acc_number:
            print("Account already exists.")
            return  

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    if balance < 500:
        print("Minimum balance should be Rs.500")
        return  
    accounts.append([acc_number, name, balance])
    print(f"Account created for {name}!")

def current_account():
    print("You have selected Current Account")

    acc_number = int(input("Enter Account Number: "))
    for acc in accounts:
        if acc[0] == acc_number:
            print("Account already exists.")
            return
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    accounts.append([acc_number, name, balance])
    print(f"Current account created for {name}!")
 
def deposit():
    acc_number = int(input("Enter Account Number: "))
    for acc in accounts:
        if acc[0] == acc_number:
            amount = float(input("Enter Deposit Amount: "))
            acc[2] += amount
            print(f"Deposited {amount}. New Balance: {acc[2]}")
            return
    print("Account not found.")
 
def withdraw():
    acc_number = int(input("Enter Account Number: "))
    for acc in accounts:
        if acc[0] == acc_number:
            amount = float(input("Enter Withdrawal Amount: "))
            if amount > acc[2] -500:
                print("Insufficient balance. Maintain minimum balance")
            else:
                acc[2] -= amount
                print(f"Withdrawn {amount}. New Balance: {acc[2]}")
            return
    print("Account not found.")
 
def check_balance():
    acc_number = int(input("Enter Account Number: "))
    for acc in accounts:
        if acc[0] == acc_number:
            print(f"Account Holder: {acc[1]}")
            print(f"Balance: {acc[2]}")
            return
    print("Account not found.")
 
def display_all():
    if not accounts:
        print("No accounts found.")
        return
    print(f"{'Acc No':<10} {'Name':<20} {'Balance':>10}")
    print("-" * 42)
    for acc in accounts:
        print(f"{acc[0]:<10} {acc[1]:<20} {acc[2]:>10.2f}")
 
while True:
    print("\n--- BMS ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Exit")
 
    choice = input("Enter Choice: ")
 
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        display_all()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
 