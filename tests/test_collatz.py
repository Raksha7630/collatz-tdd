#Running testing file first to fail the code.

#I am Rakshya Shrestha.
#I am testing the collatz function from collatz.py file.

import pytest 
from src.collatz import collatz_sequence

def test_collatz_example():
    #Following AAA pattern.
    #Arrange
    n = 12 #input value
    expected = [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]

    #Act
    result = collatz_sequence(n)

    #Assert
    assert result == expected

    