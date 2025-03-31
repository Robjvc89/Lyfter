import pytest


def bubble_sort(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Unit tests using pytest

# Test 1: Works with a small list
def test_small_list():
    # Arrange
    input_list = [5, 3, 8, 1, 2]
    
    # Act
    result = bubble_sort(input_list)
    
    # Assert
    assert result == [1, 2, 3, 5, 8]

# Test 2: Works with a large list
def test_large_list():
    # Arrange
    large_list = [i for i in range(100, 0, -1)]  # List of 100 elements in descending order
    
    # Act
    result = bubble_sort(large_list)
    
    # Assert
    assert result == list(range(1, 101))

# Test 3: Works with an empty list
def test_empty_list():
    # Arrange
    input_list = []
    
    # Act
    result = bubble_sort(input_list)
    
    # Assert
    assert result == []

# Test 4: Does not work with non-list parameters
@pytest.mark.parametrize("input_data", ["string", 123, None])
def test_invalid_input(input_data):
    # Arrange
    # Act & Assert
    with pytest.raises(ValueError):
        bubble_sort(input_data)