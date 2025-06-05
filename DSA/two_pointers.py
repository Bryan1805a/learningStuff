def two_sum(arr, target):
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return f"arr[left]:{arr[left]} + arr[right]:{arr[right]}"
        elif sum > target:
            right -= 1
        else:
            left += 1
    return False

arr = [0, -1, 2, -3, 1]
target = -2

print(two_sum(arr, target))

