def generate_fibonacci(n):
    fibonacci_sequence = []
    if n <= 0:
        return fibonacci_sequence
    elif n == 1:
        fibonacci_sequence.append(0)
    elif n == 2:
        fibonacci_sequence.extend([0, 1])
    else:
        fibonacci_sequence.extend([0, 1])
        for i in range(2, n):
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
    return fibonacci_sequence

# Get input from user
try:
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    if n < 0:
        print("Please enter a positive integer.")
    else:
        # Generate Fibonacci sequence
        fibonacci_numbers = generate_fibonacci(n)
        # Print the Fibonacci sequence
        print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")
except ValueError:
    print("Invalid input! Please enter an integer value.")