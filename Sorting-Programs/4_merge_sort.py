def merge_sort(arr):
    """
    Description:
        - A divide-and-conquer algorithm that splits the array in half, sorts each half, and then merges them back together.
        - Time Complexity: O(n log n).
    Args:
        list
    Returns:
        Sorted list
    """
    # Base case: if the array has 1 or fewer elements, it's already sorted
    if len(arr) > 1:
        # Find the middle point to divide the array into two halves
        mid = len(arr) // 2  # Integer division to get the middle index
        left_half = arr[:mid]  # Left sub-array (from start to middle)
        right_half = arr[mid:]  # Right sub-array (from middle to end)

        # Recursively split and sort both halves
        merge_sort(left_half)  # Sorting the left half
        merge_sort(right_half)  # Sorting the right half

        # Indices to track positions in left_half, right_half, and the original array
        i = j = k = 0

        # Merge the sorted halves back into the original array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]  # Take the smaller element from the left half
                i += 1  # Move to the next element in left_half
            else:
                arr[k] = right_half[j]  # Take the smaller element from the right half
                j += 1  # Move to the next element in right_half
            k += 1  # Move to the next position in the original array

        # If there are remaining elements in left_half, add them
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # If there are remaining elements in right_half, add them
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  # The array is now sorted


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
