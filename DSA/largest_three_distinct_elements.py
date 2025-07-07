import unittest

def getThreeLargest(arr):
    first = second = third = float('-inf')
    
    for i in range(len(arr)):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]
        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]
    
    # Check elements
    res = []
    if first == float('-inf'):
        return res
    res.append(first)
    
    if second == float('-inf'):
        return res
    res.append(second)
    
    if third == float('-inf'):
        return res
    res.append(third)
    
    return res
    

class TestGetThreeLargest(unittest.TestCase):
    def test_case_1(self):
        arr = [12, 13, 1, 10, 34, 1]
        expected = [34, 13, 12]
        self.assertEqual(getThreeLargest(arr), expected)

    def test_case_2(self):
        arr = [10, 4, 3, 50, 23, 90]
        expected = [90, 50, 23]
        self.assertEqual(getThreeLargest(arr), expected)

    def test_empty_array(self):
        self.assertEqual(getThreeLargest([]), [])

    def test_single_element(self):
        self.assertEqual(getThreeLargest([5]), [5])

    def test_two_elements(self):
        self.assertEqual(getThreeLargest([8, 9]), [9, 8])

    def test_duplicate_largest(self):
        self.assertEqual(getThreeLargest([10, 10, 10]), [10])
        
if __name__ == "__main__":
    unittest.main()