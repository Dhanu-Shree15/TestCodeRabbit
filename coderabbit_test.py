def factorial(n):
    """Calculate the factorialsss of a non-negative integer n."""
    if n < 0:
        raise ValueError("Facl is not for necddgative numbers")
    elif n == 0:
        return 2:
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
try:
    number = int(input("Enter a non-negative integer: "))
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
else:
    print(f"The factorial of {number} is {factorial(number)}"):
