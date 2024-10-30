class Node:
    def __init__(self, value, next = None, prev = None) -> None:
        self.value  = value
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def addToFront(self, value):
        new_node = Node(value)
        new_node.next = self.head
        
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
            
        self.head = new_node
        
    def addToEnd(self, value):
        new_node = Node(value)
        new_node.next = None
        new_node.prev = self.tail
        
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        
        self.tail = new_node
        
    def popFromFront(self):
        if not self.head:
            return None
        
        curr_value = self.head.value
        
        self.head = self.head.next
        
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
            
        return curr_value
    
    def popFromEnd(self):
        if not self.tail:
             return None
         
        curr_value = self.tail.value
        
        self.tail = self.tail.prev
        
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
            
        return curr_value
    
    def transversal(self):
        current = self.head
        while current is not None:
            
            print(current.value)
            
            current = current.next
        
        print()
    
    
db = DoubleLinkedList()

db.addToFront(3)
db.addToFront(2)
db.addToFront(1)
db.addToEnd(4)
db.addToEnd(5)

db.reverse_traversal()
# db.transversal()
# db.popFromFront()
# db.popFromFront()
# db.popFromFront()
# db.popFromFront()
# db.transversal()
