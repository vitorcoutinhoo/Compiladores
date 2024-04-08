# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This file contains the function to recognize the
# tokens of the language.

# import the functions to get the automaton and the reserved words
from reserved_words_and_automaton import (
    get_automaton,
    get_reserved_words,
    get_final_states,
    get_back_states,
)

# import the reader pointer class
from reader_pointer import ReaderPointer

# global variables
reserved_words = get_reserved_words()  # get the reserved words
final_states = get_final_states()  # get the final states of the automaton
back_states = get_back_states()  # get the back states of the automaton
automaton = get_automaton()  # get the automaton

# create the reader pointer
pointer = ReaderPointer(r"LexicalAnalisys\in_out\input_code.txt")
INITIAL_STATE = "0"  # initial state of the automaton


def get_token(reader_pointer: ReaderPointer):
    """
    Function to get the next token in the input code

    Args:
        reader_pointer (ReaderPointer): The pointer to read the input code

    Returns:
        token (str): The token recognized
        pointer (list): The pointer position
    """

    # get the first char of the input code
    char = verify_char_is_digit(reader_pointer.get_char(reader_pointer.pointer)[0])
    lexema = str(char)

    if char is None:
        return "Token not recognized"

    if char == " ":
        char = verify_char_is_digit(reader_pointer.get_char(reader_pointer.pointer)[0])

    # get the transition from the initial state to the next state
    state = automaton.loc[INITIAL_STATE, char]

    # while the char is not None
    while char is not None:

        if lexema in reserved_words:  # if the lexema is a reserved word
            return f"TK_{lexema}"  # return the reserved word

        if state in final_states:
            if state in back_states:
                reader_pointer.pointer[1] -= 1  # return the pointer to the last char
                lexema = lexema[:-1]
            return final_states[state]  # return the token recognized

        char = verify_char_is_digit(reader_pointer.get_char(reader_pointer.pointer)[0])
        lexema += str(char)

        if char == " ":
            char = verify_char_is_digit(
                reader_pointer.get_char(reader_pointer.pointer)[0]
            )

        state = automaton.loc[state, char]

    return "Token not recognized"  # return if the token is not recognized


def verify_char_is_digit(char: str):
    """
    Function to verify if a char is a digit

    Args:
        char (str): The char to verify

    Returns:
        char (str): if the char is not a digit
        char (int): if the char is a digit (0-9)
    """

    if (char is not None) & str(char).isdigit():
        char = int(char)

    return char


with open(r"LexicalAnalisys\in_out\tokens.txt", "w", encoding="utf-8") as file:
    token = get_token(pointer)
    while token != "Token not recognized":
        file.write(token + "\n")
        token = get_token(pointer)
