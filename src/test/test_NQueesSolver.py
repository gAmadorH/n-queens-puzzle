from ..NQueensSolver import NQueensSolver
import pytest

def get_nXn_board_data_test():
  return [
    (0, 0),
    (1, 1),
    (2, 0),
    (3, 0),
    (4, 2),
    (5, 10),
    (6, 4),
    (7, 40),
    (8, 92),
    (9, 352),
    (10, 724),
    (11, 2_680),
    (12, 14_200),
    (13, 73_712),
    # (14, 365_596),
    # (15, 2_279_184),
    # (16, 14_772_512),
    # (17, 95_815_104),
    # (18, 666_090_624),
    # (19, 4,968_057_848),
    # (20, 39_029_188_884),
    # (21, 314_666_222_712),
    # (22, 336_376_244_042),
    # (23, 3_029_242_658_210),
    # (24, 227_514_171_973_736),
    # (25, 2_207_893_435_808_352),
    # (26, 22_317_699_616_364_044),
    # (27, 234_907_967_154_122_528),
  ]

@pytest.mark.parametrize('n, num_solutions', get_nXn_board_data_test())
def test_nXn_board(n, num_solutions):
  solver = NQueensSolver(n)
  solver.run()

  assert solver.get_num_solutions() == num_solutions
