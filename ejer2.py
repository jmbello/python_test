# Validacion de contraseñas

def has_lower(word):
    for letter in word:
        if letter.islower():
            return True
    return False

def has_digit(word):
    for letter in word:
        if letter.isdigit():
            return True
    return False

def has_space(word):
    for letter in word:
        if letter.isspace():
            return True
    return False

is_valid_password = False
while not is_valid_password:
    password = input("Enter password: ")
    if len(password) < 8:
        print("error, password is short, try new one")
    elif not has_lower(password):
        print("error, password has not any caracter in lower case")
    elif not has_digit(password):
        print("error, password must contain a digit")
    elif has_space(password):
        print("error, password musnt contain blank spaces")
    else:
        is_valid_password = True
print("New password has been accepted...")