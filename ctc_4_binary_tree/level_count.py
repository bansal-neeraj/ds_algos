"""
count levels in a binary tree
"""


class Node:
    def __init__(self,x):
        self.x = x
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)
root.right.left = Node(50)

root.right.left.right = Node(60)


def level_count(r):
    if not r:
        return 0
    return max(level_count(r.left), level_count(r.right)) + 1


print(level_count(root))




