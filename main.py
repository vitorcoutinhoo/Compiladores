# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This is the main file of the project


# import the os module to list the files in the directory
import os

# import the classes and functions needed to run the project
from codes.reader_pointer import ReaderPointer
from codes.tokens import get_token
from codes.tables import TableTokens
from codes.error import Error


def main():
    """
    Main function of the project
    """

    # path of the input files
    PATH = "input"
    list_files = list_arquives(PATH)

    for arquive in list_files:
        # create the reader pointer
        pointer = ReaderPointer(f"{PATH}/{arquive}")

        # create the tables
        table = TableTokens()

        # create the error class
        error = Error()

        # open the file to write the tokens
        with open(f"logs/{arquive.replace(".cic", "")}.log", "w", encoding="utf-8") as file:
            token, lex, point, stt = get_token(pointer)  # get the first token

            # while the token is not the end of file
            while True:

                # ignore comments
                if token == "comment":
                    token, lex, point, stt = get_token(pointer)
                    continue

                # break the loop if the token is the end of file
                if token == "END OF FILE":
                    break

                # if the token is not recognized, verify the error
                if token == "ERROR":
                    error.verify_error(point, stt)
                else:
                    # append the token to the tables
                    table.main_table_append(point[0], point[1], token, lex)
                    table.count_table_append()

                # # write the token in the file
                # file.write(f"{token} --> {lex} | {point} {stt}\n")
                token, lex, point, stt = get_token(pointer)  # get the next token

            # write the tables in the file
            file.write(arquive + " LOGS: \n\n")

            if len(error.error) > 0:
                file.write("ERRORS FOUND IN CODE: \n")
                file.write(error.show_errors(f"{PATH}/{arquive}") + "\n\n")
            
            file.write("TABLE OF TOKENS: \n")
            file.write(table.print_main_table() + "\n\n")

            file.write("COUNT TABLE: \n")
            file.write(table.print_count_table() + "\n\n")

            # close the file
            file.close()

# list the files in the directory
def list_arquives(dir_path):
    """
    Function to list the files in the directory

    Args:
        dir_path (str): The path of the directory

    Returns:
        ar (list): The list of files in the directory
    """

    # verify if the directory exists
    if not os.path.isdir(dir_path):
        print("Directory not found")
        return

    # list the files in the directory that ends with .cic
    ar = os.listdir(dir_path)
    ar = [i for i in ar if i.endswith(".cic")]

    return ar

main()
