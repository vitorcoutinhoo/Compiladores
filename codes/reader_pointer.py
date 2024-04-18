# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This file contain the pointer used to read
# the input code.


class ReaderPointer:
    """
    This class create a pointer to read the input code
    """

    def __init__(self, code_path: str):
        """
        Constructor of the class
        """
        # Open the file
        with open(code_path, "r", encoding="utf-8") as file:
            self.lines = file.readlines() # Read all the lines of the file

        self.pointer = [0, 0]  # Create a pointer in the first line and first column

    def get_char(self, pointer_list: list):
        """
        Get the character in the pointer position

        Args:
            pointer_list (list): The pointer position

        Returns:
            char (str): The character in the pointer position
            pointer (list): The pointer position
        """

        # Get the row and column of the pointer
        row, column = pointer_list

        # Verify if the file is empty
        if self.lines == []:
            return "This file is empty"
        
        # If the column is bigger than the line, go to the next line
        if column >= len(self.lines[row]):
            row += 1
            column = 0

        # Verify if the pointer is in the end of the file
        if row == len(self.lines):
            return None, []

        # Get the character in the pointer position
        char = self.lines[row][column]
        column += 1
        
        self.pointer = [row, column]
        return char, self.pointer
