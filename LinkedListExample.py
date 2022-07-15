
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

# Linked List class

# Function to initiailse the list object
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        para = self.head
        while (para):
            print(para.data)
            para = para.next # make sure to reasign para to avoid infinte loop

if __name__=="__main__":
    
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third

    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
    
    lList = LinkedList()
    lList.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    lList.head.next = second
    second.next = third
    
    lList.printList()
    
