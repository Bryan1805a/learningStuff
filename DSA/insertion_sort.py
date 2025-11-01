def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        sorted_element_index = i
        current_value = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                arr[j + 1] = arr[j]
                sorted_element_index = j
            else:
                break
        arr[sorted_element_index] = current_value

    print(arr)

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    insertion_sort(arr)
