def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)


# Driver function to test the above function
A = [1, 2, 3, 4, 5, 6]
print("Original list:", A)
reverseList(A, 0, len(A) - 1)  # Fixed the end index here
print("Reversed list is:")
print(A)
