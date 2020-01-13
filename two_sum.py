'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

'''
we have to find all numbers in list that add upto k
if we take the first number then k=10+(10-k) is what we need
'''


def two_sum(my_list, k):
    res = []
    for num in my_list:
        a = k-num
        if a in my_list:
            return True


my_list = [10, 15, 3, 7]
k = 17
res = two_sum(my_list, k)
print(res)
