def findPeak(arr, n):
    # first or last element is peak element
    if n == 1:
        return 0
    if arr[0] >= arr[1]:
        return 0
    if arr[n - 1] >= arr[n - 2]:
        return n - 1

    # check for every other element
    for i in range(1, n - 1):
        # check if the neighbors are smaller
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return i

    # If no peak element is found (though there 
    # should be one in a valid array)
    return -1

# Driver code.
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))