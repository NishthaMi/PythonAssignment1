def string_to_list_using_comprehension(input_string):
    char_list = [char for char in input_string]
    return char_list


input_string = input("Enter a string: ")
characters = string_to_list_using_comprehension(input_string)
print("List of characters:", characters)