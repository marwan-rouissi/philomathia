import numpy as np
"""algorithme de tri"""


def bubble_sort(T):
    n = len(T)
    for i in range(n):
        for j in range(n-1, i, -1):
            if T[j] < T[j-1]:
                T[j], T[j-1] = T[j-1], T[j]
    return T


def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        x = T[i]
        j = i
        while j > 0 and T[j-1] > x:
            T[j] = T[j-1]
            j -= 1
        T[j] = x
    return T


def merge_sort(T):
    n = len(T)
    if n <= 1:
        return T
    else:
        T1 = merge_sort(T[:n//2])
        T2 = merge_sort(T[n//2:])
        return merge(T1, T2)
    

def merge(T1, T2):
    n1, n2 = len(T1), len(T2)
    T = []
    i, j = 0, 0
    while i < n1 and j < n2:
        if T1[i] < T2[j]:
            T.append(T1[i])
            i += 1
        else:
            T.append(T2[j])
            j += 1
    if i < n1:
        T.extend(T1[i:])
    else:
        T.extend(T2[j:])
    return T


def quick_sort(T):
    n = len(T)
    if n <= 1:
        return T
    else:
        x = T[0]
        T1 = [y for y in T[1:] if y <= x]
        T2 = [y for y in T[1:] if y > x]
        return quick_sort(T1) + [x] + quick_sort(T2)