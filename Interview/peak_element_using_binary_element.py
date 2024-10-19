# Find the peak element using recursive Binary Search
# Using Binary Search, check if the middle element is the peak element or not. If the middle element is not the peak element, then check if the element on the right side is greater than the middle element then there
# is always a peak element on the right side. 
# If the element on the left side is greater than the middle element then there is always a peak element on the left side. 


def findpeakutil(arr, low , high, n):
    
    mid = low +(high-low)/2
    mid = int(mid)
    
    # compare middle element with its 
    # neighbours (if neighbours exist)
    
    if ((mid==0 or arr[mid - 1]<= arr[mid]) and 
        (mid == n-1 or arr[mid+1]<=arr[mid])):
        return mid
    
    # compare middle element with its
    # neighbours (if neighbours exist)
    elif (mid > 0 and arr[mid-1]> arr[mid]):
        return findpeakutil(arr,low,(mid-1), n)
    
    else:
        return findpeakutil(arr, (mid+1), high ,n)
    
    
# A wrapper over recursive
# function findpeakutil()

def findpeak(arr,n):
    return findpeakutil(arr,0,n-1,n)

# driver code
arr = [1,3,20,4,1,0]
n = len(arr)
print("index oc a peak point is", findpeak(arr,n))

