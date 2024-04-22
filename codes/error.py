# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This is the file to verify and show the errors in the code

class Error:
    """
    Class to verify and show the errors in the code
    """

    def __init__(self):
        self.error = []  # list to store the errors


    # function to verify the error
    def verify_error(self, pointer, state):
        """
        Function to verify the error in the code

        Args:
            pointer (list): The pointer position
            state (str): The state of the automaton

        Returns:
            error (str): The error message
        """

        # if the state is '-', the error is the character that is not recognized
        if state == "-":
            self.error.append(["Unrecognized token", pointer])
        
        if state == "34":
            self.error.append(["Reserved word not recognized", pointer])
        
        if state == 20:
            self.error.append(["Bad date formatting", pointer])
        
        if state == 27:
            self.error.append(["String not closed", pointer])
        
        if state == 31:
            self.error.append(["Identifier not recognized", pointer])


    def show_errors(self, path):
        """
        Function to show the errors in the code

        Args:
            path (str): The path of the file
        
        Returns:
            error_output: The errors in the code
        """

        error_output = ""
        with open(path, "r", encoding="utf-8") as file:
            code = file.readlines()
            for i, line in enumerate(code):
                error_output += (f"[ {i+1}]  {line}") # print the lines of input code

                # show the errors in the line
                errors_on_line = [err for err in self.error if err[1][0] == i+1]
                for err in errors_on_line:
                    error_output += (f"{' ' * 5}{'-' * err[1][1]}^" + "\n")
                for err in errors_on_line:
                    error_output += (f"{' ' * 5}Error at line {err[1][0]}, column {err[1][1]}: {err[0]}" + "\n")
    
        return error_output
            
