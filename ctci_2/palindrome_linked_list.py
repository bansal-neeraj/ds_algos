# check if a linked list is plaindrome, using stack - WORKING
from linked_list import Node

head = Node(1)
head.append_to_tail(2)
head.append_to_tail(2)
head.append_to_tail(1)
# head.append_to_tail(6)
# head.append_to_tail(4)
# head.append_to_tail(3)
# head.append_to_tail(2)
# head.append_to_tail(1)

head.show_list()
print(head.list_length())


def check_palindrome(head):
    """check if a linked list is palindrome , using slow and fast pointers and loop"""

    slow = head
    fast = head
    stack = []
    mid_position = 1
    while fast and slow:
        stack.append(slow.x)

        if fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            mid_position += 2
        else:
            if fast.next:
                mid_position += 1
            break

    print(f'middle{slow.x}')
    print(stack)
    print(f'{mid_position=}')
    root = slow.next
    if mid_position % 2 != 0:
        stack.pop()

    while root:
        t_item = stack.pop()
        if t_item != root.x:
            # print(t_item,root.x)
            return False
        else:
            root = root.next

    return True


print(check_palindrome(head))


def palindrome_stack(head):
    """check palindrome using stack"""
    root = head
    link_stack = []
    status = True
    while head:
        link_stack.append(head.x)
        head = head.next

    while root:
        item = link_stack.pop()
        if root.x != item:
            status = False
            break
        else:
            root = root.next

    return status


# print(palindrome_stack(head))

