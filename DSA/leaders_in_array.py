# Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.
# Note: The rightmost element is always a leader.

# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
# Explanation: 17 is greater than all the elements to its right i.e., 
# [4, 3, 5, 2], therefore 17 is a leader. 
# 5 is greater than all the elements to its right i.e., 
# [2], therefore 5 is a leader. 2 has no element to its right, 
# therefore 2 is a leader.

def find_leader(arr) -> list:
    n = len(arr)
    result_arr = []

    max_right_leader = arr[-1]
    result_arr.append(max_right_leader)

    # Traverse from the second right element
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right_leader:
            max_right_leader = arr[i]
            result_arr.append(max_right_leader)

    result_arr.reverse()

    return result_arr

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = find_leader(arr)
    print(" ".join(map(str, result)))