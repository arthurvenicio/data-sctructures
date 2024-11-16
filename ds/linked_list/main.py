class Node:
    def __init__(self, value, next = None) -> None:
        self.value  = value
        self.next = next
        
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def addToFront(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def addToEnd(self, value):
        new_node = Node(value)
        
        if self.head:
            current = self.head
                
            while current.next is not None:
                current = current.next
                
            current.next = new_node
        else:
            self.head = new_node
        
        
    def popFromFront(self):
        if not self.head:
            return None
        
        curr_value = self.head.value
        
        self.head = self.head.next
        
        return curr_value
    
    def popFromEnd(self):
        if not self.tail:
             return None
         
        curr_value = self.tail.value
        
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
    

    
    
linked_list = LinkedList()

linked_list.addToEnd(2)
linked_list.addToFront(3)
linked_list.transversal()


# print(linked_list.popFromFront())