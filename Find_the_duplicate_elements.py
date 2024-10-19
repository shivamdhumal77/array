def find_duplicates(arr):
    n = len(arr)
    res = []
    
    
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                if arr[i] not in res:
                  res.append(arr[i])
                break
            return res


arr = [12,11,0,45,65,34,76,78]
print(find_duplicates(arr))

