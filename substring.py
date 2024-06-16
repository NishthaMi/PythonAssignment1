main_string = input("Enter the main string: ")


substring = input("Enter the substring: ")


if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")