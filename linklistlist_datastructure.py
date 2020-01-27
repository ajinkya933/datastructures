'''
class node has two parameters data, and next
 ---------------
( data  | next  )
 ---------------
class node is always going to be called upon and we are always going to insert data
each time we call class node. Initially when we have nothing we define the default
value of data = None, but when we have some data we call class node and insert
our data into it. By default 'next' value will be None as node is our first capsule
and there is nothing after it.
'''

class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
'''
linklist is going to be a class where we are going to join class node back to back
and create a chain of nodes
'''

class linklist:
    def __init__(self):
        self.head=node() # head is just a constructor pointing the node class

    def append(self, data):
        current_node=self.head # here we are calling the node class, we always call the node class through a constructor self.head
        new_node=node(data)
        while current_node.next!= None:
            current_node=current_node.next
        current_node.next=new_node

    def display(self):
        elems=[]
        current_node=self.head  # we initialize a node with a constructor self.head
        while current_node.next!=None:
            elems.append(current_node.data)   # when you want to reverse a linklist then by default head is not NONE so you have to add this statement here
            current_node=current_node.next
            #elems.append(current_node.data)
        print(elems)

    def getnode(self,index):
        index_count=0
        current_node=self.head
        while current_node.next!=None:
            current_node=current_node.next
            if index==index_count:
                return current_node.data
            index_count+=1

    def reverse_iterative(self):     #A -> B -> C
        prev = None
        current_node = self.head
        while current_node:
            next_node=current_node.next  # next_node = B
            current_node.next = prev    #  B -> None
            prev=current_node           # B->A
            current_node = next_node
        self.head = prev


object1=linklist()
object1.display()
object1.append(1)
object1.append(2)
object1.append(3)
object1.append(4)
object1.append(5)
#object1.display()
#got=object1.getnode(3)
#print(got)

object1.reverse_iterative()
out = object1.display()
print(out)
