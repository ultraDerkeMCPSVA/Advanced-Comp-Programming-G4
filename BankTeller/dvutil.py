#
#   Name:
#       dvutil.py
#   Purpose:
#       My personal Python utility library.
#   Author:
#       Derek Vuong (dv)
#   Revision History:
#       Aug-28-26: Started (dv)
#

import sys

def exit_message(message):
    print(message)
    sys.exit()

class dvUtil:
    #
    #   int_cast
    #   Safe version of performing int(x)
    #
    
    @staticmethod
    def int_cast(x, exit_on_error = True):
        try:
            return int(x)
        except:
            if exit_on_error: exit_message(f"Expected integer but got {type(x)}!")
            return None
    #
    #   input_to_int
    #   Safe version of performing int(input(x))
    #
    
    @staticmethod
    def input_to_int(x, exit_on_error = True):
        try:
            return int(input(x))
        except:
            if exit_on_error: exit_message(f"Expected integer but got {type(x)}!")
            return None

    #
    #   input_to_float
    #   Safe version of performing int(input(x))
    #
    
    @staticmethod
    def input_to_float(x, exit_on_error = True):
        try:
            return float(input(x))
        except:
            if exit_on_error: exit_message(f"Expected float but got {type(x)}!")
            return None

    #   TODO!!!
    @staticmethod
    def tokenize(x):
        pass
