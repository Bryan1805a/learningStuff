# Rotations in the array is defined as the process of rearranging the elements in an array by shifting each element to a new position. 
# This is mostly done by rotating the elements of the array clockwise or counterclockwise.

# Using The Reversal Algorithm
def reversal_algorithm(arr, d):
    n = len(arr)
    
    # Handle when d > n
    d %= n
    
    arr.reverse()
    
    arr[:d] = reversed(arr[:d])
    arr[d:] = reversed(arr[d:])

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    
    reversal_algorithm(arr, d)
        
    for i in range(len(arr)):
        print(arr[i], end=" ")