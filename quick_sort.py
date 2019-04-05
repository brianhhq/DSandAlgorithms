#!/usr/bin/env python


def quick_sort(arr, l, r):
    """
    :param arr: array to be sorted
    :param l: starting index
    :param r: ending index
    :return: None
    """
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, l, pivot-1)
        quick_sort(arr, pivot+1, r)


def partition(arr, l, r):
    """
    :param arr: array to be sorted
    :param l: starting index
    :param r: ending index
    :return: the pivot
    """
    i = l - 1
    x = arr[r]  # use rightest one as pivot
    for j in range(l, r):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    r = len(arr)-1
    print(f'Before Sorted: {"-".join([str(i) for i in arr])}')
    quick_sort(arr, 0, r)
    print(f'After Sorted: {"-".join([str(i) for i in arr])}')
