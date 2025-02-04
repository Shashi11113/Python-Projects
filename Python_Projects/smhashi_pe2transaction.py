# Sadam Hashi, CIS345, 1:30pm - 2:45pm, PE2

import os

# TODO: modify the users data structure
accounts = {'smhashi':{'Pin': 9999, 'Name': 'Sadam Hashi', 'C': 1000, 'S': 500},
            'selin2': {'Pin': 8888, 'Name': 'Elva Lin','C': 1.00, 'S': 25.50}}
pin = 0
ans = ''

# Allow 3 invalid pin entries
tries = 1
pin_tries = 1
max_tries = 3
pin_found = False

username = input('Welcome to Cactus Bank.  Please enter your username: ')

while tries <= max_tries:
    # Print bank title and menu
    print(f'{"Cactus Bank":^30}\n')
    selection = input('Enter pin or x to exit application: ').casefold()

    # determine exit, pin not found, or correct pin found
    if selection == 'x':
        break
    # FIXME: Verify entered pin is the same as the pin stored in the accounts dictionary
    elif int(selection) != accounts[username]['Pin']:
        # clear screen - cls for windows and clear for linux or os x
        os.system("clear")
        print(f'Invalid pin. Attempt {tries} of {max_tries}. Please Try again')
        if tries == max_tries:
            print('Locked out!  Exiting program')
        # increment tries
        tries += 1
    else:
        # Upgrade: successful pin entry. reset tries and save pin
        tries = 1
        pin = selection

        # clear screen
        os.system("clear")

        # TODO: Welcome customer
        print(f"Welcome {accounts[username]['Name']}\n{'Select Account':>18}")

        # TODO: Add prompt for Checking or Savings
        while True:
            selection = input("Enter C or S for (C)ecking or (S)aving: ").upper()
            try:
                if selection != 'C' and selection != 'S':
                    raise ValueError("Incorrect Selection. You must enter C or S.")
            except ValueError as ex:
                print(ex)
            else:
                os.system("clear")
                print(f"Opening {selection} Account... \n")
                break
        # Upgrade: Removed slicing and w/d entry - New Instructions
        print('Transaction instructions:')
        print(' - Withdrawal enter a negative dollar amount: -20.00.')
        print(' - Deposit enter a positive dollar amount: 10.50')

        # FIXME: Print out the balance balance in the accounts dictionary
        account = accounts[username][selection]
        print(f'\nBalance:  ${account: .2f}')

        # TODO: Add exception handling for user entry of amount
        try:
            amount = float(input(f'Enter transaction amount: '))
        except Exception:
            print("Bad Amount - No Transaction.")
            amount = 0.0
        # FIXME: All references to account need to be fixed
        # add indices for username and selection holding account type
        if (amount + account) >= 0:
            account += amount
            accounts[username][selection] += amount
            print(f'Transaction complete. New balance is {account: .2f}')
        else:
            print('Insufficient Funds. Transaction Cancelled.')

# end of application loop

