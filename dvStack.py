#
#   Name:
#       dvStack.py
#   Purpose:
#       Stack assignment for Advanced Programming G4
#   Author:
#       Derek Vuong (dv)
#   Revisions:
#       Sep-18-26: finished (dv)
#

#
#   what makes object oriented programming truly liberating,
#   is realizing that not everything neccesarily has to
#   be an object. some things are better implemented as
#   globals rather than classes.
#

from dvlib.dvutil import dvUtil
import sys

class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return True if len(self.stack) is 0 else False
    def push(self, new_element):
        self.stack.insert(0, new_element)
    def pop(self):
        if self.is_empty() is False: return self.stack.pop(0)
        else: return None
    def size(self):
        return len(self.stack)
    def peek(self):
        if self.is_empty() is False: return self.stack[0]
        else: return None
    def print_me(self):
        stack_str = ""
        for x in range(0, len(self.stack)):
            stack_str += str(self.stack[x])
            if x < len(self.stack) - 1:
                stack_str += ", "
        return f"stack = [ {stack_str} ]"

global_stack = Stack()

def _push():
    new_element = input("push to stack --> ")
    global_stack.push(new_element)

def _pop():
    popped = global_stack.pop()
    if popped is not None: print(f"popped item \"{popped}\"")
    else: print("can't pop")
    return popped

def _peek():
    peeked = global_stack.peek()
    if peeked is not None: print(f"top of stack is \"{peeked}\"")
    else: print("stack has nothing in it.")

def _isEmpty():
    if global_stack.is_empty(): print("stack is empty")
    else: print("stack is not empty")

def _size():
    print(f"stack has {global_stack.size()} elements")

fnTable = (
    _push,
    _pop,
    _peek,
    _isEmpty,
    _size,
    sys.exit
    )

FUNCTION_COUNT = 6

input_string = (
    "\npress no# to do stack operations\n"
    "1. push\n"
    "2. pop\n"
    "3. peek\n"
    "4. check emptiness\n"
    "5. size\n"
    "6. quit program\n"
    "--> "
    )

def main():
    while (1):
        print(f"\n{global_stack.print_me()}")
        user_input = dvUtil.int_cast(input(input_string)) - 1
        if dvUtil.in_range(user_input, 0, FUNCTION_COUNT): fnTable[user_input]()

if __name__ == "__main__":
    print("welcome to derek's stack program...")
    main()
