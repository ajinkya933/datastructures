from collections import OrderedDict
import string

a = string.ascii_lowercase
print(a)

b = {}  # define normal dict
b_ordered = OrderedDict()


def add(a):
    '''
    Add elements to a dictionary
    '''
    for count, num in enumerate(a):
        #print(count+1, num)
        b[num] = count+1
        b_ordered[num] = count+1
    return b, b_ordered


def read():
    '''
    read elements from a dictionary
    '''
    for k, v in (b.items()):
        print(k, v)


result, result2 = add(a)
print(result)
print('\n')
print(result2)
