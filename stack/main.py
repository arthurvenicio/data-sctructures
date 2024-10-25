class Stack:
    def __init__(self, max_lenght = 0) -> None:
        self.items = [0]*max_lenght
        self.max_lenght = max_lenght
        self.pointer = 0
        
    def push(self, item):
        self.items[self.pointer] = item
        self.pointer += 1
        
    def pop(self):
        if not len(self.items):
            raise IndexError("Empty list")
        
        item = self.items[-1]
        self.pointer -=1
        return item
    
    def peek(self):
        if not len(self.items):
            raise IndexError("Empty list")
        return self.items[-1]
    
    def size(self):
        return self.pointer