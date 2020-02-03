from random import randint


def create_array(size=10, max=50):
    return [randint(0, max) for _ in range(size)]


def partition(a, low, high):
    i = low-1
    pivot = a[high]
    print('pivot', pivot)
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return i+1


def quicksort_inplace(a, low=0, high=None):
    if high == None:
        high = len(a)-1
    if low < high:
        p_idx = partition(a, low, high)
        quicksort_inplace(a, low, p_idx-1)
        quicksort_inplace(a, p_idx+1, high)


a = create_array()
print('unsorted', a)
quicksort_inplace(a)
print('sorted', a)
