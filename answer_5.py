
class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None

class binaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def serialize(self, start):
        if not start:
            return 'x'
        else:
            return start.data, self.serialize(start.left), self.serialize(start.right)

    def deserialize(self, data):

        if (data[0]) == 'x':
            return None
        node = Node(data[0])
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])

        return node


tree=binaryTree(0)
tree.root.left = Node(1)
tree.root.right = Node(0)
tree.root.right.right = Node(0)
tree.root.right.left = Node(1)

tree.root.right.left.right = Node(1)
tree.root.right.left.left = Node(1)

res_serialize = tree.serialize(tree.root)
print(res_serialize)

res_deserialize = tree.deserialize(res_serialize)
print(res_deserialize)
