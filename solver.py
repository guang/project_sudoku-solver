"""     @author:            Guang Yang
        @mktime:            10/21/2014
        @description:       Main script to execute the sudoku puzzle solver
"""
import numpy as np


# read data in and store as matrix
try:
    raw_csv = np.genfromtxt('test_cases/case2.csv', delimiter=',')
except:
    print("Error: Unable to load file, please input valid .csv file.")


# checks on the input
# 1) matrix must be side_len-side_len
# 2) entries must be 0-side_len
# 3)


# initializations
# var_len = side_len**3
# M = 4*side_len**2
# Aeq = np.zeros([M, N])
# beq = np.ones([M, 1])
# f = np.zeros(N)
# lb = np.zeros([side_len, side_len, side_len])
# ub = np.ones([side_len, side_len, side_len])


# def get_constr_depth(side_len):
# put rules into constraints (construct Aeq)
# 1) only 1 number for each point on the grid
#    for each (i,j), sum from 1 to side_len over k has to add up to one
side_len = 2
var_len = side_len**3
constr_depth = np.empty([side_len**2, var_len])
for i in range(side_len):
    for j in range(side_len):
        constr_temp = np.zeros([side_len, side_len, side_len])
        constr_temp[i, j, :] = 1
        constr_depth[i*side_len+j, :] = constr_temp.reshape([1, var_len])

# 2) rows contain 1-side_len each exactly once
#    for each (i,k), sum from 1 to side_len over j has to add up to one
side_len = 2
var_len = side_len**3
constr_depth = np.empty([side_len**2, var_len])
for i in range(side_len):
    for j in range(side_len):
        constr_temp = np.zeros([side_len, side_len, side_len])
        constr_temp[i, j, :] = 1
        constr_depth[i*side_len+j, :] = constr_temp.reshape([1, var_len])


# 3) columns contain 1-side_len each exactly once
#    for each (j,k), sum from 1 to side_len over i has to add up to one

# 4) each 3-by-3 grid contain 1-side_len each exactly once
#    for

# put clues into constraints (construct beq)


# solve via python-zibopt OR MAN UP AND CODE BRANCH N BOUND omg
