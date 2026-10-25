# Task 03: Banking Console Application
# Balance, Deposit and Withdrawal

balance = 10000.00

while True:
    print("\n===== BANKING MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Current Balance: ₹{balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: ₹"))

            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print(f"Updated Balance: ₹{balance:.2f}")
            else:
                print("Invalid amount! Enter an amount greater than zero.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("Invalid amount! Enter an amount greater than zero.")

            elif amount <= balance:
                balance -= amount
                print("Withdrawal successful!")
                print(f"Updated Balance: ₹{balance:.2f}")

            else:
                print("Insufficient balance!")
                print(f"Current Balance: ₹{balance:.2f}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using our Banking Application!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select an option from 1 to 4.")
