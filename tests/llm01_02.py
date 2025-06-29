import random
from llm01_01 import quicksort

"""
This program tests the QuickSort implementation from llm01-01.py with various test cases.
It generates different types of input data, runs the QuickSort algorithm, validates the results,
and displays the test outcomes.
"""

def is_sorted(arr):
    """
    Checks if a list is sorted in ascending order.
    
    Args:
        arr (list): The list to check.
    
    Returns:
        bool: True if the list is sorted, False otherwise.
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def generate_random_list(size, min_val=-1000, max_val=1000):
    """
    Generates a list of random integers.
    
    Args:
        size (int): The size of the list.
        min_val (int): The minimum value for random integers.
        max_val (int): The maximum value for random integers.
    
    Returns:
        list: A list of random integers.
    """
    return [random.randint(min_val, max_val) for _ in range(size)]

def generate_sorted_list(size, min_val=-1000, max_val=1000):
    """
    Generates an already sorted list of random integers.
    
    Args:
        size (int): The size of the list.
        min_val (int): The minimum value for random integers.
        max_val (int): The maximum value for random integers.
    
    Returns:
        list: A sorted list of random integers.
    """
    return sorted(generate_random_list(size, min_val, max_val))

def generate_reverse_sorted_list(size, min_val=-1000, max_val=1000):
    """
    Generates a reverse sorted list of random integers.
    
    Args:
        size (int): The size of the list.
        min_val (int): The minimum value for random integers.
        max_val (int): The maximum value for random integers.
    
    Returns:
        list: A reverse sorted list of random integers.
    """
    return sorted(generate_random_list(size, min_val, max_val), reverse=True)

def generate_duplicates_list(size, min_val=-1000, max_val=1000, duplicate_factor=0.5):
    """
    Generates a list with many duplicate values.
    
    Args:
        size (int): The size of the list.
        min_val (int): The minimum value for random integers.
        max_val (int): The maximum value for random integers.
        duplicate_factor (float): The factor determining the number of unique values.
    
    Returns:
        list: A list with many duplicate integers.
    """
    unique_count = int(size * duplicate_factor)
    unique_values = generate_random_list(unique_count, min_val, max_val)
    result = []
    for _ in range(size):
        result.append(random.choice(unique_values))
    return result

def run_test(test_name, input_data):
    """
    Runs the QuickSort algorithm on the input data and checks if the result is sorted.
    
    Args:
        test_name (str): The name of the test.
        input_data (list): The input list to sort.
    
    Returns:
        tuple: (bool, list, list) - Test passed, original input, sorted output.
    """
    sorted_data = quicksort(input_data)
    passed = is_sorted(sorted_data)
    print(f"\nTest: {test_name}")
    print(f"Input Size: {len(input_data)}")
    print(f"Input Data (first 10 elements if large): {input_data[:10]}{'...' if len(input_data) > 10 else ''}")
    print(f"Output Data (first 10 elements if large): {sorted_data[:10]}{'...' if len(sorted_data) > 10 else ''}")
    print(f"Test {'PASSED' if passed else 'FAILED'}")
    return passed, input_data, sorted_data

def main():
    """
    Main function to run all test cases for QuickSort.
    """
    test_results = []
    
    # Test cases for different sizes with random data
    test_results.append(run_test("Random Small (10 elements)", generate_random_list(10)))
    test_results.append(run_test("Random Medium (100 elements)", generate_random_list(100)))
    test_results.append(run_test("Random Large (1000 elements)", generate_random_list(1000)))
    
    # Test cases for already sorted data
    test_results.append(run_test("Sorted Small (10 elements)", generate_sorted_list(10)))
    test_results.append(run_test("Sorted Medium (100 elements)", generate_sorted_list(100)))
    
    # Test cases for reverse sorted data
    test_results.append(run_test("Reverse Sorted Small (10 elements)", generate_reverse_sorted_list(10)))
    test_results.append(run_test("Reverse Sorted Medium (100 elements)", generate_reverse_sorted_list(100)))
    
    # Test cases for data with duplicates
    test_results.append(run_test("Duplicates Small (10 elements)", generate_duplicates_list(10)))
    test_results.append(run_test("Duplicates Medium (100 elements)", generate_duplicates_list(100)))
    
    # Edge cases
    test_results.append(run_test("Empty List", []))
    test_results.append(run_test("Single Element", [42]))
    
    # Summary of results
    passed_tests = sum(1 for result in test_results if result[0])
    total_tests = len(test_results)
    print("\nTest Summary:")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {total_tests - passed_tests}")
    print(f"Pass Rate: {(passed_tests / total_tests) * 100 if total_tests > 0 else 0:.2f}%")

if __name__ == "__main__":
    main()


# Test: Single Element
# Input Size: 1
# Input Data (first 10 elements if large): [42]
# Output Data (first 10 elements if large): [42]
# Test PASSED

# Test Summary:
# Total Tests: 11
# Passed: 11
# Failed: 0
# Pass Rate: 100.00%
