from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ARRAY, select
from sqlalchemy.sql import and_
from NQueensSolver import NQueensSolver

if __name__ == "__main__":
  # engine = create_engine("postgresql://nQueensPuzzle:nQueensPuzzle@nqueenspuzzledb:5432/nQueensPuzzle",echo=False)
  engine = create_engine("postgresql://nQueensPuzzle:nQueensPuzzle@localhost:5432/nQueensPuzzle",echo=False)
  metadata = MetaData()

  Solutions = Table(
    'solutions', metadata, 
    Column('id', Integer, primary_key=True), 
    Column('n', Integer), 
    Column('board', ARRAY(Integer))
  )

  metadata.create_all(engine)

  size = 4
  solver = NQueensSolver(size)
  solver.run()
    
  for solution in solver.get_solutions():
    print(solution)
    print(NQueensSolver.print_board(solution))

    stmt = select([Solutions]).where(and_(
      Solutions.c.n == size,
      Solutions.c.board == solution
    ))

    selected_solutions = engine.execute(stmt).fetchone()

    if selected_solutions is None:
      insert_solutions = Solutions.insert().values(n=size, board=solution)
      engine.execute(insert_solutions)

  print(solver.num_solutions)