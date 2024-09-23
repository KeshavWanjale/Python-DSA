def bubble_sort(arr):
    """
    Description:
        - Compares adjacent elements and swaps them if they are in the wrong order.
        - Repeats this process until no swaps are needed.
        - Time Complexity: O(n²) in the worst case.
    Args:
        arr list
    Returns:
        Sorted Array
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))