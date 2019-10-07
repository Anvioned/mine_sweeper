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
        '''Sets flag if called

        Args:
        None
        '''

        self.has_flag = True

    def unset_flag(self):
        '''Removed flag if called

        Args:
        None
        '''

        self.has_flag = False       

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
        '''If a flag is placed on a bomb the bomb count goes down
        '''
        self.mine_amount -= 1

    def unfound_mine(self):
        '''If a flag is removed the bomb count goes up
        '''
        self.mine_amount += 1
        
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

    # BUG: Bombs are sometimes not calculates correctly

    for row in range(0,(row_amount)):
        for col in range(0,(col_amount)):
            flag_number = 0

            # Trying and catching the IndexErrors here because I have to
            # The fields will almost always be out of index on the sides
            try:
                if (fields[row-1][col]).has_mine == True:
                    flag_number += 1
            except IndexError:
                pass
            try:
                if (fields[row+1][col]).has_mine == True:
                    flag_number += 1
            except IndexError:
                pass
            try:
                if (fields[row][col-1]).has_mine == True:
                    flag_number += 1
            except IndexError:
                pass
            try:
                if (fields[row][col+1]).has_mine == True:
                    flag_number += 1
            except IndexError:
                pass
            try:
                if (fields[row+1][col-1]).has_mine == True:
                    flag_number += 1
            except IndexError:
                pass
            try:
                if (fields[row+1][col+1]).has_mine == True:
                    flag_number += 1
            except IndexError:
                pass
            try:
                if (fields[row-1][col+1]).has_mine == True:
                    flag_number += 1
            except IndexError:
                pass
            try:
                if (fields[row-1][col-1]).has_mine == True:
                    flag_number += 1
            except IndexError:
                pass

            fields[row][col].set_neightbour(flag_number)


    return fields
    
def show_fields(settings, fields):
    '''Looks where flags need to be placed
    9
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


def calculate_user_action(user_col, user_row, user_action, fields, settings):
    '''Calculates what to do with the user action

    user_col(int): Colum that user chose
    user_row(int): Row that user chose
    user_action(str): Action that user chose

    '''
    

    if user_action == 'flag':
        if fields[user_col-1][user_row-1].has_flag == False:
            fields[user_col-1][user_row-1].set_flag()
            if fields[user_col-1][user_row-1].has_mine == True:
                settings.found_mine()
        elif fields[user_col-1][user_row-1].has_flag == True:
            fields[user_col-1][user_row-1].unset_flag()
            if fields[user_col-1][user_row-1].has_mine == True:
                settings.unfound_mine()
            
        
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
            print("Man stop fucking with the program, enter an actual option.")
    
    return fields, settings

def program_start():
    '''Asks user what they want to do, start game, or change settings

    Args:
    None

    Returns:
    None
    '''

    settings = gameSettings()
    print("Starting the game can be done by typing: start")
    print("To change the settings type settings")


    while True:
        user_choice = input("Please choose an option: ")

        if user_choice.lower() == 'start':
            fields, settings = int_game(settings)
            start_game(fields, settings)
            break # Breaking here so the game ends when they exit this loop
        elif user_choice.lower() == 'settings':

            print("mine_amount")
            print("col_amount")
            print("row_amount")
                 
            # TODO: Make the settings menu a bit more efficient than this crap
            user_setting_choice = input("Please choose setting you want to change: ")
            if user_setting_choice.lower() == 'mine_amount':
                try:
                    user_amount = int(input("Please enter the amount: "))
                    settings.set_mine_amount(user_amount)
                except:
                    print("Please enter valid input")
            elif user_setting_choice.lower() == 'col_amount':
                try:
                    user_amount = int(input("Please enter the amount: "))
                    settings.set_col_amount(user_amount) 
                except:
                    print("Please enter valid input")                    
            elif user_setting_choice.lower() == 'row_amount':
                try:
                    user_amount = int(input("Please enter the amount: "))
                    settings.set_row_amount(user_amount)
                except:
                    print("Please enter valid input")
            else:
                print("Please select an actual setting")

        else:
            print("Please enter valid input.")


def user_key():
    '''Gets input from keyboard
    
    Args:
    None
    
    Returns:
    user_col
    user_row
    user_action
    '''
    while True:
        try:
            user_col = int(input('Please select a column: '))
            break
        except:
            print('You failed to select an actual column')
    while True:
        try:
            user_row = int(input('Please select a row: '))
            break
        except:
            print('You failed to select an actual Row')
    while True:
        try:
            print("Actions are flag and open.")
            user_action = input('Please select an action: ')
            break
        except:
            print('You failed to select an actual action')

    return user_col, user_row, user_action

def int_game(settings):
    '''Initialises the game

    Args:
    settings(class): Stuff full of settings
    '''
    
    fields = set_fields(settings)
    fields = set_mines(settings, fields)
    fields = set_neightbours(settings, fields)
    show_fields(settings, fields)

    return fields, settings

def start_game(fields, settings):
    '''The main loop where the game starts and ends ultimately'''

    while settings.game_over == False:
        user_col, user_row, user_action = user_key()
        fields, settings = calculate_user_action(user_col, user_row, user_action, fields, settings)
        show_fields(settings, fields)
        if settings.mine_amount == 0:
            print("You won! Congratz")
            break
    print('Game over')
    show_all_fields(settings, fields)
    time.sleep(30)

program_start()


# DONE: TODO: Make it so you can actually win the game instead of it just constantly asking you stuff
# DONE: TODO: Change setFlag to flag so you can also remove flags
# TODO: Make a GUI so you can either right click or left click for opening and placing flags
# TODO: Make it so first bomb cant kill you
