class NQueensSolver:
  def __init__(self, size):
    self.__size = size
    self.__num_solutions = 0
    self.__all_solutions = []
    self.__temp_solution = []
    self.__all_ones = (1 << self.__size) - 1

  def get_all_solutions(self):
    return self.__all_solutions

  def get_num_solutions(self):
    return self.__num_solutions

  def run(self):
    self.solve(0, 0, 0, 0)

  def solve(self, column, left_diagonal, right_diagonal, queens_placed):
    if queens_placed == self.__size:
      self.__num_solutions += 1
      self.__all_solutions.append([i for i in self.__temp_solution])

    valid_spots = self.__all_ones & ~(column | left_diagonal | right_diagonal)

    while valid_spots != 0:
      current_spot = -valid_spots & valid_spots
      valid_spots ^= current_spot
      self.__temp_solution.append((current_spot & -current_spot).bit_length() - 1)
      self.solve(
        (column | current_spot),
        (left_diagonal | current_spot) >> 1,
        (right_diagonal | current_spot) << 1,
        queens_placed + 1
      )
      self.__temp_solution.pop()
  
  @staticmethod
  def get_board(solution):
    size = len(solution) 
    board = ''

    for colum in range(size):
      for row in range(size):
        if solution[row] == colum:
          board += 'Q '
        else: 
          board += '. '
      board += '\n'

    return board
