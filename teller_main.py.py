#
#   Name:
#       teller_main.py
#   Purpose:
#       Bank Teller assignment for Advanced Programming G4
#   Author:
#       Derek Vuong (dv)
#   Revision History:
#       Sep-23-26: Rewrote the program to ulitze classes. Haven't done
#       much error handling yet, sadly. Need to get this to write to files next.
#       Also removed dvLib. It's run it's course at this point, sadly. (dv)
#

from lib.dvutil import dvUtil
from random import randint
import sys

class dvAccount:
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance

SCREEN_STRING = 0
SCREEN_FUNC = 1

def tokenize(string):
    stripped, temp, spacelen, strlen = False, "", 0, len(string)
    for idx, x in enumerate(string):
        if x in special_chars:
            start, stripped, spacelen = idx, True, spacelen + 1
            continue
        elif stripped is True: break
        temp += x
    string = string[len(temp) + spacelen:strlen]
    return temp, string

class dvTeller:
    account_registry = {
            "000-000" : dvAccount("derek", "abc", 999.00)
        }
    current_account = None

    #
    #   Account file syntax -->
    #   000-000
    #   {
    #       name = "Account Name";
    #       password = "pw";
    #       balance = 0.00;
    #   }
    #

    template = (
        "{} {{\n"
        "\tname = {};\n"
        "\tpassword = {};\n"
        "\tbalance = {};\n"
        "}}\n"
    )

    def write_file(self):
        with open('bank_info.bnk', 'w') as f:
            for idx, (key, value) in enumerate(self.account_registry.items()):
                f.write(self.template.format(key, value.name, value.password, value.balance))

    def read_file(self):
        try:
            with open('bank_info.bnk', 'r') as f:
                for ln in f:
                    print(ln)
                    temp_line = ln[:]
                    while temp_line != "":
                        word, temp_line = tokenize(temp_line)
                        print(word)
                        
        except:
            self.write_file()
    #
    #   __init__
    #   Class constructor. The program reads the bank_info.bnk file, re-adds
    #   accounts to the this->account_registry
    #

    def __init__(self):
        self.read_file()

    #
    #   shutdown
    #   Shutdown the bank teller, and write a file to where you invoked
    #   the program.
    #

    def shutdown(self):
        self.write_file()
        sys.exit()

    #
    #   generate_id
    #   Generate an account ID, until we've generated an accountID
    #   that doesn't exist in dvTeller's local account registry.
    #

    def generate_id(self):
        while True:
            new_id = [str(randint(0, 9)) for x in range(0, 6)]
            new_id.insert(len(new_id) // 2, "-")
            new_string = "".join(new_id)
            if new_string not in self.account_registry: break
        return new_string

    #
    #   log_in
    #   Log into an account. Abort if we've inputted incorrect
    #   information.
    #

    def log_in(self):
        print(
            "Enter your account ID, username, and password to log in\n"
            "to your account.\n"
            )

        account_id = input("Enter account ID\n--> ")

        if account_id in self.account_registry:
            account = self.account_registry[account_id]
            
            username = input("Enter username\n--> ")
            password = input("Enter password\n--> ")

            if username != account.username:
                print("Error: Username is invalid.")
                return
            if password != account.password:
                print("Error: Password is invalid.")
                return

            self.current_account = self.account_registry[account_id]

            print(f"Succesfully logged in as {username}!")
        else:
            print("Error: Given Account ID does not exist.")

    #
    #   create_account
    #   Create an account. Run indefinitely if inputting an invalid
    #   starting balance.
    #

    def create_account(self):
        print(
            "To create an account for the dvBankTeller, you must\n"
            "create a username, password, and enter a starting balance.\n"
            "After creating your account, you will be given your account ID.\n"
            "Your account ID will be used to log in, so remember it.\n"
            )

        username = input("Create username\n--> ")
        password = input("Create password\n--> ")
        
        while True:
            try:
                balance = float(input("Enter starting balance\n--> "))
                break
            except ValueError:
                print("Error: You have to enter a valid starting balance!")
                
        new_id = self.generate_id()
        self.current_account = self.account_registry[new_id] = dvAccount(username, password, balance)

        print(
            f"Your Account ID is {new_id}.\n"
            "Thank you for signing up to the dvBankTeller!\n"
            )

    #
    #   deposit
    #   add money to your account. become rich.
    #

    def deposit(self):
        print(
            "Please enter how much you would like to deposit\n"
            "into your account.\n"
            )
        
        while True:
            try:
                ammount = float(input("Enter ammount to deposit\n-->"))
                break
            except ValueError:
                print("Error: Enter a proper numerical value into the deposit box!")
                
        self.current_account.balance += ammount

    #
    #   withdraw
    #   take away money from your account. cannot overdraw. the debt would be
    #   too much for one to handle.
    #

    def withdraw(self):
        print(
            "Please enter how much you would like to withdraw\n"
            "from your account.\n"
            )
        
        while True:
            try:
                ammount = float(input("Enter ammount to withdraw\n-->"))
                break
            except ValueError:
                print("Error: Enter a proper numerical value into the deposit box!")

        if self.current_account.balance - ammount < 0:
            print("\nSorry. Cannot overdraw from account!\n")
            return
        
        self.current_account.balance -= ammount

    #
    #   transfer
    #   enter recipient id, trasnfer amt, and try to transfer from your
    #   account to recipient.
    #

    def transfer(self):
        print(
            "To make a transfer, enter the recipent's account ID,\n"
            "and enter how much you would like to transfer from your account.\n"
            )

        account_id = input("Enter the recipient's account ID\n--> ")

        if account_id not in self.account_registry:
            print("Error: Given account ID does not exist in the registry.")
            return

        #   Get pointer to the recipient's account ID.
        recipient = account_registry[account_id]
        
        while True:
            try:
                ammount = float(input("Enter ammount to deposit\n-->"))
                break
            except ValueError:
                print("Error: Enter a proper numerical value into the deposit box!")
                
        if self.current_account.balance - ammount < 0:
            print("\nSorry. Cannot overdraw from account!\n")
            return
        
        recipient.balance += ammount
        self.current_account.balance -= ammount

    def log_out(self):
        user_input = input(
            "Are you sure you would like to log out?\n"
            "Press any key to abort, or type \"y\" to log out.\n"
            "--> "
            )

        if user_input.lower() == "y":
            self.current_account = None

    #
    #   Screen system
    #   Each screen is a nested tuple that contains what to print
    #   to the console, and function pointers.
    #

    basic_screen = ( # Not logged in.
            (
                "Logged out.\n"
                "1. Sign in\n"
                "2. Create account\n"
                "3. Exit\n"
                "Enter operation\n"
                "--> "
            ),
            (
                log_in,
                create_account,
                shutdown
            ),
        )

    account_screen = ( # Logged in.
            (
                f"Logged in as %s. Current balance is: %.3f\n"
                "1. Deposit\n"
                "2. Withdraw\n"
                "3. Transfer\n"
                "4. Log out\n"
                "5. Exit\n"
                "Enter operation\n"
                "--> "
            ),
            (
                deposit,
                withdraw,
                transfer,
                log_out,
                shutdown
            ),
        )

    #
    #   display
    #   Print a screen to the console, read user input, and
    #   execute the proper function from the user's input.
    #

    def display(self):
        try:
            if self.current_account is None:
                screen = self.basic_screen
                user_input = int(input(screen[SCREEN_STRING])) - 1
            else:
                screen = self.account_screen
                user_input = int(input(screen[SCREEN_STRING] % (self.current_account.name, self.current_account.balance))) - 1
        except ValueError:
            print("Error: You must enter a number to run an operation!")
            return
        if user_input in range(0, len(screen[SCREEN_FUNC])): screen[SCREEN_FUNC][user_input](self)
        else: print("Error: Operation is not on the list!")

main = dvTeller()

if __name__ == "__main__":
    while True: main.display()
