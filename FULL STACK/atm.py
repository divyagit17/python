#atm system

correct_pin = "1234"
attempts = 3

print( " WELCOME TO ATM SYSTEM ")

while attempts > 0:
    entered_pin = input("Please enter your PIN: ")
    if entered_pin == correct_pin:
        print("PIN accepted. You can now access your account.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempts left.")
        if attempts == 0:
            print("TOO MANY INCORRECT ATTEMPTS. EXITING ")
            exit()


#operations
 
balance = 1000.00
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Please select an option (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${balance:}")

    elif choice == "2":
        deposit_amount = float(input("Enter the amount to deposit: $"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"${deposit_amount:} deposited successfully.")
        else:
            print("Invalid deposit amount.")
            
    elif choice == "3":
        try:
            withdraw = float(input("Enter amount to withdraw: ₹"))
            if withdraw > balance:
                print("Insufficient balance.")
            elif withdraw <= 0:
                print("Withdrawal amount must be greater than 0.")
            else:
                balance -= withdraw
                print(f"₹{withdraw:.2f} withdrawn successfully.")
                print(f"Remaining balance: ₹{balance:}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "4":
        print("Thank you for using the ATM system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")




