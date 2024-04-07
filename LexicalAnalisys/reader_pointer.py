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

    def get_char(self):
        """
        Get the character in the pointer position

        Returns:
            char (str): The character in the pointer position
            pointer (list): The pointer position
        """

        # Verify if the file is empty
        if self.lines == []:
            return "This file is empty"

        line = self.lines[self.pointer[0]] # Get the line
    
        # Verify if the pointer of column is in the line
        if self.pointer[1] < len(line):
            char = line[self.pointer[1]] # Get the character
        else:
            self.pointer[0] += 1 # Go to the next line
            self.pointer[1] = 0 # Go to the first column

            # Verify if the pointer of line is in the file
            if self.pointer[0] < len(self.lines):
                next_line = self.lines[self.pointer[0]] # Get the next line
                char = next_line[self.pointer[1]] # Get the first character of the next line

            else:
                char = None # Return none if the pointer is out of the file


        self.pointer[1] += 1 # Go to the next column
        return char, self.pointer

