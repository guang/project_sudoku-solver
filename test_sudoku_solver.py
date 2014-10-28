"""     @author:            Guang Yang
        @mktime:            10/21/2014
        @description:       Tests for sudoku puzzle solver using basic
                            backtracking
"""
# import csv
from sudoku_solver import *     # NOQA


def build_sample_in():
    return ['0', '3', '5', '2', '9', '0', '8', '6', '4',
            '0', '8', '2', '4', '1', '0', '7', '0', '3',
            '7', '6', '4', '3', '8', '0', '0', '9', '0',
            '2', '1', '8', '7', '3', '9', '0', '4', '0',
            '0', '0', '0', '8', '0', '4', '2', '3', '0',
            '0', '4', '3', '0', '5', '2', '9', '7', '0',
            '4', '0', '6', '5', '7', '1', '0', '0', '9',
            '3', '5', '9', '0', '2', '8', '4', '1', '7',
            '8', '0', '0', '9', '0', '0', '5', '2', '6']


def test_get_infeasible_set():
    sample_in = build_sample_in()
    sample_ind = 16
    expect = set(['6', '9', '4', '3', '7', '1', '2', '8'])
    result = get_infeasible_set(sample_in, sample_ind)
    assert expect == result
