# pylint: disable = C0114, C0301, C0206, C0200, C0303

# Author: Vítor Coutinho
# This file is used to create the 
# tables used in the project

class TableTokens():
    """
    This class create the tables with the recognized tokens
    """

    def __init__(self):
        """
        Constructor of the class
        """
        self.main_table = [] # Create the main table
        self.count_table = [] # Create the count table
    
    def main_table_append(self, row, column, token, lexeme):
        """
        Append the token in the main table

        Args:
            token (str): The token
            lexeme (str): The lexeme
            row (int): The row of the token
            column (int): The column of the token
        """
        if token == 'comment':
            return

        if token not in ('TK_ID', 'TK_INT', 'TK_FLOAT', 'TK_DATA', 'TK_END', 'TK_CADEIA'):
            lexeme = ''

        for i in range(len(self.main_table)):
            if self.main_table[i][0] == row:
                row = ''
               

        aux = [row, column, token, lexeme]
        self.main_table.append(aux)
    
    def count_table_append(self):
        """
        Append the tokens in the count table
        """

        count_dict = {}
        for row in self.main_table:
            token = row[2]
            if token in count_dict:
                count_dict[token] += 1
            else:
                count_dict[token] = 1

        self.count_table = [[token, count] for token, count in count_dict.items()]
        

    def print_main_table(self):
        """
        Print the table
        """
        header = ('+' + '-' * 5 + '+' + '-' * 5 + '+' + '-' * 15 + '+' + '-' * 22 + '+' + '\n' +
                   '|' + ' '  + 'ROW' + ' '  + '|' + ' '  + 'COL' + ' '  + '|' + ' ' * 2 + 'TOKEN' + ' ' * 8 + '|' + ' ' * 3 + 'LEXEMA' + ' ' * 13 + '|' + '\n' +
                   '+' + '-' * 5 + '+' + '-' * 5 + '+' + '-' * 15 + '+' + '-' * 22 + '+' + '\n')

        body = []
        for row in self.main_table:
            body.append(f"| {row[0]:>3} | {row[1]:>3} | {row[2]:<13} | {row[3]:<20} |" + '\n' + '+' + '-' * 5 + '+' + '-' * 5 + '+' + '-' * 15 + '+' + '-' * 22 + '+')
        
        print(header + '\n'.join(body))

    def print_count_table(self):
        """
        Print the count table
        """

        header = ('+' + '-' * 15 + '+' + '-' * 11 + '+' + '\n' + 
                  '|' + ' ' * 2 + 'TOKEN' + ' ' * 8 + '|' + ' ' * 3 + 'USOS' + ' ' * 4 + '|' + '\n' + 
                  '+' + '-' * 15 + '+' + '-' * 11 + '+' + '\n')
        
        body = []
        for row in self.count_table:
            body.append(f"| {row[0]:<13} | {row[1]:>9} |" + '\n' + '+' + '-' * 15 + '+' + '-' * 11 + '+')

        print(header + '\n'.join(body))

