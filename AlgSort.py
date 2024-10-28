from random import randint
from time import time


def insertion_sort(lst):
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > tmp:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = tmp
    return lst


def bubble_sort(lst):
    n = len(lst)
    unordered = True
    while unordered:
        unordered = False
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                unordered = True
    return lst


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
    return lst


def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    x = lst[0]
    left_half = []
    right_half = []
    middle = []
    for el in lst:
        if el < x:
            left_half.append(el)
        elif el > x:
            right_half.append(el)
        else:
            middle.append(el)
    return quick_sort(left_half) + middle + quick_sort(right_half)


if __name__ == "__main__":
    for i in range(1, 9):
        n = 10 ** i
        unsorted_list = [randint(1, 100) for _ in range(n)]

        print("Number of elements:", n)

        # print("Original list:", unsorted_list)

        start_time = time()
        bubble_sorted_list = bubble_sort(unsorted_list.copy())
        print("Bubble sort time:", time() - start_time)
        # print("Bubble sort:", bubble_sorted_list)

        start_time = time()
        insertion_sorted_list = insertion_sort(unsorted_list.copy())
        print("Insertion sort time:", time() - start_time)
        # print("Insertion sort:", insertion_sorted_list)

        start_time = time()
        selection_sorted_list = selection_sort(unsorted_list.copy())
        print("Selection sort time:", time() - start_time)
        # print("Selection sort:", selection_sorted_list)

        start_time = time()
        merge_sorted_list = merge_sort(unsorted_list.copy())
        print("Merge sort time:", time() - start_time)
        # print("Merge sort:", merge_sorted_list)

        start_time = time()
        quick_sorted_list = quick_sort(unsorted_list.copy())
        print("Quick sort time:", time() - start_time)
        # print("Quick sort:", quick_sorted_list)

        start_time = time()
        sorted_list = sorted(unsorted_list.copy())
        print("Sorted time:", time() - start_time)
        # print("Sorted list:", sorted_list)
