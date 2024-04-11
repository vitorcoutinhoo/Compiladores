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
pointer = ReaderPointer(r"Lexical-Analyzer/in_out/input_code.txt")

def get_token(reader: ReaderPointer):
    """
    Function to get the next token in the input code

    Args:
        reader (ReaderPointer): The pointer to read the input code

    Returns:
        token (str): The token recognized
        pointer (list): The pointer position
    """
    initial_state = "0"  # initial state of the automaton

    # get the first char of the input code
    char = verify_char_is_digit(reader.get_char(reader.pointer)[0])

    # get the next char of the input code if the char is \t, \n or blank
    while (char == "\t") or (char == "\n") or (char == " "):
      char = verify_char_is_digit(reader.get_char(reader.pointer)[0])
  
    # create the lexema with the first char
    lexema = str(char)

    # if the fist char is None, return the token not recognized
    if char is None:
      return "END OF FILE", lexema

    # get the transition from the initial state to the next state
    state = automaton.loc[initial_state, char]

    # if the state is not recognized, return the token not recognized
    if state == "-":
        return "ERROR: TOKEN NOT RECOGNIZED", lexema

    # while the char is not None
    while char is not None:
        
        # if the lexema is a reserved word
        if lexema in reserved_words:  
            return f"TK_{lexema}"  # return the reserved word

        # if the state is a final state, return the token recognized
        if state in final_states:
            if state in back_states:
                reader.pointer[1] -= 1  # return the pointer to the last char
                lexema = lexema[:-1]
            return final_states[state], lexema  # return the token recognized

        # get the next char
        char = verify_char_is_digit(reader.get_char(reader.pointer)[0])

        # while the char is blank, stay in the same state
        aux = state
        while char == " ":
            state = aux
            char = verify_char_is_digit(reader.get_char(reader.pointer)[0])

        # add the char to the lexema
        lexema += str(char)

        # get the next state
        state = automaton.loc[state, char]

        # if the state is not recognized, return the token not recognized
        if state == "-":
            return "ERROR: TOKEN NOT RECOGNIZED", lexema

    return "ERROR: TOKEN NOT RECOGNIZED", lexema  # return if the token is not recognized


def verify_char_is_digit(char: str):
    """
    Function to verify if a char is a digit

    Args:
        char (str): The char to verify

    Returns:
        char (str): if the char is not a digit
        char (int): if the char is a digit (0-9)
    """

    if char is not None and str(char).isdigit():
        char = int(char)

    return char


with open(r"Lexical-Analyzer/in_out/tokens.txt", "w", encoding="utf-8") as file:
    token, lex = get_token(pointer)
    while token != "END OF FILE":
        file.write(f"{token} --> {lex}" + "\n")
        token, lex = get_token(pointer)
  