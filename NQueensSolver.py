class NQueensSolver:
  def __init__(self, N):
    self.N = N
    self.num_solutions = 0
    self.all_solutions = []
    self.solution = []
    self.all_ones = (1 << self.N) - 1

  def run(self):
    self.solve(0, 0, 0, 0)
    return self.all_solutions

  def solve(self, column, left_diagonal, right_diagonal, queens_placed):
    if queens_placed == self.N:
      self.num_solutions += 1
      self.all_solutions.append([i for i in self.solution])

    valid_spots = self.all_ones & ~(column | left_diagonal | right_diagonal)

    while valid_spots != 0:
      current_spot = -valid_spots & valid_spots
      valid_spots ^= current_spot
      self.solution.append((current_spot & -current_spot).bit_length() - 1)
      self.solve(
        (column | current_spot),
        (left_diagonal | current_spot) >> 1,
        (right_diagonal | current_spot) << 1,
        queens_placed + 1
      )
      self.solution.pop()