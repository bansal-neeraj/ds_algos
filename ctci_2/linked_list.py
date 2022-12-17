# create a sigly linked link list , and reverse

class Node:
    def __init__(self,x,n=None):
        self.x = x
        self.next = n

    def append_to_tail(self,d):
        new_node = Node(d)
        n = self
        while n.next :
            n = n.next
        n.next = new_node

    def show_list(self):
        """to display the contents of a linked list"""
        n = self
        while n.next:
            print(n.x,end=",")
            n = n.next
        print(n.x)

    def list_length(self):
        """called from head node and returns the number of nodes in a lined list i.e. length of the list"""
        node_count = 0
        node= self
        while (node):
            node_count += 1
            node = node.next

        return node_count

    def get_specific_node(self,loc):
        """return the node at a specific location"""
        node = self
        i = 1
        while node.next:
            if i==loc:
                return node
            else:
                i+= 1
                node = node.next
        return None


def reverse_without_recursion(n):
    """reverse a linked list without recursion"""
    head = None
    while n:
        new_node = Node(n.x)
        new_node.next = head
        head = new_node
        n = n.next
    return head


def reverse_recursion(root):
    """ using recursion"""
    if root.next:
        x, head = reverse_recursion(root.next)
        x.next = root
        return root,head
    else:
        head = root
        return root,head


head = Node(10)

head.append_to_tail(20)
head.append_to_tail(30)
head.append_to_tail(40)
head.append_to_tail(50)

if __name__ == '__main__':
    head.show_list()

    new_head = reverse_without_recursion(head)
    new_head.show_list()

    r, r_head = reverse_recursion(head)

    r.next = None
    r_head.show_list()



