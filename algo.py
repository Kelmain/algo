import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt



# TODO: sorting algorithms: Bubble sort(nb), selectionn sort(nb), insertion sort(nb), merge sort(nb), quick sort(nb),bucket sort, heap sort(nb),
# TODO: list search: linear search, binary search, hash search,
# TODO: graph search: breadth-first search, depth-first search, bellman-ford, dijkstra, A* algorithm
# TODO: tree search: BST, AVL, RB, B-Tree, Heap
# TODO: try to creating graphs to visualize the algorithms


# * generate random list
def generate_random_list(n):
    """
    Generate a random list of n elements
    """
    return np.random.randint(0, 100, n)



# * bubble sort
def bubble_sort(arr):
    """
    Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. 
    The pass through the list is repeated until the list is sorted.
    """
    if len(arr) <= 1:
        return arr
    # get length of the array
    n = len(arr)
    # loop through the array
    for i in range(n):
        # loop through the array again
        # n-i-1 because the last i elements are already sorted
        for j in range(0, n-i-1):
            # if the current element is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# * selection sort
def selection_sort(arr):
    """
    The selection sort algorithm sorts an array by repeatedly finding the minimum element from the unsorted part and putting it at the beginning. 
    The algorithm maintains two subarrays in a given array.
    """
    # if the array is empty, return the array
    if len(arr) == 0:
        return arr
    # get length of the array
    n = len(arr)
    # loop through the array
    for i in range(n):
        # find the minimum element in the unsorted part
        min_idx = i
        # loop through the array again
        for j in range(i+1, n):
            # if the current element is less than the minimum element, update the minimum element
            min_idx = j
        # swap the minimum element with the element at the beginning
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

# * insertion sort
def insertion_sort(arr):
    """
    The insertion sort algorithm is a simple sorting algorithm that builds the final sorted array one item at a time. 
    It is much less efficient on large lists than more advanced algorithms such as quicksort or heapsort, but its simplicity and in-place nature makes it a good choice for small lists or for lists that are nearly sorted.
    """
    # if the array is empty, return the array
    if len(arr) == 0:
        return arr
    # get length of the array
    n = len(arr)
    # loop through the array
    for i in range(1, n):
        # get the current element
        key = arr[i]
        # get the index of the previous element
        j = i-1
        # while j is greater than 0 and the previous element is greater than the current element, swap them
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # insert the current element at the right position
        arr[j+1] = key
    return arr

# * merge sort
def merge_sort(arr):
    """
    The merge sort algorithm is a divide and conquer algorithm that splits the input into two halves, sorts them separately, and then merges them. 
    The algorithm is stable and efficient for large lists.
    """
    if len(arr) > 1:
        # get the middle index
        mid = len(arr)//2
        # get the left half
        l = arr[:mid]
        # get the right half
        r = arr[mid:]
        # recursively call the merge sort algorithm for the left half
        merge_sort(l)
        # recursively call the merge sort algorithm for the right half
        merge_sort(r)


        i = j = k = 0
        # Until we reach the end of either left or right half
        while i < len(l) and j < len(r):
            # If the current element in the left half is less than the current element in the right half,
            # we add the current element in the left half to the array and increment the left half index
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        # While we have elements in the left half, we add them to the array
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        # While we have elements in the right half, we add them to the array
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

        return arr
    else:
        return arr

# * quick sort
def partition(arr, low, high):
    """
    Partition the array into two halves
    """
    # get the pivot element
    pivot = arr[low]
    # get the index of the pivot element
    i = low + 1
    # get the index of the last element
    j = high
    # while i is less than j
    while i <= j:
        # if the current element is less than the pivot, increment the index
        if arr[i] < pivot:
            i += 1
        # if the current element is greater than the pivot, decrement the index
        elif arr[j] > pivot:
            j -= 1
        # else, swap the elements
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i


def quick_sort(arr):
    """
    The quick sort algorithm is a divide and conquer algorithm that works by selecting a pivot element from the array and partitioning the other elements into two sub-arrays, 
    according to whether they are less than or greater than the pivot. The algorithm then recursively sorts the sub-arrays.
    """
    if len(arr) <= 1:
        return arr
    if len(arr) > 1:
        # get the index of the pivot element
        pivot = partition(arr, 0, len(arr)-1)
        # recursively call the quick sort algorithm for the left half
        quick_sort(arr[:pivot])
        # recursively call the quick sort algorithm for the right half
        quick_sort(arr[pivot:])
    return arr


# * bucket sort (for floating point numbers)

def bucket_sort(arr):
    """
    The bucket sort algorithm is a sorting algorithm that works by distributing the elements of an array into a number of buckets and then sorting the elements of each bucket individually. 
    The algorithm is efficient for large lists of floating point numbers.
    """
    # if the array is empty, return the array
    if len(arr) == 0:
        return arr
    # get the length of the array
    n = len(arr)
    # create an empty bucket for each element in the array
    buckets = [[] for _ in range(n)]
    # loop through the array
    for i in range(n):
        # get the index of the bucket
        index = int(n * arr[i])
        # add the element to the bucket
        buckets[index].append(arr[i])
    # sort the elements of each bucket
    for i in range(n):
        buckets[i] = quick_sort(buckets[i])
    # concatenate the sorted buckets
    return [item for sublist in buckets for item in sublist]
