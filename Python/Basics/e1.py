name = input("Enter your name: ")
print(f"Hello, {name}")

message = """How may i help you sir !!

Please select any of them option,
Type 1 >>>> CHECK BALANCE
Type 2 >>>> DEPOSIT
Type 3 >>>> WITHDRAWL"""

print(message)
task = int(input("\nEnter your input: "))
available_amount= 5000

if task >= 1 and task <= 3:
    print('\nWelcome in your virtual bank')

    if task == 1:
        #check balance
        print(f"\nYour available amount is {available_amount} INR")
    
    elif task == 2:
        # deposit amount
        deposit_amount = int(input("\nPlease enter the amount : "))
        
        if deposit_amount < 0:
            print("\nEnter a valid value")
            
        else:
            available_amount += deposit_amount
            print(f"\nYou have successfully deposited INR {deposit_amount}")
            print(f"\nYour available amount is : {available_amount}")
        
    
    else:
        # withdrawal amount
        withdrawal_amount = int(input("\nPlease enter the amount: "))

        if available_amount < withdrawal_amount:
            print(f"\nYou have insufficient balance of INR {available_amount} to withdraw\n")

        else:
            available_amount -= withdrawal_amount
            print(f"\nYou have successfully withdrawn INR {withdrawal_amount}")
            print(f"\nYour availabe balance is INR {available_amount}\n")
    
else:
    print("Please enter valid option in between 1, 2 or 3")





