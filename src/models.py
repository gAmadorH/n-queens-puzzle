from database import Base, db_session
from sqlalchemy import Column, Integer, ARRAY

class Solution(Base):
  __tablename__ = 'solutions'
  id = Column(Integer, primary_key=True)
  size = Column(Integer)
  board = Column(ARRAY(Integer))

  @staticmethod
  def findOne(size, board):
    return db_session.query(Solution).filter_by(size=size).filter_by(board=board).first()

  @staticmethod
  def createOne(size, board):
    db_session.add(Solution(size=size, board=board))
    db_session.commit()
