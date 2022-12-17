# create a binary search tree from an array sorted in ascending order

from ctc_4_binary_tree.binarytree import Node

arr = [10,22,23,44,58,60,71,88,91,100]


def create_tree(a):
    if len(a) == 1:
        new_node = Node(a[0])
        return new_node
    elif len(a) == 2:
        left = Node(a[0])
        root = Node(a[1])
        root.left = left
        return root
    else:
        midpoint = len(a)//2
        root = Node(a[midpoint])
        let_side = a[0:midpoint]
        right_side = a[midpoint+1:]
        root.left = create_tree(let_side)
        root.right = create_tree(right_side)
        return root


def main():
    my_binary_srh_tree = create_tree(arr)
    my_binary_srh_tree.in_order()


if __name__ == '__main__':
    main()
