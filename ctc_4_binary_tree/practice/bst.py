# practcie creating a binary tree and various traversal

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def add_node(root,x):

    if x < root.value:
        if root.left:
            add_node(root.left, x)
        else:
            root.left = Node(x)
    else:
        if root.right:
            add_node(root.right,x)
        else:
            root.right = Node(x)


def in_order(root):
    if root.left:
        in_order(root.left)
    print(root.value,end=',')
    if root.right:
        in_order(root.right)


def pre_order(root):
    print(root.value, end=',')
    if root.left:
        pre_order(root.left)

    if root.right:
        pre_order(root.right)

def post_order(root):

    if root.left:
        post_order(root.left)

    if root.right:
        post_order(root.right)
    print(root.value, end=',')

root = Node(15)
add_node(root,12)
add_node(root,7)
add_node(root,14)
add_node(root,27)
add_node(root,20)
add_node(root,88)
add_node(root,23)

in_order(root)
print()
pre_order(root)
print()
post_order(root)
# 7,12,14,15,20,23,27,88,
# 15,12,7,14,27,20,23,88,
# 7,14,12,23,20,88,27,15,

#7,12,14,15,20,23,27,88,
# 15,7,12,14,20,23,27,88,
# 7,12,14,20,23,27,88,15,