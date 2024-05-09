import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import heapq
import time




# TODO: graph search: breadth-first search, depth-first search, bellman-ford, dijkstra, A* algorithm
# TODO: tree search: BST, AVL, RB, B-Tree, Heap
# TODO: try to creating graphs to visualize the algorithms


# * generate random list
def generate_random_list(n):
    """
    Generate a random list of n elements
    """
    return np.random.randint(0, 100, n)




# * ############## Algorithms for sorting ##############
# TODO: sorting algorithms: Bubble sort(nb), selectionn sort(nb), insertion sort(nb), merge sort(nb), quick sort(nb),bucket sort, heap sort(nb),



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

        yield arr
    else:
        return arr

# * quick sort
def partition(arr, low, high):
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
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        yield from quick_sort(arr, low, pivot_index)
        yield from quick_sort(arr, pivot_index + 1, high)
        yield arr

# Example usage:
# arr = [your array]
# result = list(quick_sort(arr, 0, len(arr) - 1))
        


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


# * heap sort


def heap_sort(arr):
    """
    The heap sort algorithm is a comparison based sorting algorithm that works by dividing the input into a sorted and an unsorted region. 
    The algorithm is efficient for large lists.
    """
    # if the array is empty, return the array
    if len(arr) == 0:
        return arr
    # get the length of the array
    n = len(arr)
    # create a max heap
    for i in range(n//2 - 1, -1, -1):
        heapq.heapify(arr, i, n)
    # loop through the array
    for i in range(n-1, 0, -1):
        # swap the first element with the last element
        arr[i], arr[0] = arr[0], arr[i]
        # heapify the array
        heapq.heapify(arr, i, 0)
    yield arr


# * ############## Algorithms for searching ##############

# TODO: list search: linear search, binary search, hash search,




# * ############## main function ##############

def main():
    st.title("Algorithms visualizer")
    st.subheader("Sorting algorithms")
    st.write("This is a visualizer for sorting algorithms")
    st.write("You can select the algorithm you want to use and the size of the array")
    st.write("You can also select the number of elements you want to sort")
    n = st.slider("Number of elements", 1, 100, )
    arr = generate_random_list(n)
    

    algo_choice = st.selectbox("Select algorithm", ["Bubble sort", "Selection sort", "Insertion sort", "Merge sort", "Quick sort",  "Heap sort"])
    algo_dict = {
        "Bubble sort": bubble_sort,
        "Selection sort": selection_sort,
        "Insertion sort": insertion_sort,
        "Merge sort": merge_sort,
        "Quick sort": quick_sort,
        #"Bucket sort": bucket_sort,
        "Heap sort": heap_sort
    }


    algorithm = algo_dict[algo_choice]
    
    
    if st.button("Sort"):
        st.write("Sorting...")
        chart = st.empty()
        for i in algorithm(arr):
            fig = go.Figure(data=[go.Bar(x=np.arange(len(arr)), y=i, marker=dict(color=i, colorscale="Viridis"),
                                         )])
            chart.plotly_chart(fig)
            
            time.sleep(0.05)


if __name__ == "__main__":
    main()
