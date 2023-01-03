# Importing threading module.
import threading


# Global variable for the input string.
input_string = ""


# Function for the input thread.
def input_thread():
    try:
        global input_string
        input_string = input("\nEnter a string: ")
        print("\nInput string:", input_string)

    except EOFError:
        print("Input thread terminated!")


# Function for the reverse thread.
def reverse_thread():
    global input_string
    reversed_string = input_string[::-1]

    print("Reversed string:", reversed_string)


# Function for the capital thread.
def capital_thread():
    global input_string
    capital_string = input_string.upper()

    print("Capitalized string:", capital_string)


# Function for the shift thread
def shift_thread():
    global input_string
    shift_string = ""

    for char in input_string:
        # To check if the character is a letter or a lowercase.
        if char.isalpha() and char.islower():
            shift_string += chr(ord(char) + 2)

        else:
            shift_string += char

    print("Shifted string:", shift_string)


# Main Code.
if __name__ == '__main__':
    # Creating the threads
    t1 = threading.Thread(target=input_thread)
    t2 = threading.Thread(target=reverse_thread)
    t3 = threading.Thread(target=capital_thread)
    t4 = threading.Thread(target=shift_thread)

    # Starting the threads
    t1.start()
    t1.join()

    t2.start()
    t3.start()
    t4.start()

    # Wait for the threads to complete
    t2.join()
    t3.join()
    t4.join()
