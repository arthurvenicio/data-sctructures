class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, val):
        self.items.append(val)
        print("Item is queued")
    
    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    
queue = Queue()

queue.enqueue(1)
print("Dequeue value is: " + f"{queue.dequeue()}")