from collections import deque

class LinkedList:
    def __init__(self):
        self.head = None 

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node
    

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data

    


file = open("Day5Input.txt", "r")
File = file.readlines()

#input is position where number is
def createList(index):
    list = LinkedList()
    for x in range(8):
        onFile = File[x].strip()
        if (x == 0):
            list.head = Node(onFile[index])
        else:
            node = Node(onFile[index])
            list.head.next = node
    return list
list = createList(1)
for x in list:
    print(x)
