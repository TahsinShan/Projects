print("Welcome to my ATM!")
pin = input("Input your Name: ")
balance = 10000

if pin == "Shan":
    while True:
        d = input("- 1. Check balance - 2. Deposit money - 3. Withdraw money - 4. Exit: ")
        
        if d == "1":
            print("Your balance is ", balance)
        elif d == "2":
            dep = input("Enter amount to deposit: ")
            balance = balance + int(dep)
            print("Your new balance is ", balance)
        elif d == "3":
            withd = input("Enter amount to withdraw: ")
            if int(withd) > balance:
                print("Insufficient funds")
            else:
                balance = balance - int(withd)
                print("Your new balance is ", balance)
        elif d == "4":
            print("Goodbye")
            break
        else:
            print("Invalid option. Please try again.")
else:
    print("Incorrect pin")
