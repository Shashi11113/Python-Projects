# Sadam Hashi, CIS 345, 1:30pm to 2:45pm, PE5

import csv
from os import path
import random
import statistics

def log_transactions(logger):
    # Check if the file exists
    file_exists = path.isfile('transactions.csv')

    with open('transactions.csv', 'a', newline = '') as fp:
        data = csv.writer(fp)
        if not file_exists:
            # Write the header if the file does not exist
            data.writerow(['DateTime', 'Username', 'Old Balance', 'Transaction Amount', 'New Balance'])
        # Write the transaction data
        for transaction in logger:
            data.writerow(transaction)
        logger.clear()


# A function that prints the current data in the customers file
def print_accounts(accounts):
    for username, details in accounts.items():
        print(f'{username:>7} {details["Pin"]:>8} {details["Name"]:>17} {details["C"]:>14,.2f} {details["S"]:>17,.2f}')


def create_pin():
    tries = 1
    max_tries = 3

    while tries <= max_tries:
        try:
            choice = input('Enter 1 to create a pin yourself or 2 and the system will create a pin for you: ')


            choice = int(choice)
            if choice != 1 and choice != 2:
                raise ValueError("Invalid entry. Please select 1 or 2.")

            if choice == 1:
                print('You have 3 tries to enter a number between 1 and 9999 as your pin.')
                print("If you don't reset your pin after 3 tries, the system will create a pin for you.")
                # User creates their own pin
                while tries <= max_tries:
                    try:
                        pin = int(input('Select a number between 1 and 9999 as your pin: '))
                        if 0 < pin < 10000:
                            print(f"Your pin is: {pin}")
                            return pin  # Return the valid pin
                        else:
                            print(f'pin needs to be an integer between 1 and 9999.\n'
                                  f'Invalid pin. Attempt {tries} of {max_tries}.')
                    except (ValueError, TypeError):
                        print(f'Invalid pin. Attempt {tries} of {max_tries}.')
                    tries += 1  # Increment tries after each attempt

            elif choice == 2:
                # System generates a pin
                pin = random.randint(1, 9999)
                print(f"Your pin is: {pin}")
                return pin  # Return the system-generated pin

        except (ValueError, TypeError):
            print("Please select 1 or 2.")

    # If max attempts are reached without valid input, generate a random pin
    pin = random.randint(1, 9999)
    print(f"This system will create a pin randomly for you\nYour pin is: {pin}")
    return pin


# Function to display average balances and customers
def customers_accounts_average(accounts):
    checking_balance = [account['C'] for account in accounts.values()]
    savings_balance = [account['S'] for account in accounts.values()]

    avg_checking = statistics.mean(checking_balance)
    avg_savings = statistics.mean(savings_balance)

    print(f"\nChecking accounts' average is {avg_checking:,.2f}")
    print(f"Savings accounts' average is {avg_savings:,.2f}")

    print("Customers whose checking account balance is above the average:")
    for username, account in accounts.items():
        if account['C'] > avg_checking:
            print(f"username is {username} and name is {account['Name']}")

    print("Customers whose saving account balance is above the average:")
    for username, account in accounts.items():
        if account['S'] > avg_savings:
            print(f"username is {username} and name is {account['Name']}")


