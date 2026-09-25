#
#   Name:
#       dvutil.py
#   Purpose:
#       My personal Python utility library.
#   Author:
#       Derek Vuong (dv)
#   Revision History:
#       Aug-28-26: Started (dv)
#       Sep-25-26: Removed redundant functions. Added tokenize. (dv)
#

import sys

def exit_message(message):
    print(message)
    sys.exit()

class dvUtil:
    special_chars = (
            "\t",
            " ",
            "\n",
            "\b"
        )
    
    #
    #   tokenize
    #   Try stripping words from a string. If we can extract a word,
    #   exit loop and return extracted word + sliced string w/out extracted
    #   word.
    #
    @staticmethod
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
