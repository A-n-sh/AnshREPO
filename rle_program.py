from console_gfx import ConsoleGfx


def menu_display():

    #prints welcome message
    print("Welcome to the RLE image encoder!")
    print()
    print("Displaying Spectrum Image: ")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow) #displays rainbow


def to_hex_string(data):
    letter = "" #sets letter as empty string

    for i in range(0, len(data)):

    #runs through the whole string
    #checks for numbers and replaces them with corresponding letters and adds them to the string
    #if numbers are less than 10 then it simply adds to the string

        if data[i] < 10:
            letter = letter + str(data[i])

        if data[i] == 10:
            letter = letter + "a"

        if data[i] == 11:
            letter = letter + "b"

        if data[i] == 12:
            letter = letter + "c"

        if data[i] == 13:
            letter = letter + "d"

        if data[i] == 14:
            letter = letter + "e"

        if data[i] == 15:
            letter = letter + "f"

    return letter


def count_runs(flat_data):

    count = 1 #sets variable count to 1

    for i in range(1, len(flat_data)):

        if flat_data[i] != flat_data[i - 1]: #if the index is not equal to the index before it the count increases
            count += 1

    return count


def encode_rle(flat_data):

    rle_data = [] #defines empty list
    count = 1 #sets count value
    special = 0 #sets special value

    for i in range(1, len(flat_data)):

        if flat_data[i] == flat_data[i - 1]: #if the value doesn't equal the previous value, count and special increase
            count += 1
            special += 1

            if special == 15: #when special value reaches 15 it makes a special case with 15 of one value and resets counts.
                rle_data.extend([15, flat_data[i - 1]])
                count = 1
                special = 0

        else:
            rle_data.extend([count, flat_data[i - 1]]) #extends list to account for normal values
            count = 1
            special = 0

    rle_data.extend([count, flat_data[-1]])
    return rle_data


def get_decoded_length(rle_data):

    length = 0 #sets variable length to 0

    for i in range(0, len(rle_data), 2):
        length += rle_data[i] #adds 1 for each value in the list

    return length


def decode_rle(rle_data):

    decode_data = [] #defines empty list

    for i in range(0, len(rle_data), 2):

        count = int(rle_data[i]) #count is the current index
        val = int(rle_data[i + 1]) #val is the le
        decode_data.extend([val] * count)

    return decode_data


def string_to_data(data_string):

    character = list(data_string)
    updated_list = []

    for i in range(len(data_string)): #searches list for specific letters and assigns numbers

        if character[i] == "a" or character[i] == "A":
            updated_list.append(10)

        if character[i] == "b" or character[i] == "B":
            updated_list.append(11)

        if character[i] == "c" or character[i] == "C":
            updated_list.append(12)

        if character[i] == "d" or character[i] == "D":
            updated_list.append(13)

        if character[i] == "e" or character[i] == "E":
            updated_list.append(14)

        if character[i] == "f" or character[i] == "F":
            updated_list.append(15)

        if character[i].isdigit():
            updated_list.append(int(character[i]))

    return updated_list


def to_rle_string(rle_data):

    rle_string = ""  # defines empty string

    for i in range(0, len(rle_data), 2): #runs through string from 0 to length skipping every two steps

        rle_string += str(rle_data[i])
        rle_string += hex(rle_data[i + 1])[-1]

        if (i != len(rle_data) - 2): #adds delimiter ":" with rle_string
            rle_string += ":"

    return rle_string


def string_to_rle(rle_string):

    rle_list = [] #defines empty list
    index = rle_string.split(":") #remvoes : and gives list

    for element in index:

        length = int(element[0:-1]) #takes length value out of element string
        value = int(element[-1], 16) #takes value out of element string

        #adds length and value values to the rle_list
        rle_list.append(length)
        rle_list.append(value)

    return rle_list


if __name__ == '__main__':
    menu_display()
    user_input = 0
    image_data = None


    while True:
        # prints table as well as options
        print("RLE Menu")
        print("-" * 8)
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data")
        print()

        user_input = int(input("Select a Menu Option: ")) #prompts user for input
        if user_input == 0:

            break

        if user_input == 1:

            file_name = input("Enter name of file to load: ") # Load and store image data from file
            image_data = ConsoleGfx.load_file(file_name)

        if user_input == 2:

            print("Test image data loaded.") # Load and store test image from file
            image_data = ConsoleGfx.test_image

        if user_input == 3:

            rle_string = input("Enter an RLE string to be decoded: ") #prompt for string
            image_data = decode_rle(string_to_rle(rle_string))

        if user_input == 4:

            data_string = input("Enter the hex string holding RLE data: ") #prompt for string
            image_data = decode_rle(string_to_data(data_string))

        if user_input == 5:

            image_data = input("Enter the hex string holding flat data: ") #prompt for string

        if user_input == 6:

            print("Displaying image...")
            ConsoleGfx.display_image(image_data) #displays image

        if user_input == 7:
            # calls the encode_rle and to_rle_string functions
            print("RLE representation: ", to_rle_string(encode_rle(image_data)))


        if user_input == 8:
            #calls the encode_rle and to_hex_string function
            print("RLE hex values: ", to_hex_string(encode_rle(image_data)))


        if user_input == 9:

            rand_var = "" #defines empty string

            for j in range(len(image_data)):

                rand_var += str(image_data[j]) #adds to rand_var
            print("Flat hex values: ", rand_var)
