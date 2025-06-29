import random

def create_test_data():
    test_list = [random.randint(-1000, 1000) for _ in range(10)]
    return test_list

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def display_result(test_data, sorted_data):
    print("Initial Test Data:", test_data)
    print("Sorted Result:", sorted_data)

test_data = create_test_data()
sorted_data = quicksort(test_data)
display_result(test_data, sorted_data)
