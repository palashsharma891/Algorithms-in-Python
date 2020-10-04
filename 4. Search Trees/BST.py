class Node:
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        

def inorder_traversal(root):
    if root is not None:
        # Traverse left
        inorder_traversal(root.left)

        # Traverse root
        print(str(root.key) + "->", end=' ')

        # Traverse right
        inorder_traversal(root.right)
        
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def MinValueNode(node):
    current = node
    
    while(current.left is not None):
        current = current.left
        
    return current

def delete(root, key):
    
    if root is None:
        return root
    
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = MinValueNode(root.right)
        
        root.key = temp.key
        
        root.right = delete(root.right, temp.key)
        
    return root
        
root = None
root = insert(root, 69)
root = insert(root, 6969)
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 6)

print("Inorder traversal of BST: ")
inorder_traversal(root)

print("\nDelete 6")
root = delete(root, 6)
print("Inorder traversal of BST: ")
inorder_traversal(root)
