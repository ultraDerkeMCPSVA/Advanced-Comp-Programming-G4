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

class dvUtil:
    #
    #   int_cast
    #   Safe version of performing int(x)
    #
    
    @staticmethod
    def int_cast(x):
        try:
            return int(x)
        except:
            print("expected integer! aborting!")
            sys.exit()
            return None
    #
    #   input_to_int
    #   Safe version of performing int(input(x))
    #
    
    @staticmethod
    def input_to_int(x):
        try:
            return int(input(x))
        except:
            print("expected integer! aborting!")
            sys.exit()
            return None

    @staticmethod
    def tokenize(x):
        pass
