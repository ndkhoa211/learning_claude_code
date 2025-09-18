def fibonacci(n):
    """Calculate the nth Fibonacci number using iterative approach."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(count):
    """Generate a list of the first 'count' Fibonacci numbers."""
    sequence = []
    for i in range(count):
        sequence.append(fibonacci(i))
    return sequence


def main():
    # Calculate individual Fibonacci numbers
    print("Individual Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")

    print("\nFirst 15 Fibonacci numbers:")
    sequence = fibonacci_sequence(15)
    print(sequence)

    # Interactive input
    try:
        n = int(input("\nEnter a number to calculate its Fibonacci value: "))
        result = fibonacci(n)
        print(f"F({n}) = {result}")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()