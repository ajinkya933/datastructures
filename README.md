# datastructures
___
Here i express how I understood datastructures in python, these are the datastructures concepts you need to know as fundamentals of python. The best way to learn them is practice...practice--and practice.

Question 1:
___
```
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can 
climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could 
climb any number from a set of positive integers X? For example, 
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. 
Generalize your function to take in X.
```

Question 2:
___
```
Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in the original 
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected 
output would be [2, 3, 6].

Follow-up: what if you can't use division?
```

Question 3:
___
```
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
```

Question 4:
___
```
Given a string find consiquitively repeting characters in this string
example input='ABBA'
output = B
```
my explaination for solution https://www.youtube.com/watch?v=ws0VeSJUUns&t=23s


Question 5:
___

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:
```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
