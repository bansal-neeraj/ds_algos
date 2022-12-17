# to create a binary search tree and
class Node:

    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def add_node(self, x):
        """to be called via root node"""
        root = self
        if root.value > x:
            if root.left:
                root.left.add_node(x)
            else:
                n = Node(x)
                root.left = n

        else:
            if root.right:
                root.right.add_node(x)
            else:
                n = Node(x)
                root.right = n

    def in_order(self):
        """visit left then current node and then right node"""
        local_root = self

        if local_root.left:
            local_root.left.in_order()
        print(self.value, end=',')
        if local_root.right:
            local_root.right.in_order()

    def pre_order(self):
        """visit current node before child nodes"""
        print(self.value, end=',')
        local_root = self
        if local_root.left:
            local_root.left.pre_order()

        if local_root.right:
            local_root.right.pre_order()

    def post_order(self):
        """visit let , then right , then current node"""
        local_root = self
        if local_root.left:
            local_root.left.post_order()

        if local_root.right:
            local_root.right.post_order()
        print(self.value, end=',')


def main():
    root = Node(15)
    root.add_node(12)
    root.add_node(7)
    root.add_node(14)
    root.add_node(27)
    root.add_node(20)
    root.add_node(88)
    root.add_node(23)

    root.in_order()
    print()
    root.pre_order()
    print()
    root.post_order()


if __name__ == '__main__':
    main()


