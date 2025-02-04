#Sadam Hashi, CIS 345, 1:30pm-2:45pm, PE1

import os

# Declaring objects for balances and transactions
account = 1000.00
pin = '9999'

# Allow  invalid pin entries
tries = 1
max_tries = 3

while tries <= max_tries:
    # Print bank title and menu
    print (f'{"Cactus Bank":^30}\n')
    selection = input('Enter pin or x to exit application: ').casefold()
    if selection == 'x':
        break
    elif selection != pin:
        # Clear screen
        os.system('clear')

        print(f"Incorrect Pin. Attempt {tries} of {max_tries}. Please Try again")

        if tries == max_tries:
            print("Locked out! Exiting program")
        #incrementing tries
        tries += 1

    else:
        print('Transaction instructions:')
        print('Enter w for Withdrawal or d Deposit followed by dollar amount.')
        print('Example withdrawal of $10.50 you would enter w10.50')
        print('All dollar amounts must be positive numbers')

        # Using a for loop to prompt the user and make needed calculations
        for num in range(1,5):
            print(f"\nBalance: ${account: .2f}")
            selection = input(f'Enter x to exit application or Enter transaction {num}: ').casefold()
            if selection[0] == 'x':
                exit()
            # Exceptions handling
            if len(selection) < 2:
                print("Invalid entry. Please provide the transaction type and followed by the amount.")
                continue
            # Slicing the data with new objects
            transaction = selection[0:1]
            amount = float(selection[1:])

            if transaction == 'w' and 0 <= amount <= account:
                account = account - amount
                print(f"After Withdrawal new balance is {account}")
            if transaction == 'd' and amount >= 0:
                account += amount
                print(f"After Deposit new balance is {account}")
            else:
                print("Invalid entry. Please try again.")
            # Loop ends here
    #Application Loop ends here