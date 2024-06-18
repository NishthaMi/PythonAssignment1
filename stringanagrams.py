def are_anagrams(string1, string2):
    
    cleaned_string1 = ''.join(string1.split()).lower()
    cleaned_string2 = ''.join(string2.split()).lower()
    
   
    if len(cleaned_string1 != len(cleaned_string2)):
        return False
    
    
    sorted_string1 = sorted(cleaned_string1)
    sorted_string2 = sorted(cleaned_string2)
    
    
    return sorted_string1 == sorted_string2


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")