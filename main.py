def encode(password):

    encoded = "" # initializes an empty string

    for element in password:

        if element == "7":

            encoded += "0"

        elif element == "8":

            encoded += "1"

        elif element == "9":

            encoded += "2"

        else:
            encoded += str(int(element) + 3) # runs through every element of the password and edits it

    return encoded

# decode written by Sophie Ruetschi
def decode(password_input_list):
    newPass = ""

    for char in password_input_list:
        res = int(char) - 3
        newPass += str(res)

    return newPass

def main():

    initial_password = "" # initializes an empty sting for the initial password
    encoded_password = ""

    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        menu_option = int(input("Please enter an option: "))# prompts user for input

        if menu_option == 1:

            print("Please enter your password to encode: ",end="")
            initial_password = input()
            encoded_password = encode(initial_password)# encodes the user inputted password

            print("Your password has been encoded and stored!")

        elif menu_option == 2:

            if len(initial_password) == 0: # checks if initial password is empty

                print("No password encoded yet. Please use Option 1.")
                continue# re loops and asks for user input again

            else:
                print(encoded_password)
                decoded_password = decode(encoded_password)# implement the decode function here
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")


        elif menu_option == 3:
            break # breaks

        else:
            print("This isn't a valid option! Please try again.\n") # prompts user to enter valid option

if __name__ == '__main__':
    main()
