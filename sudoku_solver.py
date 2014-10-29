"""     @author:            Guang Yang
        @mktime:            10/21/2014
        @description:       Main script to execute the sudoku puzzle solver
                            using basic backtracking
"""
from __future__ import print_function
from math import floor
import time
import csv
import sys


def read_sudoku(file_name):
    """ Read the given file line by line, storing values in a list.

    Args:
        file_name (str):    name of the csv file to read data in

    Returns:
        raw_content (list):    content of the file stored in a list

    Exceptions:
        if failed to read the file (file not found), return empty list
    """

    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            raw_content = []
            for row in reader:
                raw_content += row
        return raw_content
    except:
        print("Failed to read the file specified: {0}".format(file_name))
        return []


def check_sudoku(raw_content):
    """ Check the content of the file for formatting errors or anomalies

    1) length of the list is 81
    2) contains only 0-9

    Args:
        raw_content (list):     content of the file, list of strings

    Returns:
        is_correct_format (bool):   True if format is correct, else False
    """

    if len(raw_content) != 81:
        return False

    for i in raw_content:
        if i not in '0123456789':
            return False

    return True


def get_infeasible_set(cell_val_all, cell_ind):
    """ Computes the set of values this blank cell (whose index is cell_ind)
    cannot take due to restrictions from existing entries on the same row,
    column and block.

    Args:
        cell_val_all (list):    Current value of each cell (0 is blank) stored
                                in a 81 items long list.
        cell_ind (int):         Index of the current blank cell that we are
                                trying to put a value in. (0 to 8)

    Returns:
        infeasible_set (set):   the set of infeasible values.

    Example:
        >>> get_infeasible_set(cell_val_all, 5)
        {1, 2, 5, 9}
    """
    col_ind = cell_ind % 9
    col_list = cell_val_all[col_ind::9]
    row_ind = cell_ind - cell_ind % 9
    row_list = cell_val_all[row_ind:row_ind+9]
    block_row_ind = int(floor(cell_ind / 27))
    block_col_ind = int(floor(cell_ind % 9 / 3))
    block_ind = 27*block_row_ind + 3*block_col_ind  # starting index for block
    block_list = []
    for i in [block_ind, block_ind+9, block_ind+18]:
        block_list += cell_val_all[i:i+3]

    infeasible_set = set(col_list + row_list + block_list)
    if '0' in infeasible_set:
        infeasible_set.remove('0')
    return infeasible_set


def solve_sudoku(cell_val_all):
    """ recursively solve sudoku puzzle using backtracking

    Args:
        cell_val_all (list):        unsolved puzzle stored as list of strings

    Returns:
        solved_sudoku (list):       solved puzzle stored as list of strings
    """

    try:
        cell_ind = cell_val_all.index('0')
    except ValueError:
        return cell_val_all

    infeasible_set = get_infeasible_set(cell_val_all, cell_ind)

    for new_val in '123456789':
        if new_val not in infeasible_set:
            solved_sudoku = solve_sudoku(cell_val_all[:cell_ind] + [new_val] +
                                         cell_val_all[cell_ind+1:])
            if solved_sudoku is not None:
                return solved_sudoku
    return None


