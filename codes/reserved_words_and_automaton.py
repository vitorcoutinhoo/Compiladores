# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This file contains the reserved words and the automaton
# used in the lexical analysis.

# import pandas to facilitate the creation of the automaton
import pandas as pd


def get_reserved_words():
    """
    Function to get the reserved words of the language

    Returns:
        reserved_words (list): List with the reserved words
    """

    reserved_words = [
        "rotina",
        "fim_rotina",
        "se",
        "senao",
        "imprima",
        "leia",
        "para",
        "enquanto",
    ]
    return reserved_words


def get_automaton():
    """
    Function to get the automaton used in the lexical analysis

    Returns:
        automaton (dataframe): The automaton used in the lexical analysis
    """

    # symbols regonized by the automaton
    digits = [i for i in range(10)]
    letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    operators = ["+", "-", "~", "*", "%", "=", "<", ">", "&", "|"]
    signals = ['"', "_", "#", "\n"]
    separators = ["(", ")", ".", ":", "/", " ", "\t"]

    # all symbols --> dataframe column names
    columns = digits + letters + operators + signals + separators

    # Create a automaton from a dictionary
    data = {}  # dictionary to store the transitions
    with open(r"automaton/automaton.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.split()
            data[line[0]] = line[1:]  # add the transitions to the dictionary

    # create the automaton using a data frame with the dictionaty and the columns
    automaton = pd.DataFrame(data, index=columns).T

    return automaton


def get_final_states():
    """
    Function to get the final states of the automaton and
    the respectives tokens.
    """

    # create a dictionary with the final states and the respectives tokens
    states = {
        "3": "TK_END",
        "6": "TK_FLOAT",
        "10": "TK_INT",
        "21": "TK_DATA",
        "27": "TK_CADEIA",
        "31": "TK_ID",
        "33": "comment",
        "36": "TK_COLON",
        "37": "TK_NOT",
        "38": "TK_SUM",
        "39": "TK_MULT",
        "40": "TK_DIV",
        "41": "TK_AND",
        "42": "TK_OR",
        "44": "TK_EQUAL",
        "46": "TK_NEG",
        "47": "TK_GT_EQ",
        "50": "TK_OP_PAR",
        "51": "TK_CL_PAR",
        "55": "TK_LESS_THAN",
        "56": "TK_ATT",
        "57": "TK_DIFF",
        "59": "comment",
        "61": "TK_LESS_EQUAL",
        "62": "TK_GT_THAN",
    }

    return states


def get_back_states():
    """
    Function to get the back states of the automaton
    """

    return ["3", "6", "10", "31", "35", "61", "62"]


# any time if the automaton.txt is changed, the df.txt will be updated
at = get_automaton()
with open(r"automaton/df.txt", "w", encoding="utf-8") as files:
    files.write(at.to_string())
