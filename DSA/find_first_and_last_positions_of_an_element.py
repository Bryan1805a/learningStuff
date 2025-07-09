# Given a sorted array arr[] with possibly some duplicates, 
# the task is to find the first and last occurrences of an element x in the given array.

# Note: If the number x is not found in the array then return both the indices as -1.

# Input : arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
# Output : 2 5
# Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5

def find_first(arr, x) -> int:
    n = len(arr)
    
    low = 0
    high = n - 1
    
    first = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    return first

def find_last(arr, x) -> int:
    n = len(arr)
    
    low = 0
    high = n - 1
    
    last = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return last

def find(arr, x) -> list:
    first = find_first(arr, x)
    last = find_last(arr, x)
    
    res = [first, last]
    
    return res

if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    x = 5
    
    res = find(arr, x)
    print(res[0], res[1])