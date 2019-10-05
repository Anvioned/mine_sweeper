import random
import os
import time

class cell:
    '''Contains the main propertys of a cell'''

    def __init__(self):
        '''Sets default values of a cell

        is_opened(bool): False
        has_flag(bool): False
        has_mine(bool): False
        neightbour_mine_count(int): 0
        '''
        
        # Set default values for a new object
        self.is_opened = False
        self.has_flag = False
        self.has_mine = False
        self.neightbour_mine_count = 0
    
    def set_mine(self):
        '''Sets bomb if called

        Args:
        None

        Returns:
        (bool): If the mine was succesfully placed
        '''
        if self.has_mine == True:
            return False
        else:
            try:
                self.has_mine = True
                return True
            except:
                return False

    def set_flag(self):
        '''Sets flag is called

        Args:
        None
        '''

        self.has_flag = True

    def open_cell(self):
        '''Opens cell if called

        Args:
        None
        '''

        self.is_opened = True

    def set_neightbour(self, number):
        '''Calculates the amount of bombs next to it

        Args:
        number(int): number between 0 and 8 to how many bombs around it
        '''

        self.neightbour_mine_count = number
        
class gameSettings:
    '''Contains default game settings for the minesweeper game.
    Also gives the ability to change them

    col_amount(int): 10
    row_amount(int): 10
    mines_amount(int): 20
    game_over(bool): False
    '''

    def __init__(self):
        '''Defines default values of the game

        Args: None
        '''
        # Default values
        self.col_amount = 10
        self.row_amount = 10
        self.mine_amount = 20
        self.game_over = False

    def set_col_amount(self, col_amount):
        '''Sets the col_amount to a certain value

        Args:
        col_amount(int): Col amount
        '''

        self.col_amount = col_amount

    def set_row_amount(self, row_amount):
        '''Sets the row_amount to a certain value

        Args:
        row_amount(int): row amount
        '''

        self.row_amount = row_amount

    def set_mine_amount(self, mine_amount):
        '''Sets the bomb to a certain value

        Args:
        mine_amount(int): bomb amount
        '''

        self.mine_amount = mine_amount

    def found_mine(self):
        '''If the bomb is found then the  bomb amount goes down
        '''
        self.mine_amount -= 1
        
    def end_game(self):
        '''Ends the game
        '''

        self.game_over = True



def set_fields(settings):
    '''Sets the field by initializing all cells

    Args:
    col_amount(int): Amount of cells in colums
    row_amount(int): Amount of cells in rows

    Returns:
    Fields(list): List containing lists containing class
    '''
    fields = list()
    row_amount = settings.row_amount
    col_amount = settings.col_amount

    for row in range(0,(row_amount)):
        fields.append(list())
        for col in range(0,(col_amount)):
            fields[row].append(cell())

    return fields


def set_mines(settings, fields):
    '''Randomly places an amount of mines

    Args:
    settings: Variabele containing all the settings
    Fields(list): List containing lists containing class

    Returns:
    Fields(list): List containing lists containing class
    '''

    row_amount = settings.row_amount
    col_amount = settings.col_amount
    mines_amount = settings.mine_amount

    for mines_to_place in range(0, mines_amount):
        mine_placed = False
        while mine_placed == False:
            col_random = random.randrange(0, col_amount)
            row_random = random.randrange(0, row_amount)
            mine_placed = fields[col_random][row_random].set_mine()

    return fields
            
