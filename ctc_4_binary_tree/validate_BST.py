# CTCI 4.5 - check if a binary is a binary search tree or not

from ctc_4_binary_tree.binary_tree_non_search import create_binary_tree,in_order


def validate_bst(root,side):
    """ min max method"""
    if root.left is None and root.right is None:
        return root.value

    left_max, right_min = None,None
    val_list = [root.value]

    if root.left:
        left_max = validate_bst(root.left,'l')
        val_list.append(left_max)

    if root.right:
        right_min = validate_bst(root.right,'r')
        val_list.append(right_min)

    if (left_max and left_max > root.value) or (right_min and right_min < root.value):
            print('not BST')
            # status = False

    if side == 'l':
        return max(val_list)
    if side == 'r':
        return min(val_list)

    return None


if __name__ == '__main__':
    print('ctci')
    root = create_binary_tree()
    in_order(root)
    print('*'*50)
    validate_bst(root,'n')



