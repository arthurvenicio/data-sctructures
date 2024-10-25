class Stack:
    def __init__(self) -> None:
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not len(self.items):
            raise IndexError("Empty list")
        
        return self.items.pop()
    
    def peek(self):
        if not len(self.items):
            raise IndexError("Empty list")
        return self.items[-1]
    
    def size(self):
        return len(self.items)