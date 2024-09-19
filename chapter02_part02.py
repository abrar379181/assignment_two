# Part 2: Caesar Cipher Decryption
def decrypt_caesar_cipher(encrypted_text, shift_amount):
    plain_text = ""
    for character in encrypted_text:
        if character.isalpha():
            # Handle uppercase letters
            if character.isupper():
                plain_text += chr((ord(character) - shift_amount - 65) % 26 + 65)
            # Handle lowercase letters
            elif character.islower():
                plain_text += chr((ord(character) - shift_amount - 97) % 26 + 97)
        else:
            plain_text += character
    return plain_text

# Example 	encoded_message
encoded_message = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VARPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAONG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URVYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Try all possible shifts (1 to 25)
attempted_decryptions = [(shift_amount, decrypt_caesar_cipher(encoded_message, shift_amount)) for shift_amount in range(1, 26)]

# Display the results
attempted_decryptions