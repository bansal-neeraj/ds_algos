# to check if a linked list is palindrome , using recursion - WORKING


from linked_list import Node

head = Node(1)

head.append_to_tail(2)
# head.append_to_tail(3)
# head.append_to_tail(4)
# head.append_to_tail(5)
# head.append_to_tail(12)
# head.append_to_tail(12)
# head.append_to_tail(5)
# head.append_to_tail(4)
# head.append_to_tail(3)
# head.append_to_tail(2)
head.append_to_tail(1)

head.show_list()
print(head.show_list.__doc__)
print(dir(head))

node_count = head.list_length()
print(node_count)


def plaindrome_check(head,length):
    """find the middle node using recusrion , when length is known in advance and check is the lined list is a
    palindrome or not, when recursion return , middle is identified , left half moved in reverse direction and right
    half moves in forward direction

    """
    if length == 2:
        print('middle',head.x,"length",length,f'{head.next.x=}')
        if head.x == head.next.x:
            return head.next.next, True
        else:
            return head.next.next, False

    elif length == 1:
        return head.next,True
    else:
        last_node,status = plaindrome_check(head.next, length - 2)
        # reducing 2 means shortening linked list by one element from starting and one element from end
        print('compare',head.x,last_node.x)
        if head.x != last_node.x:
            status = False
        return last_node.next , status


m , status = plaindrome_check(head, node_count)
print(status)



