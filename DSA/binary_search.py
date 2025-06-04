def binary_search(arr, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return binary_search(arr, low, mid-1, target)
        elif arr[mid] < target:
            return binary_search(arr, mid+1, high, target)
    
    else:
        return -1
    
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Function call
    result = binary_search(arr, 0, len(arr)-1, x)
    print(result)