import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import heapq
import time





# TODO: tree search: BST, AVL, RB, B-Tree, Heap
# TODO: try to creating graphs to visualize the algorithms


# * generate random list
def generate_random_list(n):
    """
    Generate a random list of n elements
    """
    return np.random.randint(0, 100, n)




# * ############## Algorithms for sorting ##############




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
                yield arr

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
            if arr[j] < arr[min_idx]:
                min_idx = j
        # swap the minimum element with the element at the beginning
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        yield arr

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
        yield arr

# * merge sort

def merge_sort(arr):
    """
    The merge sort algorithm is a divide and conquer algorithm that splits the input into two halves, sorts them separately, and then merges them. 
    The algorithm is stable and efficient for large lists.
    """
    if len(arr) > 1:
        # get the middle index
        mid = len(arr) // 2
        # get the left half
        left = arr[:mid]
        # get the right half
        right = arr[mid:]

        # recursively call the merge sort algorithm for the left half
        yield from merge_sort(left)
        # recursively call the merge sort algorithm for the right half
        yield from merge_sort(right)

        i = j = k = 0
        # Merge the sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            yield arr

        # Copy the remaining elements of left, if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            yield arr

        # Copy the remaining elements of right, if any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            yield arr
    else:
        yield arr

# * quick sort
def partition(arr, low, high):
    """
    The partition function is a helper function for the quick sort algorithm. 
    It takes an array and two indices, low and high, and returns the index of the pivot element.
    """
    pivot = arr[(low + high) // 2]  # Using middle element as pivot
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low=0, high=None):
    """
    The quick sort algorithm is a divide and conquer algorithm that splits the input into two halves, sorts them separately, and then merges them. 
    The algorithm is efficient for large lists.
    """
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        yield from quick_sort(arr, low, pivot_index)
        yield from quick_sort(arr, pivot_index + 1, high)
        yield arr



# * bucket sort (for floating point numbers)

def bucket_sort(arr):
    """
    The bucket sort algorithm is a sorting algorithm that works by distributing the elements of an array into a number of buckets and then sorting the elements of each bucket individually. 
    The algorithm is efficient for large lists of floating point numbers.
    """
    if len(arr) == 0:
        return arr
    n = len(arr)
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / n
    buckets = [[] for _ in range(n + 1)]

    for i in arr:
        index = int((i - min_value) / bucket_range)
        if index == n:
            index -= 1
        buckets[index].append(i)
        yield arr  # Yield the state after adding an element to a bucket

    sorted_array = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)  # Using sorted for simplicity
        sorted_array.extend(sorted_bucket)
        yield sorted_array  # Yield the state after sorting each bucket


# * heap sort

# FIXME: check in place version

def heap_sort(arr):
    """
    The heap sort algorithm is a comparison based sorting algorithm that works by dividing the input into a sorted and an unsorted region. 
    The algorithm is efficient for large lists.
    """
    # Convert numpy array to list if necessary
    if isinstance(arr, np.ndarray):
        arr = arr.tolist()

    # if the array is empty, return the array
    if len(arr) == 0:
        return arr

    # Transform list into a heap
    heapq.heapify(arr)
    n = len(arr)
    sorted_arr = []

    # Extract elements one by one
    for _ in range(n):
        sorted_arr.append(heapq.heappop(arr))
        yield sorted_arr + arr  # This yields the current state of the sorted and unsorted parts





# * ############## Algorithms for searching ##############


#linear search


def linear_search(arr, x):
    """
    The linear search algorithm is a simple searching algorithm that searches for an element in a list by going through the list one by one. 
    The algorithm is efficient for small lists.
    """
    for index, value in enumerate(arr):
        if value == x:
            return index
    return -1

# binary search
def binary_search(arr, x):
    """
    The binary search algorithm is a divide and conquer algorithm that splits the input into two halves, sorts them separately, and then merges them. 
    The algorithm is efficient for large lists.
    """
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# hash search
def hash_search(arr, x):
    """
    The hash search algorithm uses a hash table to store the elements of the list for quick lookup.
    """
    # Create a hash table
    hash_table = {}
    # Populate the hash table with elements from the array
    for index, value in enumerate(arr):
        hash_table[value] = index

    # Search for the item using the hash table
    if x in hash_table:
        return hash_table[x]
    else:
        return -1
    


#* ############## Algorithms for graphs ##############
# TODO: graph search: breadth-first search, depth-first search, bellman-ford, dijkstra, A* algorithm




# * ############## main function ##############

def main():
    st.title("Algorithms visualizer")
    st.subheader("Sorting algorithms")
    st.write("This is a visualizer for sorting algorithms")
    n = st.slider("Number of elements", 1, 100)
    arr = generate_random_list(n)

    algo_choice = st.selectbox("Select algorithm", ["Bubble sort", "Selection sort", "Insertion sort", "Merge sort", "Quick sort", "Heap sort", "Bucket sort"])
    algo_dict = {
        "Bubble sort": bubble_sort,
        "Selection sort": selection_sort,
        "Insertion sort": insertion_sort,
        "Merge sort": merge_sort,
        "Quick sort": quick_sort,
        "Heap sort": heap_sort,
        "Bucket sort": bucket_sort
    }

    algorithm = algo_dict[algo_choice]

    if st.button("Sort"):
        st.write("Sorting...")
        chart = st.empty()
        for i in algorithm(arr):
            fig = go.Figure(data=[go.Bar(x=np.arange(len(i)), y=i, marker=dict(color=i, colorscale="Viridis"))])
            chart.plotly_chart(fig)
            time.sleep(0.05)

if __name__ == "__main__":
    main()