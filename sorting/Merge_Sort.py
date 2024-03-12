import math


def merge_sort(array, a, b):
    if b - a > 0:
        q = math.floor((a + b) / 2)

        merge_sort(array, a, q)
        merge_sort(array, q + 1, b)
        merge(array, a, q, b)


def merge(array, a, q, b):
    l = []
    r = []

    for i in range(a, q + 1):
        l.append(array[i])

    for i in range(q + 1, b + 1):
        r.append(array[i])

    l.append(len(array) + 1)
    r.append(len(array) + 1)

    j = 0
    k = 0

    for i in range(a, b + 1):
        if l[j] <= r[k]:
            array[i] = l[j]
            j = j + 1
        else:
            array[i] = r[k]
            k = k + 1
