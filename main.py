# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This is the main file of the project

# import the classes and functions needed to run the project
from codes.reader_pointer import ReaderPointer
from codes.tokens import get_token
from codes.tables import TableTokens
from codes.error import verify_error

# create the reader pointer
pointer = ReaderPointer(r"in_out/input_code.txt")

# create the tables
table = TableTokens()

# open the file to write the tokens
with open("in_out/tokens.txt", "w", encoding="utf-8") as file:
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
            token = verify_error(point, stt)
        else:
            # append the token to the tables
            table.main_table_append(point[0], point[1], token, lex)
            table.count_table_append()

        # write the token in the file
        file.write(f"{token} --> {lex} | {point} {stt}\n")
        token, lex, point, stt = get_token(pointer)  # get the next token

table.print_main_table()
print("\n")
table.print_count_table()
