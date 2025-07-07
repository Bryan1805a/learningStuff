import unittest

def binary_search(arr, low, high, key) -> int:
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

class TestGetThreeLargest(unittest.TestCase):
    def test_case_1(self):
        arr = [12, 13, 1, 10, 34, 0]
        expected = 2 # Key = 13, index = 1
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 1), expected)
    
    def test_case_2(self):
        arr = [10, 4, 3, 50, 23, 90]
        expected = 5 # Key = 90, index = 5
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 90), expected)
    
    def test_case_3(self):
        arr = [1, 2, 3]
        expected = 0 #Key = 1, index = 0
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 1), expected)
    
    def test_case_4(self):
        arr = [4, 5, 6]
        expected = -1 # Key is non exist
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 7), expected)

if __name__ == "__main__":
    unittest.main()