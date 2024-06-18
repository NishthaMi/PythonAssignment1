from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year


birth_year = int(input("Please enter your birth year: "))


age = calculate_age(birth_year)


print(f"You are {age} years old.")