import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    characters = lowercase

    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_special:
        characters += special_characters

    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

password = generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True)
print("Generated password:", password)
