import pytest

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If divisible by any number other than 1 and itself, it's not prime
            return False
    return True  


def filter_primes(lst):
    prime_list = []  
    for number in lst:  
        if is_prime(number):  # Check if the number is prime
            prime_list.append(number)  
    return prime_list

# Test cases using pytest

def test_is_prime_with_prime_number():
    # Arrange: Prepare a prime number
    num = 7
    
    # Act: Call the is_prime function with this number
    result = is_prime(num)
    
    # Assert: Verify that the number is prime
    assert result == True

def test_is_prime_with_non_prime_number():
    # Arrange: Prepare a non-prime number
    num = 6
    
    # Act: Call the is_prime function with this number
    result = is_prime(num)
    
    # Assert: Verify that the number is not prime
    assert result == False

def test_filter_primes_with_mixed_numbers():
    # Arrange: Prepare a list with mixed numbers
    numbers = [1, 4, 6, 7, 13, 9, 67]
    
    # Act: Call the filter_primes function with this list
    result = filter_primes(numbers)
    
    # Assert: Verify that the filtered prime numbers are returned
    assert result == [7, 13, 67]

def test_filter_primes_with_empty_list():
    # Arrange: Prepare an empty list
    numbers = []
    
    # Act: Call the filter_primes function with this empty list
    result = filter_primes(numbers)
    
    # Assert: Verify that the result is an empty list
    assert result == []

def test_filter_primes_with_no_primes():
    # Arrange: Prepare a list with no prime numbers
    numbers = [1, 4, 6, 8]
    
    # Act: Call the filter_primes function with this list
    result = filter_primes(numbers)
    
    # Assert: Verify that the result is an empty list since there are no prime numbers
    assert result == []

# To run the tests with pytest, use the following command in the terminal:
# pytest test_script.py
