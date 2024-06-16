def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
result = check_even_odd(number)

# Print the result
print("The number {} is {}.".format(number, result))