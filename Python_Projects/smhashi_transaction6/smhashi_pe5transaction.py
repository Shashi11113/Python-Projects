# Sadam Hashi, CIS 345, 1:30pm to 2:45pm, PE5

# os allows us to clear the screen in an actual console or terminal
import os
# json will allow us to parse data in the customers.json file
import json
# importing a module file that contains important functions
from smhashi_logger import *
# allow the current date and time to be printed
import time

# Read customers data file into accounts
with open("customers.json") as file_handle:
    accounts = json.load(file_handle)

# Allow 3 invalid pin entries
tries = 1
max_tries = 3

# List to record transactional data
logger = []

# App header
print('Welcome!')
print('Welcome to Cactus Bank Application')
print('********************************')
print('* Enter 1 to add a new student *')
print('* Enter 2 to delete a student  *')
print('* Enter 3 to make transactions *')
print('* Enter 4 to exit Application  *')
print('********************************')

while True:
    try:
        selection = int(input('Select an operation: '))
        if selection not in range(1, 5):
            raise TypeError
        break
    except (ValueError, TypeError):
        print('Selection should be 1, 2, 3, or 4. Try again...')

if selection == 1:
    username = input('Please enter a username: ')
    if username in accounts:
        print("Username exists in the system.")
        exit()

    pin = create_pin()

    # Ensure the user provides a non-empty name
    while True:
        name = input('Please enter your name: ').strip()
        if name == '':
            print('Name cannot be empty. Please enter a valid name.')
        else:
            break  # Exit the loop when a valid name is entered

    # Initializes the account with zero balances
    accounts[username] = {"Pin": pin, "Name": name, "C": 0.0, "S": 0.0}

    # Add initial deposit to checking and savings accounts
    for account_type in ["C", "S"]:
        while True:
            try:
                value = float(input(f'Enter the amount you will deposit to the {account_type} account: '))
                if value < 0:
                    print('Invalid number entered. The current balance will be 0.0')
                    accounts[username][account_type] = 0
                    break
                accounts[username][account_type] = value
                break
            except (ValueError, TypeError):
                print('Invalid number entered. The current balance will be 0.0')
                accounts[username][account_type] = 0
                break

    print('Your account has been created')
    print("Please visit the system again to make transactions")
    input('Press Enter to continue...')
    print('\n\nSaving data...')
    with open('customers.json', 'w') as file_handle:
        json.dump(accounts, file_handle)

    print_accounts(accounts)

elif selection == 2:
    username = input('Please enter a username: ')
    if username in accounts:
        accounts.pop(username)
        print(f'Customer {username} has been deleted')
        print('\n\nSaving data...')
        with open('customers.json', 'w') as file_handle:
            json.dump(accounts, file_handle)

        print_accounts(accounts)
    else:
        print(f'Username {username} is not in the system')

