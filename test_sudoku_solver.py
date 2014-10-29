"""     @author:            Guang Yang
        @mktime:            10/21/2014
        @description:       Tests for sudoku puzzle solver using basic
                            backtracking
"""
# import csv
from sudoku_solver import *     # NOQA


def build_example_in():
    return ['0', '3', '5', '2', '9', '0', '8', '6', '4',
            '0', '8', '2', '4', '1', '0', '7', '0', '3',
            '7', '6', '4', '3', '8', '0', '0', '9', '0',
            '2', '1', '8', '7', '3', '9', '0', '4', '0',
            '0', '0', '0', '8', '0', '4', '2', '3', '0',
            '0', '4', '3', '0', '5', '2', '9', '7', '0',
            '4', '0', '6', '5', '7', '1', '0', '0', '9',
            '3', '5', '9', '0', '2', '8', '4', '1', '7',
            '8', '0', '0', '9', '0', '0', '5', '2', '6']


def build_example_out():
    return ['1', '3', '5', '2', '9', '7', '8', '6', '4',
            '9', '8', '2', '4', '1', '6', '7', '5', '3',
            '7', '6', '4', '3', '8', '5', '1', '9', '2',
            '2', '1', '8', '7', '3', '9', '6', '4', '5',
            '5', '9', '7', '8', '6', '4', '2', '3', '1',
            '6', '4', '3', '1', '5', '2', '9', '7', '8',
            '4', '2', '6', '5', '7', '1', '3', '8', '9',
            '3', '5', '9', '6', '2', '8', '4', '1', '7',
            '8', '7', '1', '9', '4', '3', '5', '2', '6']


def build_short_example_in():
    return ['1', '3', '5',
            '9', '0', '2',
            '2', '3', '4']


def build_non_int_example_in():
    return ['a', '1', '0', '2', '9', '7', '8', '6', '4',
            '9', '8', '2', '4', '1', '6', '7', '5', '3',
            '7', '6', '4', '3', '8', '5', '1', '9', '2',
            '2', '1', '8', '7', '3', '9', '6', '4', '5',
            '5', '9', '7', '8', '6', '4', '2', '3', '1',
            '6', '4', '3', '1', '5', '2', '9', '7', '8',
            '4', '2', '6', '5', '7', '1', '3', '8', '9',
            '3', '5', '9', '6', '2', '8', '4', '1', '7',
            '8', '7', '1', '9', '4', '3', '5', '2', '6']


def build_non_0to9_example_in():
    return ['13', '1', '0', '2', '9', '7', '8', '6', '4',
            '9', '8', '2', '4', '1', '6', '7', '5', '3',
            '7', '6', '4', '3', '8', '5', '1', '9', '2',
            '2', '1', '8', '7', '3', '9', '6', '4', '5',
            '5', '9', '7', '8', '6', '4', '2', '3', '1',
            '6', '4', '3', '1', '5', '2', '9', '7', '8',
            '4', '2', '6', '5', '7', '1', '3', '8', '9',
            '3', '5', '9', '6', '2', '8', '4', '1', '7',
            '8', '7', '1', '9', '4', '3', '5', '2', '6']


def build_sparse_example_in():
    return ['0', '3', '0', '0', '0', '0', '0', '6', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '3',
            '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '9', '0', '0', '0', '3', '0', '0', '4', '0',
            '0', '0', '0', '0', '0', '4', '0', '0', '0',
            '0', '4', '3', '0', '0', '0', '0', '0', '0',
            '4', '0', '6', '5', '0', '0', '0', '0', '9',
            '3', '5', '0', '0', '0', '0', '0', '1', '0',
            '8', '0', '0', '0', '0', '0', '0', '2', '0']


def test_get_infeasible_set():
    """ testing get_infeasible_set is returning the correct values """

    sample_in_1 = build_example_in()
    sample_ind_1 = 16
    expect_1 = set(['6', '9', '4', '3', '7', '1', '2', '8'])
    result_1 = get_infeasible_set(sample_in_1, sample_ind_1)
    assert expect_1 == result_1

    sample_ind_2 = 77
    expect_2 = set(['7', '1', '5', '2', '8', '9', '4', '6'])
    result_2 = get_infeasible_set(sample_in_1, sample_ind_2)
    assert expect_2 == result_2

    sample_in_3 = build_sparse_example_in()
    sample_ind_3 = 80
    expect_3 = set(['3', '9', '2', '8', '1'])
    result_3 = get_infeasible_set(sample_in_3, sample_ind_3)
    assert expect_3 == result_3


def test_solve_sudoku():
    """ testing solve_sudoku is returning the correct values """

    expect_1 = build_example_out()
    result_1 = solve_sudoku(build_example_in())
    assert expect_1 == result_1


def test_check_sudoku():
    """ testing check_sudoku is returning the correct values """

    expect_1 = False
    result_1 = check_sudoku(build_short_example_in())
    short_sudoku_returns_false = expect_1 == result_1
    assert short_sudoku_returns_false

    expect_2 = False
    result_2 = check_sudoku(build_non_int_example_in())
    non_int_sudoku_returns_false = expect_2 == result_2
    assert non_int_sudoku_returns_false

    expect_3 = False
    result_3 = check_sudoku(build_non_0to9_example_in())
    non_0to9_sudoku_returns_false = expect_3 == result_3
    assert non_0to9_sudoku_returns_false

    expect_4 = True
    result_4 = check_sudoku(build_example_in())
    good_sudoku_returns_true = expect_4 == result_4
    assert good_sudoku_returns_true
