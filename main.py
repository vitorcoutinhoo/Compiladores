# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This is the main file of the project

# import the reader pointer class
from codes.reader_pointer import ReaderPointer
from codes.tokens import get_token
from codes.tables import TableTokens

# create the reader pointer
pointer = ReaderPointer(r"in_out/input_code.txt")
table = TableTokens()


with open("in_out/tokens.txt", "w", encoding="utf-8") as file:
    token, lex, point = get_token(pointer)
    
    while token != "END OF FILE":
        table.main_table_append(point[0], point[1], token, lex)
        table.count_table_append()

        file.write(f"{token} --> {lex} | {point}\n")
        token, lex, point = get_token(pointer)

table.print_main_table()
print('\n\n\n')
table.print_count_table()
