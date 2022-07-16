"""SINGLY LINKED LIST """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None
    def append(self, data):
        # If the last node is empty then the last node will be none so in this if statement the head will be created
        if (self.head is None):
            self.head = Node(data)
            self.lastNode = self.head
        else:
            self.lastNode.next = Node(data)
            self.lastNode = self.lastNode.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        print()

if __name__ == "__main__":
    L = LinkedList()
    
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    L.display()
    

"""DOUBLY LINKED LIST """