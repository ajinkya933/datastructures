'''
this code shows how to fill values in a binary tree
and how to find the depth of this binary tree and
also how to serialize a binary tree


                1
               / \
              2   3
             / \
            4   5
'''
class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None
class binaryTree:
    def __init__(self, root):
        self.root=Node(root)

    def serialize(self, start):
        if not start:
            return 'x'
        else:
            return start.data, self.serialize(start.left), self.serialize(start.right)

    def height(self, start):
        if not start:
            return -1
        left_node=self.height(start.left)
        right_node=self.height(start.right)

        return 1 + max(left_node, right_node)



tree = binaryTree(1)
tree.root.right=Node(3)
tree.root.left = Node(2)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)


height=tree.height(tree.root)
print('height of tree = ',height)

serialize  = tree.serialize(tree.root)
print(serialize)
