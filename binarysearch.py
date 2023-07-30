def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left+(right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1#increasing the value
        else:
            right = mid - 1#decreasing the value

    return -1
  '''
  In this example we add the binary serach algo and we return -1 if we don't find an target'''
