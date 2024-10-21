def reverse_arr(arr):
    n = len(arr)-1
    temp = []*n
    
    for i in range(n):
     temp[i] = arr[n-i-1]

# copy elements to temporary elements
    for i in range(n):
        arr[i] = temp[i]


arr = [1,4,3,5,6,32,5] 
reverse_arr(arr)

for i in range(len(arr)):
    print(arr[i], end =" ")      