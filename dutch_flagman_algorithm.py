def dutch_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]  # Fixing the assignment
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]  # Fixing the assignment
            high -= 1

    return arr


arr = [0, 1, 0, 2, 0, 1]
print(dutch_flag(arr))

for x in arr:
    print(x, end=" ")
