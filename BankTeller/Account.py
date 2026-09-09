#
#   Name:
#       Account.py
#   Author:
#       Derek Vuong (dv)
#   Revision History:
#       Sep-03-26: Moved out of Teller.py for organization reasons.
#       (dv)
#

from dvutil import dvUtil

#   Pointer to external dictionary that will be used for
#   account checking.
reg_dict = None

#
#   Name:
#       check_for_account
#   Description:
#       check to see if the given account_id has an associated
#       account tied to it.
#   Input:
#       account_id (string)
#   Output:
#       pointer to account if it exists. otherwise return null.
#

def check_for_account(account_id):
    if reg_dict == None:
        print("MUST SET Account.reg_dict to perform account checking!!!")
        return None
    if account_id in reg_dict:
        return reg_dict[account_id]
    return None

class dvAccount:
    def __init__(self, number, name, balance):
        self.m_num = number
        self.m_name = name
        self.m_balance = balance
        
    def deposit(self):
        num = dvUtil.input_to_float("Enter how much you would like to deposit\n"
                                  "into your account\n"
                                  "--> ")
        self.m_balance += num
        print(f"\nAdded ${num} to your account.\nBalance is now ${self.m_balance:.2f}.\n")

    def withdraw(self):
        num = dvUtil.input_to_float("Enter how much you would like to withdraw\n"
                                  "from your account\n"
                                  "--> ")
        
        if (self.m_balance - num) < 0:
            print("\nCannot overdraw from account!\n")
            return
        
        self.m_balance -= num
        print(f"\nWithdrew ${num} from your account.\nBalance is now ${self.m_balance:.2f}.\n")

    def transfer(self):
        acc = check_for_account(input("Enter account id to transfer into\n"
                                      "--> "))
        if acc is None: # got null
            print("Given account id does not exist.")
            return

        num = dvUtil.input_to_float("Enter how much you would like to transfer\n"
                                  f"into {acc.m_name}'s account\n"
                                  "--> ")
        
        if (self.m_balance - num) < 0:
            print("\nCannot overdraw from account!\n")
            return

        self.m_balance, acc.m_balance = self.m_balance - num, acc.m_balance - num
        print(f"\nSuccesfully Transfered ${num:.2f} from your account\n"
              f"into {acc.m_name}'s account.\n")
