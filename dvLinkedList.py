#
#   Name:
#       dvLinkedList.py
#   Purpose:
#       Linked List assignment for Advanced Programming G4
#   Author:
#       Derek Vuong (dv)
#   Revision History:
#       Sep-14-26: finished this assignment. could i have formatted
#       and commented this a bit better? perhaps. hehehe (dv)
#


from dvlib.dvutil import dvUtil

class Node:
    def __init__(this, data):
        this.data = data
        this.next = None

class LinkedList:
    def __init__(this):
        this.m_head = None

    def display(this):
        tempString = "list = "
        tempNode = this.m_head
        while tempNode is not None:
            tempString += f"{tempNode.data}"
            tempNode = tempNode.next
            if tempNode is not None:
                tempString += ", "
        print(tempString)
        
    def append(this, data):
        newNode, tempNode, tempHead = Node(data), this.m_head, None
        print(f"added node with data \'{data}\' to linked list.")

        if this.m_head is None:
            this.m_head = newNode
            return

        while tempNode is not None:
            if tempHead is None:
                # set temp head ptr to new head
                # node
                tempHead = tempNode
            if tempNode.next is None:
                # assign new node to the end of the
                # linked list
                tempNode.next = newNode
                break
            tempNode = tempNode.next # go through next
        this.m_head = tempHead # assign the newly linked head to this.m_head

    def prepend(this, data):
        print(f"added node with data \'{data}\' to linked list.")
        newNode = Node(data)
        newNode.next = this.m_head
        this.m_head = newNode

    def remove(this, data):
        tempHead, tempTail, tempNext, tempNode = None, None, None, this.m_head
        removed = False

        # rebuild linked list to exclude the node(s) that
        # has data we don't want
        
        while tempNode is not None:
            tempNext = tempNode.next
            tempNode.next = None
            
            if tempNode.data != data:
                if tempHead is None:
                    tempHead = tempTail = tempNode
                else:
                    tempTail.next = tempNode
                    tempTail = tempNode
            else:
                removed = True
                
            tempNode = tempNext
        this.m_head = tempHead

        if removed:
            print(f"succesfully removed element with data \'{data}\'")
        else:
            print(f"element with data \'{data}\' does not exist in linked list")

class dvInterface:
    m_list = LinkedList()
    m_interfaceString = str(
        "enter no# of operation you'd like to do.\n"
        "1. append\n"
        "2. prepend\n"
        "3. remove\n"
        "4. display\n"
        "--> "
    )
    
    def __init__(this):
        pass

    # wrappers for some interface stuff
    def interface_append(this):
        data = input("append --> ")
        this.m_list.append(data)

    def interface_prepend(this):
        data = input("prepend --> ")
        this.m_list.prepend(data)

    def interface_remove(this):
        data = input("remove --> ")
        this.m_list.remove(data)

    def interface_display(this):
        this.m_list.display()

    # function ptr table
    m_fnTable = (
        interface_append,
        interface_prepend,
        interface_remove,
        interface_display
    )

    def draw(this):
        selection = dvUtil.input_to_int(this.m_interfaceString) - 1
        if dvUtil.in_range(selection, 0, 3):
            this.m_fnTable[selection](this)
        else:
            print("invalid mode selected!")
        

# create interface object
interface = dvInterface()

if __name__ is "__main__":
    print("welcome to derek's linked list tool\n", end="")
    while 1:
        interface.draw()
