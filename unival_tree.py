'''

Given a node in our tree, we know that it is a univalue subtree
if it meets one of the following criteria:

    1. The node has no children (base case)
    2. All of the node's children are univalue subtrees, and the node and its children all have the same value

'''

'''
step1: define a Node and define a binary tree,
'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def serilize(self, start):

        if not start:
            return 'x'

        else:
            return start.data, self.serilize(start.left), \
                self.serilize(start.right)

    def countUnivalSubtrees(self, root):
        if root is None:
            return 0
        self.count = 0
        # self.is_uni(root)
        # return self.count
        a = self.is_uni(root)
        print(a)

    def is_uni(self, node):
        if node.left is None and node.right is None:
            self.count += 1
            return True
        '''
        If node.left and node.right are not NONE,
        then by default we assume that its a unival tree
        '''
        is_uni = True
        '''
        check if all of the node's children are univalue
        subtrees and if they have the same value
        '''
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.data == node.data
        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.data == node.data

        self.count += is_uni

        return self.count


'''
Step 2: add data to this  binaryTree

                    5
                   / \
                  1   5
                 / \   \
                5   5   5
'''

tree = binaryTree(5)
tree.root.right = Node(5)
tree.root.left = Node(1)
tree.root.right.right = Node(5)
tree.root.left.left = Node(5)
tree.root.left.right = Node(5)

'''
Step 3: count number of nodes which have no children
'''
data = tree.countUnivalSubtrees(tree.root)
print(data)
