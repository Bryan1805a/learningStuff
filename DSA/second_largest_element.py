# Given an array of positive integers arr[] of size n, 
# the task is to find second largest distinct element in the array.

# Using One Pass Search
# The idea is to keep track of the largest and second largest element while traversing the array. 
# Initialize largest and secondLargest with -1. Now, for any index i,
# If arr[i] > largest, update secondLargest with largest and largest with arr[i].
# Else If arr[i] < largest and arr[i] > secondLargest, update secondLargest with arr[i]. 

def getSecondLargest(arr):
    largest = -1
    second_largest = -1
    
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
            
    return second_largest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))
    
    arr_2 = [10, 5, 10]
    print(getSecondLargest(arr_2))
    
    arr_3 = [10, 10, 10]
    print(getSecondLargest(arr_3))