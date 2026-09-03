#
#   Name:
#       Teller.py
#   Author:
#       Derek Vuong (dv)
#   Revision History:
#       Aug-28-26: Started (dv)
#
#       Sep-01-26: added proper case-handling for being logged in and logged
#       out. removed arguments from dvAccount methods. variables are now assigned
#       within the methods themselves. added functions:
#           + sign_up - sign up for bank teller
#           + log_out - log out of bank teller
#       will try to comment code more within the following days. (dv)
#
#       Sep-03-26: moved dvAccount class into Account.py. added wrappers for
#       dvAccount functions:
#           + deposit, withdraw, transfer
#       added new function
#           + log_out - log out of bank teller so we can log in again.
#       in general, this program is a lot more functional than it was just a few
#       days ago. now you can sign in and out of accounts, and perform all necessary
#       bank account operations. i hope to add writing to files next week. (dv)
#

from dvutil import dvUtil

import Account
import sys

# Account registry for storing and looking up accounts.
account_registry = {"0" : Account.dvAccount("0", "test", 3.00)}
Account.reg_dict = account_registry

# Global ID for generating account IDs.
global_id = 0

# Pointer to the account we're currently signed into.
current_account = None

#
#   Name:
#       sign_up
#   Description:
#       create an account for the bank.
#

def sign_up():
    global global_id, account_registry, current_account

    print("Welcome to the dvBankTeller Sign-Up page!")
    
    global_id += 1
    id_string = f"{global_id:06d}"
    
    while 1:
        name = input("Enter account name here. This information\n"
                     "will be used during the log-in process.\n"
                     "--> ")
        
        balance = dvUtil.input_to_float("Enter your desired starting balance.\n"
                                      "--> ")

        check = input("\nNew Account details:\n"
                      f"-> Name: {name}\n"
                      f"-> Balance: ${balance}\n"
                      f"-> ID is #{id_string}\n"
                      "If these details are correct, press any key to continue\n"
                      "the sign up process. Otherwise, press \"N\" to restart the\n"
                      "sign-up process.\n"
                      "--> ")
        
        if check.capitalize() == "N":
            continue
        
        print("\nThank you for signing up for dvBankTeller!\n")

        account_registry[id_string] = Account.dvAccount(id_string, name, balance)
        current_account = account_registry[id_string]
        break

#
#   Name:
#       log_in
#   Description:
#       Sign into your bank account.
#

def log_in():
    global account_registry, current_account
    
    name = input("Enter account id.\n"
                 "--> ")
    
    if name in account_registry:
        current_account = account_registry[name]
        print(f"\nSuccesfully logged into: {current_account.m_name}\n")
    else:
        print("Given account id does not exist\n"
              "in bank database!\n")

#
#   Name:
#       logout
#   Description:
#       Sign out of your current bank account.
#

def logout():
    global current_account
    
    check = input("Are you sure you would like to\n"
                  "sign out of your account?\n"
                  "If no, type \"N\", otherwise press\n"
                  "any key to continue.\n"
                  "--> "
        )
    
    if check.capitalize() != "N":
        print("\nYou have been logged out of your account.\n")
        current_account = None

#
#   Safe wrappers for dvAccount methods, incase current_account
#   returns as nullptr/None (dv)
#

def deposit():
    if current_account: current_account.deposit()
def withdraw():
    if current_account: current_account.withdraw()
def transfer():
    if current_account: current_account.transfer()

#
#   Global function pointer table.
#

login_modes = (
        deposit,
        withdraw,
        transfer,
        logout,
        sys.exit
    )

logout_modes = (
        log_in,
        sign_up,
        sys.exit
    )

#
#   Name:
#       main
#   Description:
#       Primary main while loop for using the bankTeller.
#

def main():
    print("Welcome to the dvBankTeller!")
    while 1:
        if current_account:
            function_table = login_modes
            mode = dvUtil.input_to_int(f"Logged in as: {current_account.m_name}\n"
                                       f"Balance: ${current_account.m_balance}, ID: #{current_account.m_num}\n"
                                       "Enter mode:\n"
                                       "1. Deposit.\n"
                                       "2. Withdraw.\n"
                                       "3. Transfer.\n"
                                       "4. Logout.\n"
                                       "5. Quit\n"
                                       "--> ",)
        else:
            function_table = logout_modes
            mode = dvUtil.input_to_int("Enter mode:\n"
                                       "1. Log in.\n"
                                       "2. Sign up.\n"
                                       "3. Quit\n"
                                       "--> ",)

        # check for validity of input!
        if mode is None or (mode > len(function_table) or mode < 1):
            print("Invalid mode given!\n")
            continue
        
        print("\n", end="")
        function_table[mode-1]()

if __name__ == "__main__":
    main()
