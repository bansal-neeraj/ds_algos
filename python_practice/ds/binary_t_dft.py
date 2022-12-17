# Binary tree Depth First Traversal using recursion and stack
from collections import deque

class Node:
    def __init__(self,x):
        self.x = x
        self.left = None
        self.right = None


def main():
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.right = Node('f')
    root.left.left.left = Node(1)
    root.left.right.right = Node(2)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)

    arr = []
    dft_recursion(root,arr)
    print(f'recursion {arr=}')
    print('using stack')
    dft_stack(root)
    print('')
    print(f'breadth first or levelwise traversal - loop {bft_loop(root)=}')
    print(''*10)
    print(f'breadth first or levelwise traversal - deque')
    bft_queue(root)
    print('level by level traversal')
    print(level_by_level(root))


def dft_recursion(root,arr):
    """dft or pre-order using recursion"""
    if root:
        arr.append(root.x)
    else:
        return

    dft_recursion(root.left,arr)
    dft_recursion(root.right, arr)


def dft_stack(root):
    """dft or pre-order using stack"""
    my_stack = [root]
    while my_stack:
        n = my_stack.pop()
        print(n.x,end=',')
        if n.right:
            my_stack.append(n.right)
        if n.left:
            my_stack.append(n.left)


def level_by_level(root):
    level = []
    my_q = deque()
    my_q.append(root)
    while my_q:
        r = my_q.popleft()
        level.append(r.x)
        if r.left:
            my_q.append(r.left)
        if r.right:
            my_q.append(r.right)

    return level



def bft_loop(root):
    """bft using loop"""
    if root:
        arr = [root.x]
    else:
        return []

    children = [root.left,root.right]
    while children:
        tmp_child = []
        for i in children:
            if i:
                arr.append(i.x)
                tmp_child.append(i.left)
                tmp_child.append(i.right)
        children = tmp_child

    return arr


def bft_queue(root):
    my_queue = deque()
    my_queue.appendleft(root)
    while my_queue:
        n = my_queue.pop()
        print(n.x,end=',')
        if n.left:
            my_queue.appendleft(n.left)
        if n.right:
            my_queue.appendleft(n.right)


def bft_recursion(root):
    """not working """
    if not root:
        return []
    else:
        return [root.x] + bft_recursion(root.left) + bft_recursion(root.right)


if __name__ == '__main__':
    main()
