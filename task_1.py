from node import Node, insert
from avl_node import AVLNode, insert_avl

def search_max_value(root):
    if root is None:
        return root
    return max_value_node(root).val

def search_avl_max_value(root):
    if root is None:
        return root
    return max_value_node(root).key

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    root = insert(root, 1)
    print(f"Maximum value in the binary tree : "+str(search_max_value(root)))

    root = AVLNode(15)
    root = insert_avl(root, 13)
    root = insert_avl(root, 12)
    root = insert_avl(root, 14)
    root = insert_avl(root, 17)
    root = insert_avl(root, 16)
    root = insert_avl(root, 18)
    root = insert_avl(root, 11)
    print(f"Maximum value in the avl tree : "+str(search_avl_max_value(root)))

