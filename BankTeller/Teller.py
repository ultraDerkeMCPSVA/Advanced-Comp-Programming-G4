#
#   Name:
#       Teller.py
#   Author:
#       Derek Vuong (dv)
#   Revision History:
#       Aug-28-26: Started (dv)
#

import sys
from dvutil import DVUtil

accounts = {}
MAX_MODES = 3

class DVAccount:
    def __init__(self, number, name, balance):
        self.m_num = number
        self.m_name = name
        self.m_balance = balance
        
    def deposit(self, num):
        self.m_balance += num
        print(f"Added ${num} to your account.\nBalance is now {self.m_balance}.")

    def withdrawl(self, num):
        if (self.m_balance - num) < 0:
            print("Cannot overdraw from account!")
            return
        self.m_balance += num
        print(f"Withdrew ${num} from your account.\nBalance is now {self.m_balance}.")

    def transfer(self, acc, num):
        # got null account
        if acc is None:
            return
        pass

def write_to_file():
    pass

def add_account():
    num = DVUtil.input_to_int("enter acc no#: ")
    name = input("enter acc name: ")
    balance = DVUtil.input_to_int("enter starting balance: ")

def main():
    modes = (add_account, None, None, None)
    print("welcome to our atm.!")
    while 1:
        mode = DVUtil.input_to_int("Enter mode:\n"
                                   "1. Create Account.\n"
                                   "2. Login.\n"
                                   "2. Deposit.\n"
                                   "3. Withdrawl.\n"
                                   "--> ",)
        if mode > MAX_MODES or mode < 1:
            print("invalid mode given")
            continue
        modes[mode-1]()
        

if __name__ == "__main__":
    main()
