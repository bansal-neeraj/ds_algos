# find out if a binary is balanced or not

class Node:
    def __init__(self,x):
        self.x = x
        self.left = None
        self.right = None


def height_binary_tree(root):
    if root is None:
        return 0
    else:
        return 1 + max(height_binary_tree(root.left) , height_binary_tree(root.right))


def check_if_balanced(root):
    if root is None:
        return 0,True
    else:
        l_height,l_status = check_if_balanced(root.left)
        r_height, r_status = check_if_balanced(root.right)
        if l_status and r_status:
            balanced = True if 0 <= abs(l_height - r_height) <= 1 else False
        else:
            balanced = False

        return 1 + max(l_height, r_height), balanced


def main():
    # root = Node(10)
    # root.left = Node(20)
    # root.right = Node(30)
    # root.left.left = Node(40)
    # root.left.right = Node(50)
    # root.left.right.right = Node(60)

    # root = Node(3)
    # root.left = Node(9)
    # root.right = Node(20)
    # root.right.left = Node(15)
    # root.right.right = Node(7)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(3)
    root.left.left.left = Node(4)
    root.left.left.right = Node(4)


    print(f'{height_binary_tree(root)=}')
    print(f'{check_if_balanced(root)=}')


if __name__ == '__main__':
    main()
