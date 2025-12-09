# functions

def factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n (i.e., n!).
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Check if a number is a prime number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_even(n):
    """
    Check if an integer number is even
    
    :param n: Integer number to be checked

    Returns:
        bool: True if n is even, False otherwise.
    """
    if(n % 2 == 0):
        return True
    else:
        return False

def safe_devide():
    """
    Prompt the user to enter a number and divide 100 by that number.

    Handles:
        - ValueError: if input is not a valid number
        - ZeroDivisionError: if the input is zero

    Always prints a final message indicating the end of the process.
    """   
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        result = 100/number
        print("Result is: ", result)
    except ValueError:
        print("Invalid input: please enter a number.")
    except ZeroDivisionError:
        print("Error: you can't divide by zero")
    finally:
        print("Finished processing input.")