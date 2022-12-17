# linked list with a loop , check if there is a loop and if yes then what is the starting node of the loop

from ctci_2.linked_list import Node

head = Node(1)

head.append_to_tail(2)
head.append_to_tail(3)
head.append_to_tail(4)
head.append_to_tail(5)
head.append_to_tail(6)
head.append_to_tail(7)
head.append_to_tail(8)
head.append_to_tail(9)

head.show_list()

specific_node = head.get_specific_node(5)
if specific_node:
    print(specific_node.x)
else:
    print('not found')


def create_loop(head_list: Node,existng_node: Node) -> None:
    """creates a loop in the linked list by linking an existing node in the end"""
    n = head_list
    while n.next:
        n = n.next
    n.next = existng_node


create_loop(head,specific_node)


def runner(head_list: Node) -> (Node, bool):
    """check if loop exists in the linked list"""
    sp = head_list
    fp = head_list
    while fp.next and fp.next.next:
        if sp == fp and sp !=head_list:
            return sp
        else:
            sp = sp.next
            fp = fp.next.next

    return False


collision_point = runner(head)
print('collosion point',collision_point.x)


def find_loop_start(head_list: Node,collsion: Node) -> Node:
    """find where the loop starts"""
    sp = head_list
    fp = collsion
    while sp != fp:
        sp= sp.next
        fp= fp.next
    return sp


node_where_loop_starts = find_loop_start(head,collision_point)
print(node_where_loop_starts.x)


