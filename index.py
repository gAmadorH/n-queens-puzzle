from NQueensSolver import NQueensSolver

if __name__ == "__main__":
  solver = NQueensSolver(8) 

  for solve in solver.run():
    print(solve)
  
  print(solver.num_solutions)