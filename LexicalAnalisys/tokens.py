# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This file contains the function to recognize the
# tokens of the language.

# import the functions to get the automaton and the reserved words
from reserved_words_and_automaton import get_automaton, get_reserved_words, get_final_states

# import the reader pointer class
from reader_pointer import ReaderPointer

# global variables
reserved_words = get_reserved_words() # get the reserved words
final_states = get_final_states() # get the final states of the automaton
automaton = get_automaton() # get the automaton
pointer = ReaderPointer(r"LexicalAnalisys\in_out\input_code.txt") # create the reader pointer
INITIAL_STATE = '0' # initial state of the automaton


def get_token(reader_pointer: ReaderPointer):
    """
    Function to get the next token in the input code

    Args:
        reader_pointer (ReaderPointer): The pointer to read the input code

    Returns:
        token (str): The token recognized
        pointer (list): The pointer position
    """

    char = verify_char_is_digit(reader_pointer.get_char()[0]) # get the first char of the input code
    state = automaton.loc[INITIAL_STATE, char] # get the transition from the initial state to the next state

    return state

def verify_char_is_digit(char: str):
    """
    Function to verify if a char is a digit

    Args:
        char (str): The char to verify

    Returns:
        char (str): if the char is not a digit
        char (int): if the char is a digit (0-9)
    """
    if char.isdigit():
        char = int(char)
    return char

print(get_token(pointer)) # test the function

    