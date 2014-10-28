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
        file_name (str):    name of the file to read data in

    Returns:
        cell_
    """
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        cell_val_all = []
        for row in reader:
            cell_val_all += row
    return cell_val_all


def check_sudoku(cell_val_all):
    pass


def get_infeasible_set(cell_val_all, cell_ind):
    """ Computes the set of values this blank cell (whose index is cell_ind)
    cannot take due to restrictions from existing entries on the same row,
    column and block.

    Args:
        cell_val_all (list):    Current value of each cell (0 is blank) stored
                                in a 81 items long list.
        cell_ind (int):         Index of the current blank cell that we are
                                trying to a value in. (0 to 8)

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
    with open(file_name, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for row in range(9):
            writer.writerow(cell_val_all[row*9:row*9+9])


def print_sudoku(cell_val_all):
    print('-'*21)
    for i in range(9):
        for j in range(9):
            print(cell_val_all[9 * i + j] + ' ', end='')    # NOQA
            if (j+4) % 9 == 0 or (j+7) % 9 == 0:
                print('| ', end='')     # NOQA
        print('')
        if (i+1) % 3 == 0:
            print('-'*21)


def save_sudoku(solved_sudoku, file_name):
    is_save = get_input("Would you like to save the results to a separate file "
                        "(y/n)? ")
    if is_save in ('y', 'yes', 'Y', 'Yes'):
        print("")
        user_file_name = get_input("Please name the file (e.g. my_sud.csv): ")
        try:
            write_sudoku(solved_sudoku, user_file_name)
            print("File successfully saved.")
        except:
            default_file_name = "solved_{0}".format(file_name)
            print("Could not save to the specified file name, instead "
                  "it is saved to {0}".format(default_file_name))
            write_sudoku(solved_sudoku, default_file_name)
    print("Thanks for using Guang's sudoku solver! Questions/comments"
          "are welcome at gy8@berkeley.edu")


def main(file_name):
    cell_val_all = read_sudoku(file_name)

    print("Here's the unsolved sudoku puzzle you picked:")
    print_sudoku(cell_val_all)

    print("Running Backtracking Solver...")

    t0 = time.clock()
    solved_sudoku = solve_sudoku(cell_val_all)
    print("Successfully solved in {:.3f} seconds\n"
          "Here's the solved puzzle".format(time.clock()-t0))
    print_sudoku(solved_sudoku)

    save_sudoku(solved_sudoku, file_name)


if __name__ == "__main__":
    # Supports Python 2 and 3 input
    # Defaults to Python 3 input()
    get_input = input

    # If Python 2 detected, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        raw_file_name = get_input("Welcome to Guang's sudoku solver! What's "
                                  "the name of the unsolved sudoku csv file? "
                                  "(if you don't have one, try typing "
                                  "example.csv)\n")
        main(raw_file_name)
