class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        
        
class Stack:
    def __init__(self) -> None:
        self.head = None
        self._size = 0
        
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        
    def pop(self):
        if self._size == 0:
            raise IndexError("Empty stack")
        
        popped_node = self.head
        self.head = popped_node.next
        self._size -= 1
        return popped_node.val
    
    
    def is_empty(self):
        return self._size == 0
    
    def peek(self):
        if self._size == 0:
            raise IndexError("Empty stack")
        
        
        return self.head.val
    
    def size(self):
        return self._size
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.peek())
print(stack.size())
print(stack.is_empty())
