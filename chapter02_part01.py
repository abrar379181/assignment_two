# Part 1: Separate string into numbers and letters, and convert to ASCII codes
def analyze_text(text_input):
    # Initialize variables to hold numbers and letters
    num_str = ""
    alpha_str = ""
    
    # Loop through the string to separate numbers and letters
    for character in text_input:
        if character.isdigit():
            num_str += character
        elif character.isalpha():
            alpha_str += character
    
    # Find even numbers and their ASCII codes
    even_digits_ascii = [ord(digit) for digit in num_str if int(digit) % 2 == 0]
    
    # Find uppercase letters and their ASCII codes
    capital_letters_ascii = [ord(letter) for letter in alpha_str if letter.isupper()]
    
    return num_str, alpha_str, even_digits_ascii, capital_letters_ascii

# Example input string
input_string = "56aAww1984sktr235270aYmn145ss785fsq31D0*"

# Process the string and get the results
num_str, alpha_str, even_digits_ascii, capital_letters_ascii = analyze_text(input_string)

num_str, alpha_str, even_digits_ascii, capital_letters_ascii