elif selection == 3:
    while True:  # Main application loop
        username = input('Please enter a username: ').casefold()
        print("Cactus Bank - Making Transactions")
        tries = 1  # Reset tries for a new username input

        # Check for a valid username
        if username not in accounts:
            print('Error: username is not in the system.')
            exit()  # Ask for username again if it doesn't exist
        customer_username = username

        while tries <= max_tries:
            pin_input = input('\nEnter pin or x to exit application: ').casefold()

            if pin_input == 'x':
                print('Exiting application. Thank you for visiting Cactus Bank!')
                exit(0)  # Exit the entire program

            try:
                pin_input = int(pin_input)  # Convert pin input to integer
                if pin_input != accounts[username]['Pin']:
                    os.system('clear')
                    print(f'Invalid pin. Attempt {tries} of {max_tries}. Please Try again')
                    tries += 1
                else:
                    os.system('clear')
                    print(f"Welcome {accounts[username]['Name']}")
                    break  # Successful pin, exit the pin entry loop
            except ValueError:
                print(f'Invalid input. Please enter a valid pin or "x" to exit. Attempt {tries} of {max_tries}')
                tries += 1
                continue  # Ask for pin again if input is invalid

        if tries > max_tries:
            while True:  # Loop until valid input is provided
                new_pin = input("Do you want to get a new pin (y/n)? ").lower()
                if new_pin == 'y':
                    accounts[username]['Pin'] = create_pin() # Create a new pin and assign it
                    print("Please visit the system again to make transactions")
                    input('Press Enter to continue...')
                    print('\n\nSaving data...')
                    with open('customers.json', 'w') as file_handle:
                        json.dump(accounts, file_handle)
                    print('\nData Saved.\nExiting...')
                    print_accounts(accounts)
                    customers_accounts_average(accounts)
                    exit()  # Exit loop after creating a new pin
                elif new_pin == 'n':
                    print("Exiting application.")
                    exit()  # exit the program
                else:
                    print("Invalid entry. Please enter 'y' to get a new pin or 'n' to exit application.")

        transactions = 0  # Initialize transaction counter

        while True:  # Main transaction loop
            while transactions < 4:  # Allow up to 4 transactions before requiring a PIN re-entry
                print(f'{"Select Account": ^20}')
                selection = input('Enter C or S for (C)hecking or (S)avings: ').upper()

                if selection not in ['C', 'S']:
                    print('Incorrect selection. You must enter C or S.')
                    continue  # Ask for input again

                os.system('clear')
                print(f'Opening {selection} Account...\n')

                # Transaction instructions
                print('Transaction instructions:')
                print(' - Withdrawal enter a negative dollar amount: -20.00.')
                print(' - Deposit enter a positive dollar amount: 10.50')

                print(f'\nBalance: ${accounts[username][selection]:,.2f}')

                date_time = time.ctime()
                old_balance = '${:,.2f}'.format(accounts[username][selection])

                try:
                    amount = float(input(f'Enter transaction amount: '))
                except ValueError:
                    print('Invalid input. No transaction performed.')
                    continue  # Ask for transaction amount again
                transaction_amount = '${:,.2f}'.format(amount)

                # Validate transaction and update account balance safely
                if (amount + accounts[username][selection]) >= 0:
                    # Correct balance update logic
                    accounts[username][selection] = round((accounts[username][selection] + amount), 2)
                    print(f'Transaction complete. New balance is {accounts[username][selection]:,.2f}')

                else:
                    print('Insufficient Funds. Transaction Cancelled.')
                new_balance = '${:,.2f}'.format(accounts[username][selection])
                transactions += 1  # Increment the transaction counter

                transaction_data = [date_time, customer_username, old_balance, transaction_amount, new_balance]
                logger.append(transaction_data)
                log_transactions(logger)

                if transactions >= 4:
                    print('You have reached the maximum of 4 transactions without re-entering the PIN.')
                    break  # Break the transaction loop after 4 transactions

                # Ask if the user wants to make another transaction or exit
                next_action = input('Press n to make another transaction or x to exit application: ').casefold()

                # Correct loop logic for next_action
                while next_action not in ['n', 'x']:
                    print("Invalid Entry, Please enter 'n' to continue or 'x' to exit application.")
                    next_action = input('Press n to make another transaction or x to exit application: ').casefold()

                if next_action == 'x':
                    print('\n\nSaving data...')
                    with open('customers.json', 'w') as file_handle:
                        json.dump(accounts, file_handle)
                    print('\nData Saved.\nExiting...')
                    print_accounts(accounts)
                    customers_accounts_average(accounts)
                    exit()  # Exit the transaction loop

            # After 4 transactions, require PIN re-entry
            if transactions >= 4:
                print('Re-enter your PIN to continue making more transactions.')
                while tries <= max_tries:
                    pin_input = input('Enter pin or x to exit application: ').casefold()

                    if pin_input == 'x':
                        print('\n\nSaving data...')
                        with open('customers.json', 'w') as file_handle:
                            json.dump(accounts, file_handle)
                        print('\nData Saved.\nExiting...')
                        print_accounts(accounts)
                        customers_accounts_average(accounts)
                        exit() # Exit the entire program
                    try:
                        pin_input = int(pin_input)  # Convert pin input to integer
                        if pin_input != accounts[username]['Pin']:
                            print(f'Invalid pin. Attempt {tries} of {max_tries}. Please try again.')
                            tries += 1
                        else:
                            os.system('clear')
                            print(f"Welcome back, {accounts[username]['Name']}")
                            transactions = 0  # Reset transaction count after successful PIN entry
                            break  # Exit the pin re-entry loop
                    except ValueError:
                        print(f'Invalid input. Please enter a valid pin or "x" to exit. Attempt {tries} of {max_tries}')
                        tries += 1
                        continue  # Ask for pin again if input is invalid

                if tries > max_tries:
                    print('Maximum attempts exceeded. Exiting...')
                    exit()  # Exit after max pin attempts

            # Save data to file and display current data
            print('\n\nSaving data...')
            with open('customers.json', 'w') as file_handle:
                json.dump(accounts, file_handle)
            print('\nData Saved.\nExiting...')
            print_accounts(accounts)
            customers_accounts_average(accounts)

elif selection == '4':
    exit(0)

log_transactions(logger)
