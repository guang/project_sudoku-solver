"""     @author:            Guang Yang
        @mktime:            10/25/2014
        @description:       benchmark sudoku_solver on files in
                            benchmarking_data
"""
import os
import csv
import time
from sudoku_solver import *         # NOQA


def read_space_sep_sudoku(file_name):
    """ read sudoku files in .txt separated by spaces instead of commas """

    with open(file_name, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        raw_content = []
        for row in reader:
            raw_content += row[:9]

    return raw_content


def average_run_time(content, n_iter):
    """ average run_time for n_iter number of iterations

    Args:
        content (list):         content of the puzzle
        n_iter (int);             number of iterations to be run

    Returns:
        avg_run_time (float):       average run_time
    """

    run_time_record = [None]*n_iter

    for i in range(n_iter):
        t0 = time.clock()
        solve_sudoku(content)
        run_time_record[i] = time.clock() - t0

    return sum(run_time_record) / n_iter


if __name__ == '__main__':
    path_name = 'benchmarking_data/sudokus'
    files = os.listdir(path_name)
    for file_name in files:
        long_file_name = "{0}/{1}".format(path_name, file_name)
        content = read_space_sep_sudoku(long_file_name)

        avg_run_time = average_run_time(content, 20)
        with open('benchmarking_results.txt', 'a') as resultz:
            resultz.write("{}, {:.5f}\n".format(file_name, avg_run_time))
