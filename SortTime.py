from LibSort import *
from time import time

for i in range(1, 9):
    n = 10 ** i
    unsorted_list = [randint(1, 100000) for _ in range(n)]

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
