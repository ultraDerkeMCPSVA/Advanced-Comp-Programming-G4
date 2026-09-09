class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

tempList = [(Node(x % 2)) for x in range(0, 16)]
head = None
tail = None


for x in tempList:
    head = x
    head.next = x

#for (ptr = head; ptr != nullptr; ptr = ptr->next)
