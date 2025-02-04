# Sadam Hashi, CIS 345, 1:30pm to 2:45pm, PE3

# os allows us to clear the screen in an actual console or terminal
import os
# TODO X: Add imports for json
import json
# TODO X: Read customers data file into accounts
file_handle = open("customers.json")
accounts = json.load(file_handle)
file_handle.close()
# 'aaa1': {'Pin': 1234, 'Name': 'Brit Masters', 'C': 8.62, 'S': 922.07}}

# Allow 3 invalid pin entries
tries = 1
max_tries = 3

# In this PE exercise, we will only test the existing username
username = input('Welcome to Cactus Bank! Please enter your username: ')
while tries <= max_tries:
    # Print bank title and menu
    print(f'{"Cactus Bank":^30}\n')
    selection = input('Enter pin or x to exit application: ').casefold()

    # determine exit, pin not found, or correct pin found
    if selection == 'x':
        break
    # Verify entered pin is a key in accounts
    elif int(selection) != accounts[username]['Pin']:
        # clear screen - cls for windows and clear for linux or os x
        os.system('clear')
        # os.system('clear') for mac users
        print(f'Invalid pin. Attempt {tries} of {max_tries}. Please Try again')
        if tries == max_tries:
            print('Locked out! Exiting program')
        tries += 1
    else:
        # Successful pin entry. reset tries and save pin
        tries = 1
        pin = selection
        os.system('clear')
        # os.system('clear')

        for t in range(1, 5):
            # Welcome customer
            print(f"Welcome {accounts[username]['Name']}")
            print(f'{"Select Account": ^20}')

            # Prompt for Checking or Savings
            while True:
                try:
                    selection = input('Enter C or S for (C)hecking or (S)avings: ').upper()
                    if selection != 'C' and selection != 'S':
                        raise ValueError('Incorrect selection. You must enter C or S.')
                except ValueError as ex:
                    print(ex)
                else:
                    os.system('clear')
                    print(f'Opening {selection} Account...\n')
                    break
            # End Prompt Checking or Savings

            print('Transaction instructions:')
            print(' - Withdrawal enter a negative dollar amount: -20.00.')
            print(' - Deposit enter a positive dollar amount: 10.50')

            # FIXME X: Modify the code below to display the selected account's balance with commas for thousands
            print(f'\nBalance: ${accounts[username][selection]:,.2f}')
            amount = 0.00
            try:
                amount = float(input(f'Enter transaction amount: '))
                # FIXME X: Catch appropriate exceptions not just Exception
                # print better error message details using exception object
            except (ValueError, TypeError) as ex:
                print(f'Error: {ex}. No Transaction.')
                amount = 0.00

            # Verify enough funds in account
            if (amount + accounts[username][selection]) >= 0:
                # FIXME X: round() new account balance to 2 decimal places
                accounts[username][selection] = round((accounts[username][selection] + amount), 2)
                # Do this step last after running your program.
                # FIXME X: Modify formatting to add commas for thousands
                print(f'Transaction complete. New balance is {accounts[username][selection]:,.2f}')
            else:
                print('Insufficient Funds. Transaction Cancelled.')

            ans = input('Press n to make another transaction or x to exit application: ').casefold()
            if ans[0] == 'x':
                tries = max_tries + 1
                break

# end of application loop
print('\n\nSaving data...')
# TODO X: Write accounts data structure to file
file_handle = open("customers.json")
with open("customers.json", "w") as fp:
    json.dump(accounts, fp)
print('\nData Saved.\nExiting...')
