from random import randint


def quick_sort(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    pivot = a[randint(0, len(a)-1)]

    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quick_sort(smaller)+equal+quick_sort(larger)


a = [3, 1, 2, 6, 9]
print(quick_sort(a))
