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
        with open(code_path, "r", encoding="utf-8") as file:
            self.lines = file.readlines()  # Read all the lines of the code

        self.pointer = [0, 0]  # Create a pointer in the first line and first column

    def get_char(self):
        """
        Get the character in the pointer position

        Returns:
            char (str): The character in the pointer position
            pointer (list): The pointer position
        """
        # Verify if the pointer is in the end of the line
        if self.pointer[1] < len(self.lines[self.pointer[0]]):
            # Get the character in the pointer position
            char = self.lines[self.pointer[0]][self.pointer[1]]
            self.pointer[1] += 1
        else:
            # Check if there is a next line
            if self.pointer[0] < len(self.lines) - 1:
                self.pointer[0] += 1
                self.pointer[1] = 0
                return self.get_char()
            else:
                # If there is no next line, return None
                return None, self.pointer

        return char, self.pointer
