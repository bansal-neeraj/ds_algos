# ctci 4.8

from ctc_4_binary_tree.binary_tree_non_search import create_binary_tree,in_order

def srh2(root,n1,n2):
    other_node = None
    if root.value == n1:
        ancestor = srh_2_sub(root.left,n2) or srh_2_sub(root.right,n2)
        if ancestor:
            return root,n2
        else:
            return None, n2

    if root.value == n2:
        ancestor = srh_2_sub(root.left, n1) or srh_2_sub(root.right, n1)
        if ancestor:
            return root, n1
        else:
            return None, n1

    if root.left:
        ancestor, other_node = srh2(root.left,n1,n2)
        if ancestor:
            return ancestor,other_node
        elif other_node and root.right:
            status = srh_2_sub(root.right,other_node)
            if status:
                return root,other_node

    if root.right:
        ancestor, other_node = srh2(root.right, n1, n2)
        if ancestor:
            return ancestor, other_node
        elif other_node and root.left:
            status = srh_2_sub(root.left, other_node)
            if status:
                return root, other_node

    return None,other_node


def srh_2_sub(r,other_node):
    if r is None:
        return False

    if r.value == other_node:
        return True
    if r.left:
        status = srh_2_sub(r.left,other_node)
        if status:
            return True
    if r.right:
        status = srh_2_sub(r.right, other_node)
        if status:
            return True
    return False


def method3(root,n1,n2):
    if root is None:
        return None

    if root.value == n1 or root.value == n2:
        return root

    left = method3(root.left,n1,n2)
    right = method3(root.right,n1,n2)

    if left and right:
        return root
    elif not left:
        return right
    elif not right:
        return left


if __name__ == '__main__':
    print('ctci 4.8')
    root = create_binary_tree()
    in_order(root)
    print('result')
    ancestor,other_node = srh2(root,20,7)
    print('ancestor is - ',ancestor.value)

    print('method 3')
    new_ancestor = method3(root,20,7)
    print(new_ancestor.value)



