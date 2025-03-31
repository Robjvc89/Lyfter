import pytest

def sort_words(string):
    word_list = string.split('-')  # Split the string by hyphen
    word_list.sort()  # Sort the list of words
    sorted_string = '-'.join(word_list)  # Join the sorted list back into a string
    return sorted_string

# Test cases using pytest

def test_sort_words_with_normal_case():
    # Arrange: Prepare the string with unsorted words
    text = "python-variable-function-computer-monitor"
    
    # Act: Call the sort_words function with this string
    result = sort_words(text)
    
    # Assert: Verify that the words are correctly sorted
    assert result == "computer-function-monitor-python-variable"

def test_sort_words_with_single_word():
    # Arrange: Prepare a string with a single word
    text = "sun"
    
    # Act: Call the sort_words function with this string
    result = sort_words(text)
    
    # Assert: Verify that the result is the same single word
    assert result == "sun"

def test_sort_words_with_multiple_hyphens():
    # Arrange: Prepare a string with multiple hyphens and words
    text = "cat-dog-bird-apple"
    
    # Act: Call the sort_words function with this string
    result = sort_words(text)
    
    # Assert: Verify that the words are correctly sorted
    assert result == "apple-bird-cat-dog"

def test_sort_words_with_empty_string():
    # Arrange: Prepare an empty string
    text = ""
    
    # Act: Call the sort_words function with the empty string
    result = sort_words(text)
    
    # Assert: Verify that the result is also an empty string
    assert result == ""

def test_sort_words_with_same_word_repeated():
    # Arrange: Prepare a string with repeated words
    text = "apple-apple-apple"
    
    # Act: Call the sort_words function with this string
    result = sort_words(text)
    
    # Assert: Verify that the repeated word remains the same
    assert result == "apple-apple-apple"

# To run the tests with pytest, use the following command in the terminal:
# pytest test_script.py
