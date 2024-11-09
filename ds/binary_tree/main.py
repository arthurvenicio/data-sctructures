from collections import deque


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insert_recursive(val, self.root)

    def __insert_recursive(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.__insert_recursive(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.__insert_recursive(val, node.right)
                
    def search(self, val):
        return self.__search_recursive(self.root, val)
    
    def __search_recursive(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self.__search_recursive(node.left, val)
        else:
            return self.__search_recursive(node.right, val)
        
    def preorder_traversal(self):
        result = []
        self.__preorder_traversal_recursive(self.root, result)
        return result
    
    def __preorder_traversal_recursive(self, node, result):
        if node:
            result.append(node.val)
            self.__preorder_traversal_recursive(node.left, result)
            self.__preorder_traversal_recursive(node.right, result)
            
    def inorder_traversal(self):
        result = []
        self.__inorder_traversal_recursive(self.root, result)
        return result
    
    def __inorder_traversal_recursive(self, node, result):
        if node:
            self.__inorder_traversal_recursive(node.left, result)
            result.append(node.val)
            self.__inorder_traversal_recursive(node.right, result)
            
    def postorder_traversal(self):
        result = []
        self.__postorder_traversal_recursive(self.root, result)
        return result
    
    def __postorder_traversal_recursive(self, node, result):
        if node:
            self.__postorder_traversal_recursive(node.left, result)
            self.__postorder_traversal_recursive(node.right, result)
            result.append(node.val)
            
    def bfs(self, val):
        if self.root is None:
            return False
        
        queue = deque()
        queue.append(self.root)
        
        while queue:
            node = queue.popleft()
            print(node.val)
            if node.val == val:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
            

# Create a binary tree
tree = BinaryTree()

# Insert nodes
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(9)
tree.insert(19)

# Search for a value
# print(tree.search(17))
# print(tree.preorder_traversal())
# print(tree.inorder_traversal())
# print(tree.postorder_traversal())
print(tree.bfs(19))