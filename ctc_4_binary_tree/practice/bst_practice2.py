# Binary Tree traversal - inorder , via recursion and iteration
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    """using recursion"""
    if not root:
        return []
    else:
        return inorder(root.left) + [root.val] + inorder(root.right)


def in_order_iteration(root):
    """using iteration"""
    s = []
    output = []
    while root:
        s.append(root)
        if root.left:
            root = root.left
            continue
        else:
            current_node = s.pop()
            output.append(current_node.val)
            while not current_node.right:
                if s:
                    current_node = s.pop()
                    output.append(current_node.val)
                else:
                    break
            root = current_node.right

    return output


def main():
    # root = Node(8)
    # root.left = Node(4)
    # root.right = Node(10)
    # root.left.left = Node(2)
    # root.left.right = Node(6)
    # root.right.right = Node(20)

    root = Node(10)
    root.left = Node(7)
    root.left.right = Node(9)
    root.left.right.left = Node(8)
    root.left.left = Node(6)
    root.left.left.left = Node(5)

    print(f'{inorder.__doc__} {inorder(root)}')
    print(f'{in_order_iteration.__doc__} {in_order_iteration(root)}')
    # print(help(inorder))
    # print(dir(inorder))
    # print(inorder(root))


if __name__ == '__main__':
    main()



