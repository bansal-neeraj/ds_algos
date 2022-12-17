# create a binary tree that is not a Binary Search Tree

class Node:
    # value = None
    # left = None
    # right = None

    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None

def in_order(root):
    """visit left then current node and then right node"""

    if root.left:
        in_order(root.left)
    print(root.value,end=',')
    if root.right:
        in_order(root.right)


def create_binary_tree():
    """create a non binary search tree"""
    # root = Node(10)
    # left_node = Node(5)
    #
    # root.left = left_node
    # left_node.left = Node(3)
    # left_node.left.left = Node(7)
    # left_node.left.left.right = Node(14)
    #
    # left_node.right = Node(9)
    # left_node.right.right = Node(11)
    # # left_node.left.right = Node(9)
    #
    # right_node = Node(12)
    # # right_node.left = Node(11)
    # right_node.right = Node(20)
    # root.right = right_node
    # right_node.right.left = Node(15)

    # root = Node(1)
    # right_node =Node(5)
    # root.right = right_node
    # left_node = Node(2)
    # root.left = left_node
    #
    # left_node.left = Node(3)
    # left_node.right = Node(4)

    root = Node(20)
    left_node = Node(10)
    right_node = Node(30)

    root.left = left_node
    root.right = right_node

    left_node.left = Node(5)
    left_node.left.left = Node(3)
    left_node.left.right = Node(7)

    left_node.right = Node(15)
    left_node.right.right = Node(17)

    return root


if __name__== '__main__':
    root = create_binary_tree()
    in_order(root)

