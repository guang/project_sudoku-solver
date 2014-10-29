Guang's Sudoku Solver
=====================

submission for insight data engineering coding challenge (Jan 2015 session)

## Table of Cntents
- [Quick Start](#quick-start)
  - [Usage](#usage)
  - [Dependencies](#dependencies)
- [Project Documentation](#project-documentation)
  - [Executive Summary](#executive-summary)
  - [Literature Review](#literature-review)
  - [Algorithm Implementation](#algorithm-implementation)
  - [Testing](#testing)
  - [Existence and Uniqueness](#existence-and-uniqueness)
  - [Python Version Compatibility](#python-version-compatibility)
  - [Benchmarking](#benchmarking)
- [References](#references)


## Quick Start
With an input csv file consisting of an unsolved sudoku (on a 9 by 9 grid) with 0's
representing blanks, Guang's sudoku solver tries to find a feasible solution via backtracking
and save the solved sudoku to a separate csv file.

### Usage
This program is designed to be flexible with different kinds of inputs, specifically:

- No inputs:

  ```python
  python sudoku_solver.py
  ```

  Here the user can type the name of their input csv file after the welcome prompt

- 1 input:

  ```python
  python sudoku_solver.py example.csv
  ```

  Where `example.csv` is the unsolved sudoku puzzle in .csv format

- 2 inputs:

  ```python
  python sudoku_solver.py example.csv solved_example.csv
  ```

  Where `example.csv` is the unsolved sudoku puzzle in .csv format and `solved_example.csv`
  is the name of the file to store the output from the algorithm.


### Dependencies
- [Python](https://www.python.org): 2.7 or 3.4



## Project Documentation
This section details my approach to designing and implementing the sudoku solver


### Executive Summary

The task of this code challenge is to implement a sudoku puzzle solver that takes in a csv file
of an unsolved sudoku puzzle and outputs a csv file with solved sudoku. Three design criteria
are especially important: 

1. clean formulation and implementation of the algorithm
2. technical trade-offs are considered and justified
3. great user experience

Solving sudoku puzzles
using computer programs is not a new idea. Thus before writing any code, I first conducted a
brief literature review on existing popular approaches and algorithms to solve sudoku puzzles.
This
allowed me to examine the *pros and cons* of different methods in order to pick the one most
appropriate for this code challenge.

Having decided to take the recursive backtracking approach for its simplicity, I chose
to implement
the solver in Python for both its *readability* and flexibility. In order to deliver a *great
user experience*, a lot of effort is spent on

1. enabling the user to have varying levels of interaction with the program (multiple
   I/O methods)
2. making error messages informative and helpful
3. creating useful intermediate reports (pretty-printing the sudoku and recording runtime).

Lastly, to evaluate my solver, I collected and tested 46 benchmark sudoku instances with
varying levels of difficulty. The results show that this simple solver solves sudoku puzzles
with competitive run time.

### Literature Review
A quick search on the internet yields the following popular algorithms to solving the problem:


- **Backtracking**

  By iterating over all possible solutions, the algorithm rolls back to a preview solution
  when the current solution leads to a dead end.

  Due to the brute force nature of the algorithm, it can be slower comparing to other
  algorithms, however, it is clearly the **best approach for this project**, where
  simplicity and conciseness
  in implementation details is valued over computation time.

- **Integer Programming**

  Having studied applied mathematics, the most obvious method was to pose the problem as a 
  binary integer program. In order to use constraints
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
  ) we have 9^81 for regular backtracking and 2^729 for this IP formulation. since
  2^729 >> 9^81, there is no obvious benefits to using branch and bound.

- **Exact Cover**

  This can be done using constraints, very much similar to the integer programming approach.
  Like integer programming, this would involve using libraries that can work well with
  large (sparse) matrices, namely Numpy, and a industrial-strength solver (sampling space is
  a lot larger so it makes no sense to use brute-force)

- **Stochastic search**

  This method works by randomly assigning numbers to blank cells and calculate the number
  of errors to figure out a direction to move to reduce the errors down to zero.

  This sounds like a really interesting idea and it could outperform the other algorithms
  for edge or really hard cases due to its stochastic nature. However, due to the lack
  of experience with stochastic search, I decided not to go with this method.



### Algorithm Implementation
Having decided backtracking is the best way to go, I further used recursion to make
the codes more readable. Here's the pseudocode for this approach:

```python
  if 'already at a solution':
    return 'the value'
  'pick an empty cell'
  for 'every feasible choice at this cell':
    'make the choice for the cell and take a step along the path'
    'invoke recursion to solve the problem from this point'
    if 'recursive call succeeds'
      return 'solutions to the next higher level'
  else:
    'backtrack to previous state'
```


### Testing
Minimal tests are written to test the logics and some edge cases. They are stored in
`test_sudoku_solver.py` using simple assert statements. Using [pytest](pytest.org/), we
simply type
```
py.test test_sudoku_solver.py
```
in terminal and the tests will be automatically collected and ran.


### Existence and Uniqueness
From [literature](http://mathworld.wolfram.com/Sudoku.html), we know that there is no
uniqueness guarantees unless we exhaustively explore all possibilities for sudoku puzzles
less than 17 clues.

As such, an algorithm that uses backtracking, like mine, cannot guarantee uniqueness of
solution - instead it returns an element from the set of feasible solutions.

Because of the exhaustive nature of this algorithm, it will find a solution if there is
at least one solution to the given puzzle.


### Python Version Compatibility
The codes are developed in Python 3.4. To ensure a smooth user experience, I added the
following features to provide backward compatability for Python 2.7 in `sudoku_solver.py`:

- using `__future__` package, I make sure 2.7 users are using the python 3 print() function.

- when the module is ran directly, I check for the python version and use `input` or
  `raw_input` accordingly.



### Benchmarking
A set of 46 benchmarking sudoku instances are derived from a
[paper](lipas.uwasa.fi/~timan/sudoku) published in IEEE WCCI 2008 on *Solving and Analyzing
Sudokus with Cultural Algorithms*.

I run my algorithm on all 46 instances for 20 times each to get the average computation
time. I then compared my results to the cultural algorithm described in the paper.

**Important: Please keep in mind that I did not run the algorithm from the paper on my machine
(which has better specs), so the purpose of this comparison is to show trends, not to show
the absolute difference in speeds**

Here are some examples:

<table>
  <tr>
    <th>File Name</th>
    <th>Puzzle Difficulty</th>
    <th>Guang's Sudoku Solver run time</th>
    <th>Cultural Algorithm run time</th>
  </tr>
  <tr>
    <td>s10a.txt</td>
    <td>Easy</td>
    <td>0.01301</td>
    <td>0.428</td>
  </tr>
  <tr>
    <td>s11a.txt</td>
    <td>Medium</td>
    <td>0.27099</td>
    <td>2.280</td>
  </tr>
  <tr>
    <td>s11b.txt</td>
    <td>Medium</td>
    <td>0.18505</td>
    <td>7.874</td>
  </tr>
  <tr>
    <td>s12a.txt</td>
    <td>Hard</td>
    <td>0.01285</td>
    <td>34.015</td>
  </tr>
  <tr>
    <td>s12b.txt</td>
    <td>Hard</td>
    <td>0.03943</td>
    <td>3.436</td>
  </tr>
</table>

Albeit my solver is ran on a better machine, these results show that it solves the problems in very reasonable time.



### References

- http://mathworld.wolfram.com/Sudoku.html
- http://lipas.uwasa.fi/~timan/sudoku/
- http://en.wikipedia.org/wiki/Sudoku_solving_algorithms
- http://norvig.com/sudoku.html
- http://www.mathworks.com/company/newsletters/articles/solving-sudoku-with-matlab.html
- http://freepythontips.wordpress.com/2013/09/01/sudoku-solver-in-python/
