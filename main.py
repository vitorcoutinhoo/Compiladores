# import the reader pointer class
from reader_pointer import ReaderPointer
from tokens import get_token

# create the reader pointer
pointer = ReaderPointer(r"in_out/input_code.txt")

with open(r"in_out/tokens.txt", "w", encoding="utf-8") as file:
    token, lex, pnt = get_token(pointer)
    while token != "END OF FILE":
        file.write(f"{token} --> {lex} {pnt}" + "\n")
        token, lex, pnt = get_token(pointer)