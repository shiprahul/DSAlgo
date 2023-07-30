#when the target is provided

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1  # Initialize the result to -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            result = mid  # Update the result to the current element smaller than the target
            left = mid + 1
        else:
            right = mid - 1

    return result  # Return the index of the element smaller than the target
'''
Explanation:

We modify the binary search algorithm to use mid = (left + right) // 2 to calculate the midpoint, 
which ensures the proper middle index is used to divide the search space.

We initialize the result variable to -1 before starting the binary search. 
This variable will keep track of the index of the element smaller than the target.

During the binary search, if the element at mid is smaller than the target, we update the result variable to the current index mid.

If the target is not found in the list, the loop will terminate, and the function will return the value of result, 
which will be the index of the element smaller than the target.
With this modification, the binary search will now correctly return the index of the element smaller than the target if the target is not present in the list.
'''
