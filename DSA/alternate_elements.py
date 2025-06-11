# Given an array arr[], 
# the task is to print every alternate element of the array 
# starting from the first element.

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: 10 30 50
# Explanation: Print the first element (10), 
# skip the second element (20), 
# print the third element (30), 
# skip the fourth element(40) and print the fifth element(50).

def getAlternates(arr):
    new_arr = []

    for i in range(0, len(arr), 2):
        new_arr.append(arr[i])

    return new_arr

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = getAlternates(arr)
    print(" ".join(map(str, res)))