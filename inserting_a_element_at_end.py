def insert(arr,element):
    arr.append(element)
    
if __name__ == '__main__':
    arr = [12,16,20,40,50,70]
    key = 26
    print(" before inserting")
    print(arr)
    
    insert(arr, key)
    print('after inserting')
    print(arr)