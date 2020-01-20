'''
Design a tree witch looks as follows:

            1
           / \
          2   3
             / \
            4   5
'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def display_tree(self, start):
        if not start:
            return 'x'
        else:
            return start.data, self.display_tree(start.left), self.display_tree(start.right)


tree = binaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.right = Node(5)
tree.root.right.left = Node(4)

'''
display this designed tree. this process is also called as
serialization os a tree.
'''
a, b, c = tree.display_tree(tree.root)
print(a, b, c)
