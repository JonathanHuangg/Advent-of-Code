from collections import deque

class LinkedList:
    def __init__(self):
        self.head = None 

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def addEnd(self, newData):
        newNode = Node(newData)
        if (len(str(newData)) == 0):
            return
        if self.head is None:
            self.head = newNode
            return
        lastVal = self.head
        while (lastVal.next):
            lastVal = lastVal.next
        lastVal.next = newNode
    
    def __str__(self):
        if self.head is None:
            return "hi"
        lastVal = self.head
        string = ""
        while (lastVal.next):
            string += f"{str(lastVal)} "
            lastVal = lastVal.next
        string += f"{str(lastVal)} "
        return string
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
    
    def __str__(self):
        return f"{self.data}"

file = open("Day5Input.txt", "r")
File = file.readlines()

#input is position where number is
def createList(index):
    list = LinkedList()
    for x in range(8):
        onFile = File[x].strip()
        list.addEnd(Node(onFile[index]))
    return list

indexes = File[8].strip()
stack1 = createList(indexes.index("1") + 1)
stack2 = createList(indexes.index("2") + 1)
stack3 = createList(indexes.index("3") + 1)
print(stack3)


