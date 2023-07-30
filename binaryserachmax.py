#when the target is provided
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = len(arr)  # Initialize the result to the length of the list

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            result = mid  # Update the result to the current element larger than the target
            right = mid - 1
        else:
            left = mid + 1

    return result  # Return the index of the element larger than the target
