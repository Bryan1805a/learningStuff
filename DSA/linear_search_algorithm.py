# Given an array, arr of n integers, 
# and an integer element x, 
# find whether element x is present in the array. 
# Return the index of the first occurrence of x in the array, 
# or -1 if it doesn't exist.

# Input: arr[] = [1, 2, 3, 4], x = 3
# Output: 2
# Explanation: There is one test case with array as [1, 2, 3 4] 
# and element to be searched as 3. 
# Since 3 is present at index 2, the output is 2.

def search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)