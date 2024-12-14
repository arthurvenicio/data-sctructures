class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, val):
        new_node = Node(val)
        if not self.head:
            head = new_node
        else:
            head.next = new_node
            
        print("Item is queued")
    
    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    

# This code doesnt works yet
    
    
queue = Queue()

queue.enqueue(1)
print("Dequeue value is: " + f"{queue.dequeue()}")