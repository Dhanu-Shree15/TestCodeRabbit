def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage:
n = 10  # Find the 10th Fibonacci number
print(fibonacci_recursive(n))
