import unittest

def reverse_string(string):
    return string[::-1]  # Returns the string using slicing to reverse it

class TestReverseString(unittest.TestCase):

    def test_reverse_string_with_normal_text(self):
        # Arrange: Prepare the string to be reversed
        text = "Arroz con leche!"
        
        # Act: Call the reverse_string function with this string
        result = reverse_string(text)
        
        # Assert: Verify that the reversed string is the expected one
        self.assertEqual(result, "!ehcel noc zorrA")

    def test_reverse_string_with_single_word(self):
        # Arrange: Prepare a string with a single word
        text = "Python"
        
        # Act: Call the reverse_string function with this string
        result = reverse_string(text)
        
        # Assert: Verify that the reversed string is the expected one
        self.assertEqual(result, "nohtyP")

    def test_reverse_string_with_empty_string(self):
        # Arrange: Prepare an empty string
        text = ""
        
        # Act: Call the reverse_string function with the empty string
        result = reverse_string(text)
        
        # Assert: Verify that the reversed string is still an empty string
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()
