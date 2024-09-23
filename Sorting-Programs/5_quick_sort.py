def quick_sort(arr):
    """
    Description:
        Another divide-and-conquer algorithm that selects a "pivot" element, partitions the other elements into those less than and greater than the pivot, and recursively sorts the partitions.
        Time Complexity: O(n log n) on average, O(n²) in the worst case.
    Args:
        list
    Returns:
        Sorted list
    """
    # Base case: arrays with 1 or zero elements are already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choosing the pivot element (here we choose the middle element)
        pivot = arr[len(arr) // 2]

        # Partitioning step: elements smaller than pivot, equal to pivot, and greater than pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recursively apply quick_sort to left and right partitions and concatenate the results
        return quick_sort(left) + middle + quick_sort(right)
    
print(quick_sort([3, 6, 8, 10, 1, 2, 1]))
