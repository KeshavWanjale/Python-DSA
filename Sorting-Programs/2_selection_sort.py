def selection_sort(arr):
    """
    Description:
    - Divides the input into a sorted and unsorted region.
    - Repeatedly selects the smallest (or largest) element from the unsorted region and moves it to the end of the sorted region.
    - Time Complexity: O(n²).
    Args:
        List
    Returns:
        sorted array
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print(selection_sort([64, 25, 12, 22, 11]))
