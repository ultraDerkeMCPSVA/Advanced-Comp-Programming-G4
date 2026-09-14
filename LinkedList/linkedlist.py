class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

tempList = [(Node(x)) for x in range(0, 16)]
head = None
tail = None


for x in tempList:

    print(x.data)
    if (x.data % 2) == 0:
        if head == None:
            head = x
        else:
            head = head.next
        head.next = x

ptr = head
while ptr != None:
    print(ptr.data)
    ptr = ptr.next

#for (ptr = head; ptr != nullptr; ptr = ptr->next)
