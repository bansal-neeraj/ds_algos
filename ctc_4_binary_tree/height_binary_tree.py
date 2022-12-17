# to calculate height of binary tree and also identify if the tree is balanced  - CTCI 4.4

from ctc_4_binary_tree.binarytree import Node


def main():
    """create a binary tree"""
    root = Node(10)
    root.add_node(5)
    root.add_node(12)
    root.add_node(20)
    root.add_node(3)
    root.add_node(7)
    root.add_node(15)

    root.in_order()
    return root


def binary_tree_height(root):
    # print('height')
    if root.left is None and root.right is None:
        return 1,True
    else:
        left_height, right_height = 0, 0
        if root.left:
            left_height,balance_status = binary_tree_height(root.left)
        if root.right:
            right_height,balance_status = binary_tree_height(root.right)

        if balance_status:  # if the tree is balanced till now, only then check else if unbalanced , no need to check.
            if abs(right_height - left_height) > 1:
                balance_status = False  # unbalanced
            else:
                balance_status = True  # balanced

        height = 1 + (right_height if right_height > left_height else left_height)
        return height,balance_status


if __name__ == '__main__':
    tree_root = main()
    print()
    print(f'heigh is {binary_tree_height(tree_root)}')
