# Given an array of size n, the task is to check if it is sorted in ascending order or not. 
# Equal values are allowed in an array and two consecutive equal values are considered sorted.

# Examples: 
# Input: arr[] = [20, 21, 45, 89, 89, 90]
# Output: Yes

# Input: arr[] = [20, 20, 45, 89, 89, 90]
# Output: Yes

# Input: arr[] = [20, 20, 78, 98, 99, 97]
# Output: No

def check_sorted_array(arr, n) -> bool:
    if (n == 0) or (n == 1):
        return True
    
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False

    return True

arr = [20, 23, 23, 45, 78, 88]
n = len(arr)
if (check_sorted_array(arr, n)):
    print("Yes")
else:
    print("No")