def write_sudoku(cell_val_all, file_name):
    """ writes the solved sudoku to specified file """

    with open(file_name, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for row in range(9):
            writer.writerow(cell_val_all[row*9:row*9+9])


def print_sudoku(cell_val_all):
    """ pretty print sudoku puzzle given its content stored as a list """
    print('-'*21)
    for i in range(9):
        for j in range(9):
            # The 'end' argument in print() is a known bug in pyflakes
            # use NOQA to suppress warning from pyflakes
            print(cell_val_all[9 * i + j] + ' ', end='')    # NOQA
            if (j+4) % 9 == 0 or (j+7) % 9 == 0:
                print('| ', end='')     # NOQA
        print('')
        if (i+1) % 3 == 0:
            print('-'*21)


def save_sudoku(solved_sudoku, input_file_name):
    """ Asks user whether/where to save the solved sudoku. If user chooses to
    save the file with specified name, call write_sudoku(). If the file name
    cannot be saved to, call write_sudoku() with a  default file name.

    Args:
        solved_sudoku (list):       content of the solved sudoku as a list
        input_file_name (str):      file_name used to read the input file. this
                                    is used to make the default output file_name
    """

    is_save = get_input("Would you like to save the results to a separate file "
                        "(y/n)? ")
    if is_save in ('y', 'yes', 'Y', 'Yes'):
        user_file_name = get_input("Please name the file (e.g. my_sud.csv): ")
        try:
            write_sudoku(solved_sudoku, user_file_name)
            print("File successfully saved to."
                  "{0}".format(user_file_name))
        except:
            default_file_name = "solved_{0}".format(input_file_name)
            print("Could not save to the specified file name, instead "
                  "it is saved to {0}".format(default_file_name))
            write_sudoku(solved_sudoku, default_file_name)
    print_end_msg()


def print_wrong_format():
    """ prints error message when input format is wrong """
    print("Unable to properly parse given csv file, please check its "
          "content to make sure it is in the correct format: a 9 by 9 "
          "'matrix' with each element ranging from 0 to 9 (0 meaning "
          "blank) separated by comma, like this:\n"
          "0,0,1,0,0,0,8,0,0\n"
          "0,5,0,0,1,0,0,4,0\n"
          "0,0,0,2,0,0,0,0,7\n"
          "0,0,7,0,0,5,0,8,0\n"
          "4,0,0,0,6,0,0,0,9\n"
          "0,2,0,4,0,0,5,0,0\n"
          "3,0,0,0,0,7,0,0,0\n"
          "0,7,0,0,2,0,0,9,0\n"
          "0,0,4,0,0,0,1,0,0\n")


def print_end_msg():
    print("Thanks for using Guang's sudoku solver! Questions/comments"
          " are welcome at gy8@berkeley.edu")


def main(file_name):
    """ reads and checks user specified unsolved sudoku, prints and solves it,
    finally saves it based on user instructions

    Args:
        file_name (str):            name of the file to read in and parse

    Returns:
        solved_sudoku (list):       content of the solved sudoku as a list,
                                    empty if not solved
    """

    raw_content = read_sudoku(file_name)
    is_correct_format = check_sudoku(raw_content)
    if is_correct_format:
        cell_val_all = raw_content
    else:
        print_wrong_format()
        return []

    print("Here's the unsolved sudoku puzzle you picked:")
    print_sudoku(cell_val_all)

    print("Running Backtracking Solver...")

    t0 = time.clock()
    solved_sudoku = solve_sudoku(cell_val_all)
    print("Successfully solved in {:.3f} seconds\n"
          "Here's the solved puzzle".format(time.clock()-t0))
    print_sudoku(solved_sudoku)
    return solved_sudoku


if __name__ == "__main__":
    # Supports Python 2 and 3 input
    # Defaults to Python 3 input()
    get_input = input
    # If Python 2 detected, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    # Check for number of inputs
    # case1: no arguments -> ask for input_file_name
    if len(sys.argv) == 1:
        raw_file_name = get_input("Welcome to Guang's sudoku solver! What's "
                                  "the name of the unsolved sudoku csv file? "
                                  "(if you don't have one, try typing "
                                  "example.csv)\n")
        solved_sudoku = main(raw_file_name)
        if len(solved_sudoku) == 81:
            save_sudoku(solved_sudoku, raw_file_name)

    # case2: 1 argument -> run main
    elif len(sys.argv) == 2:
        solved_sudoku = main(sys.argv[1])
        if len(solved_sudoku) == 81:
            save_sudoku(solved_sudoku, sys.argv[1])

    # case3: 2 arguments -> treat input 1 as input_file_name and input 2
    #                       as output_file_name
    elif len(sys.argv) == 3:
        solved_sudoku = main(sys.argv[1])
        try:
            write_sudoku(sys.argv[2])
            print_end_msg()
        except:
            print("Unable to write file to {0}".format(sys.argv[2]))

    else:
        print("Too many input arguments: Try running 'python sudoku_solver.py "
              "example.csv'")
