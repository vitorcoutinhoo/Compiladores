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

    # if the state is 0, the error is the character that is not recognized
    if state == "-":
        return "ERROR: UNRECOGNIZED TOKEN"

    return "ERROR:"
