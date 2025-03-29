import unittest

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():  # Checks if the character is uppercase
            upper_count += 1
        elif char.islower():  # Checks if the character is lowercase
            lower_count += 1

    return upper_count, lower_count  # Return the counts for testing purposes

class TestCountUpperLower(unittest.TestCase):

    def test_count_upper_lower_with_mixed_case(self):
        # Arrange: Prepare the string with both uppercase and lowercase letters
        text = "Vamos a visitar Medio Oriente."
        
        # Act: Call the count_upper_lower function with this string
        upper_count, lower_count = count_upper_lower(text)
        
        # Assert: Verify the count of uppercase and lowercase letters
        self.assertEqual(upper_count, 3)  # "V", "M", "O" (3 uppercase letters)
        self.assertEqual(lower_count, 22)  # All the lowercase letters

    def test_count_upper_lower_with_all_uppercase(self):
        # Arrange: Prepare a string with all uppercase letters
        text = "HELLO WORLD"
        
        # Act: Call the count_upper_lower function with this string
        upper_count, lower_count = count_upper_lower(text)
        
        # Assert: Verify that there are 10 uppercase and 0 lowercase letters
        self.assertEqual(upper_count, 10)
        self.assertEqual(lower_count, 0)

    def test_count_upper_lower_with_all_lowercase(self):
        # Arrange: Prepare a string with all lowercase letters
        text = "hello world"
        
        # Act: Call the count_upper_lower function with this string
        upper_count, lower_count = count_upper_lower(text)
        
        # Assert: Verify that there are 0 uppercase and 10 lowercase letters
        self.assertEqual(upper_count, 0)
        self.assertEqual(lower_count, 10)

if __name__ == "__main__":
    unittest.main()
