class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, newData):
        #  Allocate the node and put it in the data
        newNode = Node(newData)
        
        # Make the next of the new Node the head
        newNode.next = self.head
        
        # Move the node to point to the new head
        self.head = newNode
        
    def inplace(self, prevNode, newNode):
        
        if prevNode is None:
            print('Select Node in LinkedList')
            return 
        
        newNode = Node(newNode)
        
        newNode.next = prevNode.next
        
        prevNode.next = newNode
        
        
    def printlist(self):
        para = self.head
        while (para):
            print(para.data)
            para = para.next
    
    def atEnd(self,newNode):
        newNode = Node(newNode)
        
        last = self.head
        
        # While loop will break when last has no next
        while (last.next):
            last = last.next
        
        # Set the last pointer to the new Node 
        last.next = newNode
    
# Creating the List 
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

#Pointers 
llist.head.next = second
second.next = third

llist.atEnd(4)
llist.printlist()