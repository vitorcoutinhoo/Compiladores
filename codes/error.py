# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This is the file to verify and show the errors in the code


# function to verify the error
def verify_error(pointer, state):
    """
    Function to verify the error in the code

    Args:
        pointer (list): The pointer position
        state (str): The state of the automaton

    Returns:
        error (str): The error message
    """

    # if the state is '-', the error is the character that is not recognized
    if state == "-":
        return "ERROR: UNRECOGNIZED TOKEN"

    return "ERROR:"

def show_errors():
    """
    Function to show the errors in the code
    """
    with open("in_out/input_code.txt", "r", encoding="utf-8") as file:
        code = file.readlines()
        for i, line in enumerate(code):
            print(f"[ {i+1}]  {line.strip("\n")}")



