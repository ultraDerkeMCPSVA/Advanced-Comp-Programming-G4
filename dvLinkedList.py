#
#   Name:
#       dvLinkedList.py
#   Purpose:
#       Linked List assignment for Advanced Programming G4
#   Author:
#       Derek Vuong (dv)
#   Revision History:
#       Sep-14-26: finished this assignment. could i have formatted
#       and commented this a bit better? perhaps. hehehe. (dv)
#           micro update - simplified append implementation!!!!
#
#       Sep-16-26: cleaned up my impl. of append and remove linkedlist
#       functions. also added some more comments to the code to clear up
#       stuff... (derek)
#


from dvlib.dvutil import dvUtil

class Node:
    #
    #   __init__
    #   Constructor
    # 
    def __init__(this, data):
        this.data = data
        this.next = None

class LinkedList:
    #
    #   __init__
    #   Constructor
    #
    def __init__(this):
        this.m_head = None

    #
    #   display
    #   Print linked list.
    #
    def display(this):
        tempString = "list = "
        tempNode = this.m_head
        while tempNode is not None:
            tempString += f"{tempNode.data}"
            tempNode = tempNode.next
            if tempNode is not None:
                tempString += ", "
        print(tempString)

    #
    #   append
    #   Add new element to linked list.
    #
    def append(this, data):
        newNode, tempNode = Node(data), this.m_head
        print(f"added node with data \'{data}\' to linked list.")

        if this.m_head is None:
            this.m_head = newNode
            return
        
        this.m_head = tempNode
        while tempNode is not None:
            if tempNode.next is None:
                tempNode.next = newNode
                break
            tempNode = tempNode.next # go through next
            
    #
    #   prepend
    #   Add new element to the start of a linked list.
    #
    def prepend(this, data):
        print(f"added node with data \'{data}\' to linked list.")
        newNode = Node(data)
        newNode.next = this.m_head
        this.m_head = newNode
        
    #
    #   remove
    #   Remove one instance of the given unwanted data from
    #   the linked list.
    #
    def remove(this, data):
        removed, tempTail, tempNext, tempNode = False, None, None, this.m_head

        # rebuild linked list to exclude the node(s) that
        # has data we don't want.
        
        this.m_head = None
        
        while tempNode is not None:
            tempNext = tempNode.next
            tempNode.next = None
            
            # relink the head of the linked list if we have
            # already removed the desired element or the node's
            # data is not that of our unwanted element.
            
            if removed is True or tempNode.data != data:
                if this.m_head is None:
                    this.m_head = tempTail = tempNode
                else:
                    tempTail.next = tempNode
                    tempTail = tempNode
            else:
                removed = True
            tempNode = tempNext

        if removed: print(f"succesfully removed element with data \'{data}\'")
        else: print(f"element with data \'{data}\' does not exist in linked list")

class dvInterface:
    #   Linked list object.
    m_list = LinkedList()

    #   Const. interface string.
    m_interfaceString = str(
        "enter no# of operation you'd like to do.\n"
        "1. append\n"
        "2. prepend\n"
        "3. remove\n"
        "4. display\n"
        "--> "
    )
    
    #
    #   __init__
    #   Constructor
    # 
    def __init__(this):
        pass

    #   Wrappers for linked list methods.
    
    #
    #   interface_append
    #
    def interface_append(this):
        data = input("append --> ")
        this.m_list.append(data)

    #
    #   interface_prepend
    #
    def interface_prepend(this):
        data = input("prepend --> ")
        this.m_list.prepend(data)

    #
    #   interface_remove
    #
    def interface_remove(this):
        data = input("remove --> ")
        this.m_list.remove(data)

    #
    #   interface_display
    #
    def interface_display(this):
        this.m_list.display()

    #   Function pointer table.
    m_fnTable = (
        interface_append,
        interface_prepend,
        interface_remove,
        interface_display
    )

    #
    #   draw
    #   Print basic interface.
    #
    def draw(this):
        selection = dvUtil.input_to_int(this.m_interfaceString) - 1
        if dvUtil.in_range(selection, 0, 3):
            this.m_fnTable[selection](this)
        else:
            print("invalid mode selected!")
        

#   Create global interface object.
interface = dvInterface()

if __name__ is "__main__":
    print("welcome to derek's linked list tool\n", end="")
    while 1:
        interface.draw()
