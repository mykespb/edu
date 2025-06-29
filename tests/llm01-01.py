import random

"""
This program implements the QuickSort algorithm to sort a list of randomly generated integers.
It includes functions to create test data, sort the data using QuickSort, and display the results.
"""

def create_test_data():
    """
    Generates a list of 10 random integers between -1000 and 1000 for testing sorting algorithms.
    
    Returns:
        list: A list of 10 random integers.
    """
    test_list = [random.randint(-1000, 1000) for _ in range(10)]
    return test_list

def quicksort(arr):
    """
    Sorts a list of integers using the QuickSort algorithm.
    The algorithm selects a 'pivot' element from the list and partitions the other elements into
    three sub-lists: less than, equal to, and greater than the pivot. It then recursively sorts
    the sub-lists.
    
    Args:
        arr (list): The list of integers to be sorted.
    
    Returns:
        list: A new sorted list containing all elements from the input list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def display_result(test_data, sorted_data):
    """
    Displays the initial unsorted test data and the sorted result.
    
    Args:
        test_data (list): The original unsorted list of integers.
        sorted_data (list): The sorted list of integers.
    """
    print("Initial Test Data:", test_data)
    print("Sorted Result:", sorted_data)

test_data = create_test_data()
sorted_data = quicksort(test_data)
display_result(test_data, sorted_data)
