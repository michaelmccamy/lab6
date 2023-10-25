def menu():
    print("Menu\n1. Encode\n2. Decode\n3. Quit\n")

def main():
    program_run = True
    while program_run is True:
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            encode()
        elif user_input == 2:
            decode()
        else:
            program_run is False

def encode():
    encoded_password = ""
    user_password = input("Please enter your password: ")
    for char in user_password:
        new_digit = int(char) + 3
        if new_digit >= 10:
            new_digit -= 10
        else:
            pass
        encoded_password = encoded_password + str(new_digit)
    return encoded_password



