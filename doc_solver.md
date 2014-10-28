### Sudoku Solver Documentation
This page details my approach to solving the problem


#### Executive Summary

The task of this code challenge is to implement a sudoku puzzle solver that takes in a csv file
of an unsolved sudoku puzzle and outputs a csv file with solved sudoku.

Solving sudoku puzzles
using computer programs is not a new idea. Thus before writing any code, I first conducted a
brief literature review on existing popular approaches and algorithms to solve sudoku puzzles.
This
allowed me to examine the *pros and cons* of different methods in order to pick the one most
appropriate for this code challenge.

Having decided to take the backtracking approach for its simplicity, I chose to implement
the solver in Python for both its *readability* and flexibility. [ADD DETAILS ABOUT THE ALGO]

Lastly, to evaluate my solver against other approaches, I collected and tested 46 benchmark
sudoku instances with varying levels of difficulty. [TEST OTHER ALGOS IF HAVE TIME, OTHERWISE
REWORD THIS PARAGRAPH]

#### Literature Review
A quick search on the internet yields the following popular algorithms to solving the problem:


- Backtracking
An iterative approach that tries 

- Brute-force
Here we try all possible 

- Exact-cover

- Stochastic search

- Constraint programming

- **Integer Programming**

  Lastly, we can also pose the problem as a binary integer program. In order to use constraints
  to describe rules like "each row must contain numbers 1 to 9 exactly once", we have to add a
  third dimension (that uses position in the vector and a binary switch to indicate the number
  on the grid).
  This turns the number of variables from 81 (on the 9-by-9 grid) to 729 (on the 9-by-9-by-9
  array).

  This turns out to be an overkill for this code challenge. If we think about this carefully,
  we realize that the objective function for this optimization problem will be 0 as we are only
  interested in feasbility (and there is no optimality). This implies that the branch and bound
  algorithm (which we would use to solve the IP) would reduce down to really just good ole
  backtracking. Furthermore, in terms of computations, we see that using brute force trying all
  possible combinations (which is not what we do, but nevertheless a proxy for actual complexity
  ) we have 9\*\*81 for regular backtracking and 2\*\*729 for this IP formulation. since
  2\*\*729 >> 9\*\*81, there is no obvious benefits to using branch and bound.


#### Model Approach
After considering the pro/con of each algorithm and my own background, I decided to use the
integer programming approach due to
- ability to exploit existing (IP) solvers
- elegant formulation using linear algebra
- performance gaurantees as an integer program


#### Assumptions
- input puzzle must have at least 17 entries (


#### Formulation
In order to set up the binary integer program, we need to construct its components one by one:

- Variable (x)

  Here we have a vector of 9\*9\*9=729 components that represent a 9 by 9 by 9 tensor (3
  dimensional matrix). For this tensor, the 2D matrix formed by *i* and *j* components
  is the sudoko grid while the 3rd dimension represents numeric val

- Objective function (f)
This 


#### Testing
Minimal tests are written to test the logics and some benchmark cases. Using `py.test`, we
simply type
```
py.test test_sudoku_solver.py
```
in terminal to run the tests.


#### Error Handling

- In addition to checking the size (it must be a 9 by 9 grid), value (must be integers from 1
to 9), and 




#### Usage





#### Benchmarking



#### References

- http://lipas.uwasa.fi/~timan/sudoku/
- http://en.wikipedia.org/wiki/Sudoku_solving_algorithms
- http://norvig.com/sudoku.html
- http://www.mathworks.com/company/newsletters/articles/solving-sudoku-with-matlab.html
- http://freepythontips.wordpress.com/2013/09/01/sudoku-solver-in-python/
