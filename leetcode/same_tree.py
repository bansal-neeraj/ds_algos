class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def pre_order(root):
    print(root.val,end=',')
    if root.left:
        pre_order(root.left)
    if root.right:
        pre_order(root.right)


def main():
    p= Node(10)
    p.left =  Node(15)
    p.right =  Node(25)
    p.left.left = Node(100)

    q = Node(10)
    q.left = Node(15)
    q.right = Node(25)
    q.left.left = Node(100)
    # q.left.right = Node(100)
    # p = Node(1)
    # q = Node(1)
    # q.right = Node(2)
    pre_order(p)
    print('next tree')
    pre_order(q)
    print(same_tree(p,q))


def same_tree(p,q):
    if (p and q) and p.val == q.val:
        return same_tree(p.left,q.left) and same_tree(p.right,q.right)
    elif p is None and q is None:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
