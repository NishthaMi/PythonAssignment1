def add_numbers(num1, num2):
    return num1 + num2

# Take input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calculate the sum
sum_result = add_numbers(number1, number2)

# Print the sum
print("The sum of {} and {} is: {}".format(number1, number2, sum_result))