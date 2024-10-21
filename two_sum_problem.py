def plusOne(digits):
    n = len(digits)
    
    # Start from the end of the array
    for i in range(n - 1, -1, -1):
        # If the digit is less than 9, just add one and return the result
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If the digit is 9, set it to 0
        digits[i] = 0
    
    # If all digits are 9, we end up here
    return [1] + digits

print(plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]
print(plusOne([0]))        # Output: [1]
print(plusOne([2, 9, 9]))