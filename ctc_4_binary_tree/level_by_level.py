from collections import deque

class Node:
    def __init__(self,x):
        self.x = x
        self.left = None
        self.right = None

#
# root = Node(3)
# root.left = Node(9)
# root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)


root = None
q = deque()
q.append(root)
result = []
while q:
    tmp_level = []
    queue_level = deque()
    while q:
        x = q.popleft()
        tmp_level.append(x.x)
        if x.left:
            queue_level.append(x.left)
        if x.right:
            queue_level.append(x.right)

    result.append(tmp_level)
    if queue_level:
        q = queue_level


print(result)


