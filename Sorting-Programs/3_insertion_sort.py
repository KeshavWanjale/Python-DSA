def insertion_sort(arr):
    """
    Description:
        - Builds the sorted array one element at a time by repeatedly taking the next element from the unsorted region and inserting it into the correct position in the sorted region.
        - Time Complexity: O(n²).   
    Args:
        list
    Returns:
        Sorted list
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(insertion_sort([12, 11, 13, 5, 6]))
