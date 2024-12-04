
def add_numbers(numbers):
    return sum(numbers)


def subtract_numbers(numbers):
    if len(numbers) < 2:
        return "Error: Need at least two numbers for subtraction."
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiply_numbers(numbers):
    if len(numbers) < 2:
        return "Error: Need at least two numbers for multiplication."
    result = 1
    for num in numbers:
        result *= num
    return result


def average(numbers):
    if len(numbers) < 1:
        return "Error: Need at least one number for average."
    return sum(numbers) / len(numbers)


def factorial(number):
    if number < 0:
        return "Error: Factorial of a negative number is not defined."
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def sort_numbers(numbers, descending=False):
    """Sort the numbers in ascending or descending order."""
    return sorted(numbers, reverse=descending)
