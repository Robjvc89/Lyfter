import unittest

def sum_list(numbers):
    total = 0  
    for number in numbers:
        total += number 
    return total 

class TestSumList(unittest.TestCase):

    def test_sum_list_with_positive_numbers(self):
        # Arrange: Prepare the list of numbers
        numbers_list = [15, 22, 34, 14, 5]
        
        # Act: Call the sum_list function with the numbers list
        result = sum_list(numbers_list)
        
        # Assert: Verify that the result is as expected (90)
        self.assertEqual(result, 90)

    def test_sum_list_with_one_number(self):
        # Arrange: Prepare a list with a single number
        numbers_list = [7]
        
        # Act: Call the sum_list function with this list
        result = sum_list(numbers_list)
        
        # Assert: Verify that the result is 7
        self.assertEqual(result, 7)

    def test_sum_list_with_negative_and_positive_numbers(self):
        # Arrange: Prepare a list with negative and positive numbers
        numbers_list = [-10, 5, -3, 8, 12]
        
        # Act: Call the sum_list function with this list
        result = sum_list(numbers_list)
        
        # Assert: Verify that the result is 12
        self.assertEqual(result, 12)

if __name__ == "__main__":
    unittest.main()



