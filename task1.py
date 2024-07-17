def caching_fibonacci():
    cache = {}

    # Inner function for Fibonacci calculation.
    def fibonacci(n):
        # Base cases.
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # Check if the number is already in the cache.
        if n in cache:
            return cache[n]

        # Recursive case.
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Return the inner function.
    return fibonacci


# Example usage:
# Get the fibonacci function
fib = caching_fibonacci()

# We use the fibonacci function to calculate Fibonacci numbers
print(fib(10))  # Output: 55
print(fib(15))  # Output: 610
