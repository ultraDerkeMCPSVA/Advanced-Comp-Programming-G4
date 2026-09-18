#   derek's external file syntax!!!
#
#   account_name
#   {
#       number = 000-001;
#       balance = 20;
#   }
#

from dvutil.dvlib import dvUtil
from random import randint

class dvAccount:
    def __init__(name, password, balance,):
        self.m_name = name
        self.m_password = password
        self.m_balance = balance

class dvTeller:
    accounts = {"999-999" : dvAccount("Dummy", "pickles", 999_999.00)}
    account = None
    
    def load_file(self):
        pass
    
    def __init__(self):
        pass

    def write_to_file(self):
        pass

    def generate_id(self):
        id_array = [None] * 6 # best way to get fixed size arrays
        # ids are formatted as: xxx-xxx
        while 1:
            for x in range(0, 6): id_array[x] = randint(0, 9)

    def sign_up(self):
        name = input("username --> ")
        password = input("password --> ")
        balance = float(input("starting balance --> "))
        
