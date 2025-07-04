def pushZeroesToEnd(arr):
    count = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            pass
        else:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZeroesToEnd(arr)
    for num in arr:
        print(num, end=" ")