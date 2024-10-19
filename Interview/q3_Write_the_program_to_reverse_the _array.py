def reverse_array_extra_array(arr):
    reversed_arr = arr[::-1]
    
    print("Reversed Array:", end=" ")
    for i in reversed_arr:
        print(i, end=" ")
        
original_arr = [1,2,3,4,5]
reverse_array_extra_array(original_arr)