import unittest

def floor_square(n) -> int:
    low = 1
    high = n
    res = 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if mid * mid <= n:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return res

class Test(unittest.TestCase):
    def test_case_1(self):
        n = 11
        expected = 3
        self.assertEqual(floor_square(n), expected)
        
if __name__ == "__main__":
    unittest.main()