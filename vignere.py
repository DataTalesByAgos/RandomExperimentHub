text = 'im testing if this works properly 1 2 3 ! - . @           done'
custom_key = 'test_keyword'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)].lower()  # Convert key_char to lowercase
            key_index += 1

            if key_char in alphabet:
                offset = alphabet.index(key_char)
                index = alphabet.find(char)
                new_index = (index + offset * direction) % len(alphabet)
                final_message += alphabet[new_index]
            else:
                # Handle case where key_char is not in the alphabet (though it should be)
                final_message += char  # Fallback to append the original character
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

encrypted_text = encrypt(text, custom_key)
print(f'Encrypted text: {encrypted_text}')

decrypted_text = decrypt(encrypted_text, custom_key)
print(f'Decrypted text: {decrypted_text}')

if decrypted_text == text:
    print('\nSuccessful encryption and decryption. The original message has been recovered correctly.')
else:
    print('\nError: The decrypted message does not match the original.')