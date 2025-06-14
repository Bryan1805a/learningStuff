# Given an array arr[], 
# the task is to find the top three largest distinct integers 
# present in the array.

# Note: If there are less than three distinct elements in the array, 
# then return the available distinct numbers in descending order.

# Input: arr[] = [10, 4, 3, 50, 23, 90]
# Output: [90, 50, 23]

# Input: arr[] = [10, 9, 9]
# Output: [10, 9]
# There are only two distinct elements

# Input: arr[] = [10, 10, 10]
# Output: [10]
# There is only one distinct element

# Input: arr[] = []
# Output: []

def find_three_largest(arr) -> list:
    first = second = third = float('-inf')
    new_arr = []

    for i in arr:
        if i > first:
            third = second
            second = first
            first = i
        elif i > second and i != first:
            third = second
            second = i
        elif i > third and i != second and i != first:
            third = i

    if first == float('-inf'):
        return new_arr
    new_arr.append(first)

    if second == float('-inf'):
        return new_arr
    new_arr.append(second)

    if third == float('-inf'):
        return new_arr
    new_arr.append(third)

    return new_arr
arr = [12, 13, 1, 10, 34, 1]
res = find_three_largest(arr)
print(" ".join(map(str, res)))