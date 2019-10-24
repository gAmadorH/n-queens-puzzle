from database import db_session
from NQueensSolver import NQueensSolver
from models import Solution
import time
import inquirer

def resolve(size):
  solver = NQueensSolver(size)

  # calculate resolution time
  start_time = time.time()
  solver.run()
  end_time = time.time()

  # resolution time
  duration_seconds = end_time - start_time  
  duration_milliseconds = duration_seconds * 1000
  duration_minutes = duration_milliseconds / 60000

  for solution in solver.get_all_solutions():
    print(solution)
    print(solver.get_board(solution))
    print()

    if Solution.findOne(size, solution) is None:
      Solution.createOne(size, solution)

  db_session.remove()

  print("Board size : {}".format(size))
  print("Number of solutions: {}".format(solver.get_num_solutions()))
  print("Resolution time (milliseconds): {}".format(duration_milliseconds))
  print("Resolution time (seconds): {}".format(duration_seconds))
  print("Resolution time (minutes): {}".format(duration_minutes))

if __name__ == "__main__":
  
  while True:
    questions = [
      inquirer.Text('size', message="Indicate the size of the chess board, only Enter key to exit")
    ]

    answers = inquirer.prompt(questions)
    size = answers["size"]
    
    if len(size) <= 0:
      break

    sizeInt = 0
    try:
        sizeInt = int(size)
    except:
      print("inavalid value")
      continue

    print(sizeInt)
    # resolve(size)

  print("Exit!!! bye bye!!!")