def count_character_frequency(input_string):
    
    frequency_dict = {}
    
    
    for char in input_string:
       
        if char in frequency_dict:
            frequency_dict[char] += 1
        
        else:
            frequency_dict[char] = 1
    
    
    for char, frequency in frequency_dict.items():
        print(f"'{char}': {frequency}")


input_string = input("Enter a string: ")
count_character_frequency(input_string)