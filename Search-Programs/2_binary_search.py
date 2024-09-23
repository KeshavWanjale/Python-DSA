def binary_search(arr, target):
    """
    Description:
        Finds the target in list using Binary Search Algorithm
    Parameters:
        arr(list): List of intigers
    Returns:
        int: if target is found index where , else -1 .
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        
        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half
    
    return -1  # Return -1 if the element is not found


arr = [1, 2, 3, 4, 5, 6, 7]
target = 4
result = binary_search(arr, target)
print("Element found at index:", result) if result != -1 else print("Element not found.")
