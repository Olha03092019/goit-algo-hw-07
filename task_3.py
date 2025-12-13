from node import Node, insert
from avl_node import AVLNode, insert_avl

def sum_values(root):
    if root is None:
        return 0
    return root.val + sum_values(root.left) + sum_values(root.right)

def sum_avl_values(root):
    if root is None:
        return 0
    return root.key + sum_avl_values(root.left) + sum_avl_values(root.right)

if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    root = insert(root, 1)
    print(f"Sum of values of the binary tree : " + str(sum_values(root)))

    root = AVLNode(5)
    root = insert_avl(root, 3)
    root = insert_avl(root, 2)
    root = insert_avl(root, 4)
    root = insert_avl(root, 7)
    root = insert_avl(root, 6)
    root = insert_avl(root, 8)
    root = insert_avl(root, 1)
    print(f"Sum of values of the avl tree : "+str(sum_avl_values(root)))

