# ctci 4.6 find the successor of nodde in in order traversal

from ctc_4_binary_tree.binarytree import Node


def create_bst():
    root = Node(15)
    root.add_node(12)
    root.add_node(7)
    root.add_node(14)
    root.add_node(27)
    root.add_node(20)
    root.add_node(88)
    root.add_node(23)

    return root


def find_successor(local_root,n):
    # print(local_root.value)
    if local_root.left:
        status = find_successor(local_root.left,n)
        if status:
            print('successor is', local_root.value)
            return False

    # print(local_root.value,end=',')
    if local_root.value == n:

        if local_root.right:
            right_tree,successor = local_root.right,None
            while right_tree:
                successor = right_tree.value
                right_tree = right_tree.left

            print('successor is',successor)
        else:

            return True

    if local_root.right:
        status = find_successor(local_root.right,n)
        return status


if __name__ == '__main__':
    root = create_bst()
    root.in_order()
    print()
    find_successor(root,27)
