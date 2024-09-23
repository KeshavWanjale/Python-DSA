def linear_search(arr, target):
    """
    Description:
        Finds the target in list using Linear search.
    Parameters:
        arr(list): List of intigers
    Returns:
        int: if target is found index where , else -1 .
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  


arr = [3, 5, 2, 4, 9]
target = 4
result = linear_search(arr, target)
print("Element found at index:", result) if result != -1 else print("Element not found.")
