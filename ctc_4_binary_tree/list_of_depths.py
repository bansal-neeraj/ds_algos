# ctc 4.3
# given a binary tree design an algorithm which creates a linked list or a list of all nodes at each depth

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


def list_depths(root):
    """create a list of nodes at each depth, using depth first traversal"""
    level_list = [root]
    level = 1
    level_dict = {}
    while level_list:
        level_dict[level] = []
        for i in level_list:
            level_dict[level].append(i)
        level_list.clear()
        for j in level_dict[level]:
            if j.left:
                level_list.append(j.left)
            if j.right:
                level_list.append(j.right)

        level += 1

    return level_dict


def pre_order_list_depth(root,level):
    """preorder - visit current node before child nodes, using pre0rder to identify nodes at each level"""
    if level not in pre_level_dict:
        pre_level_dict[level] = []
    pre_level_dict[level].append(root.value)

    local_root = root
    if local_root.left:
        pre_order_list_depth(local_root.left,level+1)

    if local_root.right:
        pre_order_list_depth(local_root.right,level+1)


if __name__ == '__main__':
    tree_root = main()
    print('level info')
    l_dict = list_depths(tree_root)
    for k,v in l_dict.items():
        print('level' ,k,end='--')
        for j in v:
            print(j.value,end=',')
        print('')

#     using depth first travels - pre order to list nodes at each level
    print('using pre order')
    pre_level_dict = {}

    pre_order_list_depth(tree_root,1)

    for k,v in pre_level_dict.items():
        print('level' ,k,end='--')
        for j in v:
            print(j,end=',')
        print('')



