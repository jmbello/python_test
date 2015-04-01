# Valida nombre de usuario segun parametros...

is_valid_name = False
while not is_valid_name:
    name = input("Enter name: ")
    if len(name) < 6 or len(name) > 12:
        print("name cannot be less than 6 or greater than 12")
    elif not name.isalnum():
        print("name must be written with numbers or caracters")
    else:
        is_valid_name = True
print ("name successful, welcome %s" %name)