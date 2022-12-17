# ctc 4.10 ,

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root):
    if root.left:
        inorder(root.left)
    print(root.value,end=',')

    if root.right:
        inorder(root.right)


def srh_main(t1,t2):
    """search root of sub tree in main tree and return the node of main tree that matches subtree root"""
    if t1 is None:
        return None
    if t1.value == t2.value:
        return t1

    return srh_main(t1.left,t2) or srh_main(t1.right, t2)


def check_sub_tree(m_tree,sub_tree):
    if m_tree is None and sub_tree is None:
        return True
    if m_tree is None or sub_tree is None:
        return False
    if m_tree.value != sub_tree.value:
        return False
    return check_sub_tree(m_tree.left,sub_tree.left) and check_sub_tree(m_tree.right,sub_tree.right)


if __name__ == '__main__':
    # main tree

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(12)
    root.right.right.left = Node(15)
    root.left.left = Node(4)
    root.left.left.left = Node(11)
    root.left.right = Node(10)

    inorder(root)

    # create sub tree to search in the main tree
    root2 = Node(3)
    root2.right = Node(12)
    root2.right.left = Node(15)
    print()
    print('sub tree')
    inorder(root2)
    # print()
    # print('node in main tree')
    main_tree_node = srh_main(root,root2)
    # if main_tree_node:
    #     print(main_tree_node.value)
    # else:
    #     print('not found')

    found = check_sub_tree(main_tree_node,root2)
    if found:
        print('sub tree exista')
    else:
        print('sub tree does not exists')

