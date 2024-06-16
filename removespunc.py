import string

def remove_punctuation(input_string):
    
    translator = str.maketrans('', '', string.punctuation)
   
    no_punctuation_string = input_string.translate(translator)
    return no_punctuation_string


input_string = input("Enter a string: ")
clean_string = remove_punctuation(input_string)
print("String without punctuation:", clean_string)