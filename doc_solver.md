### Sudoku Solver Documentation
This page details my approach to solving the problem

#### Literature Review
A quick search on the internet yields the following popular algorithms to solving the problem:
- Backtracking
An iterative approach that tries 

- Brute-force
Here we try all possible 

- Exact-cover

- Stochastic search

- Constraint programming


#### Model Approach
After considering the pro/con of each algorithm and my own background, I decided to use the
constraint programming approach due to
- ability to exploit existing (IP) solvers
- elegant formulation using linear algebra
- runtime gaurantees as an integer program


