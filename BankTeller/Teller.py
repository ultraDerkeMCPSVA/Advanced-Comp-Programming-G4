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

import sys
from dvutil import dvUtil

account_registry = {}
logged_in = False
global_id = 0

def check_for_account(account_id):
    return None

class dvAccount:
    def __init__(self, number, name, balance):
        self.m_num = number
        self.m_name = name
        self.m_balance = balance
        
    def deposit(self):
        num = dvUtil.input_to_int("Enter how much you would like to deposit\n"
                                  "into your account\n"
                                  "--> ")
        self.m_balance += num
        print(f"Added ${num} to your account.\nBalance is now {self.m_balance}.")

    def withdraw(self):
        num = dvUtil.input_to_int("Enter how much you would like to withdraw\n"
                                  "from your account\n"
                                  "--> ")
        if (self.m_balance - num) < 0:
            print("Cannot overdraw from account!")
            return
        self.m_balance -= num
        print(f"Withdrew ${num} from your account.\nBalance is now {self.m_balance}.")

    def transfer(self):
        acc = check_for_account(input("Enter account id to transfer into\n"
                                      "--> "))
        if acc is None:
            return
        if (self.m_balance - num) < 0:
            print("Cannot overdraw from account!")
            return

        self.m_balance, acc.m_balance = self.m_balance - num, acc.m_balance - num
        print(f"transfered {num} from your account into user \"{acc.m_name}\"'s account.")

current_account = dvAccount(0, "", 0)

def write_to_file():
    pass

def sign_up():
    global global_id, logged_in

    print("\nWelcome to the dvBankTeller Sign-Up page!")
    
    global_id += 1
    id_string = f"{global_id:06d}"
    
    while 1:
        name = input("Enter account name here. This information\n"
                     "will be used during the log-in process.\n"
                     "--> ")
        balance = dvUtil.input_to_int("Enter your desired starting balance.\n"
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
        
        account_registry[id_string] = {dvAccount(id_string, name, balance)}
        current_account = account_registry[id_string]
        logged_in = True
        break

def log_in():
    name = input("enter account id.")
    try:
        account_name = account_registry[id_string]
    except:
        print("id does not exist!!")

login_modes = (current_account.deposit, current_account.withdraw, current_account.transfer, None)
logout_modes = (log_in, sign_up)

def main():
    print("Welcome to the dvBankTeller!")
    while 1:
        if logged_in:
            cur_modes = login_modes
            mode = dvUtil.input_to_int("Enter mode:\n"
                                       "1. Deposit.\n"
                                       "2. Withdraw.\n"
                                       "3. Transfer.\n"
                                       "3. Logout.\n"
                                       "--> ",)
        else:
            cur_modes = logout_modes
            mode = dvUtil.input_to_int("Enter mode:\n"
                                       "1. Log in.\n"
                                       "2. Sign up.\n"
                                       "--> ",)
        if mode > len(cur_modes) or mode < 1:
            print("invalid mode given")
            continue
        cur_modes[mode-1]()
    print("\n") # add white-space after every loop.

if __name__ == "__main__":
    main()
