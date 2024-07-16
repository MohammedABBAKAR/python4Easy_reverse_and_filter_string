# Task
# Given a string str, reverse it and omit all non-alphabetic characters.

# Example
# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

# Input/Output
# [input] string str


def reverse_and_filter_string(s):
    filtered_chars = []
    
    # Filtrer les caractères alphabétiques
    for char in s:
        if char.isalpha():
            filtered_chars.append(char)
    
    # Inverser la liste des caractères filtrés
    filtered_chars.reverse()
    
    # Joindre les caractères pour former la chaîne finale
    reversed_string = ''.join(filtered_chars)
    
    return reversed_string

# Cas de test
print(reverse_and_filter_string("krishan"))



# def reverse_and_filter_string(s):
#     # Step 1: Filter out non-alphabetic characters
#     filtered_string = ''.join(char for char in s if char.isalpha())
#     # Step 2: Reverse the filtered string
#     reversed_string = filtered_string[::-1]
#     return reversed_string

# # Test cases
# print(reverse_and_filter_string("krishan"))