def set_neightbours(settings, fields):
    '''Looks where flags need to be placed
    
    Args:
    Settings: Variabele containing all the settings
    Fields(list): List containing lists containing class

    Returns:
    Fields(list): List containing lists containing class
    '''

    row_amount = settings.row_amount
    col_amount = settings.col_amount

    for row in range(0,(row_amount)):
        for col in range(0,(col_amount)):
            flag_number = 0
            try:
                if (fields[row-1][col]).has_mine == True:
                    flag_number += 1
            except:
                pass
            try:
                if (fields[row+1][col]).has_mine == True:
                    flag_number += 1
            except:
                pass
            try:
                if (fields[row][col-1]).has_mine == True:
                    flag_number += 1
            except:
                pass
            try:
                if (fields[row][col+1]).has_mine == True:
                    flag_number += 1
            except:
                pass
            try:
                if (fields[row+1][col-1]).has_mine == True:
                    flag_number += 1
            except:
                pass
            try:
                if (fields[row+1][col+1]).has_mine == True:
                    flag_number += 1
            except:
                pass
            try:
                if (fields[row-1][col+1]).has_mine == True:
                    flag_number += 1
            except:
                pass
            try:
                if (fields[row-1][col-1]).has_mine == True:
                    flag_number += 1
            except:
                pass

            fields[row][col].set_neightbour(flag_number)


    return fields
    
def show_fields(settings, fields):
    '''Looks where flags need to be placed
    
    Args:
    col_amount(int): Amount of cells in colums
    row_amount(int): Amount of cells in rows
    Fields(list): List containing lists containing class

    Returns:
    None
    '''
    # Clear field (linux / windows)
    os.system('cls' if os.name == 'nt' else 'clear')

    row_amount = settings.row_amount
    col_amount = settings.col_amount

    print('Your move:')

    for row in range(0,(row_amount)):
        for col in range(0,(col_amount)):
            if fields[row][col].is_opened == True:
                print('[{0:^1}]'.format(fields[row][col].neightbour_mine_count),end= '')
            elif fields[row][col].has_flag == True:
                print('[{0:^1}]'.format('F'),end= '')
            else:
                print('[{0:1}]'.format(' '),end= '')
        print()

def show_all_fields(settings, fields):
    '''Shows all fields
    this is for game over'''

    os.system('cls' if os.name == 'nt' else 'clear')

    row_amount = settings.row_amount
    col_amount = settings.col_amount

    for row in range(0,(row_amount)):
        for col in range(0,(col_amount)):
            if fields[row][col].has_mine == True:
                print('[{0:^1}]'.format('B'),end= '')
            elif fields[row][col].has_flag == True:
                print('[{0:^1}]'.format('F'),end= '')
            else:
                print('[{0:^1}]'.format(fields[row][col].neightbour_mine_count),end= '')
        print()


def calculate_user_action(user_col, user_row, user_action, fields):
    '''Calculates what to do with the user action

    user_col(int): Colum that user chose
    user_row(int): Row that user chose
    user_action(str): Action that user chose

    '''

    if user_action == 'placeFlag':
        fields[user_col-1][user_row-1].set_flag()
        return fields, settings
    elif user_action == 'open':
        if fields[user_col-1][user_row-1].has_mine == True:
            settings.end_game()
            return fields, settings
        elif fields[user_col-1][user_row-1].is_opened == False:
            fields[user_col-1][user_row-1].open_cell()
            # TODO: Make is open more neighbourign cells
        else:
            # TODO: Tell the user to actually do something
            pass
    
    return fields, settings

def user_key():
    '''Gets input from keyboard
    
    Args:
    None
    
    Returns:
    user_col
    user_row
    user_action
    '''

    try:
        user_col = int(input('Please select a column: '))
    except:
        print('You failed to select an actual column')

    try:
        user_row = int(input('Please select a row: '))
    except:
        print('You failed to select an actual Row')
    
    try:
        user_action = input('Please select an action: ')
    except:
        print('You failed to select an actual action')

    return user_col, user_row, user_action

def int_game():
    '''Initialises the game
    '''

    settings = gameSettings()
    fields = set_fields(settings)
    fields = set_mines(settings, fields)
    fields = set_neightbours(settings, fields)
    show_fields(settings, fields)

    return fields, settings

def start_game(fields, settings):
    while settings.game_over == False:
        user_col, user_row, user_action = user_key()
        fields, settings = calculate_user_action(user_col, user_row, user_action, fields)
        show_fields(settings, fields)

    print('Game over')
    show_all_fields(settings, fields)
    time.sleep(30)

fields, settings = int_game()
start_game(fields, settings)