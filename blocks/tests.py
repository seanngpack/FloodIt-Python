import utils
import cell
import consts
import unittest
import sys
sys.path.append("..")

class TestUtils(unittest.TestCase):

    def test_generate_board(self):
        self.assertEqual(len(utils.generate_board()), consts.BOARD_SIZE ** 2)

    def test_rand_color(self):
        self.assertIsInstance(utils.rand_color(), tuple)        

    def test_fix_links(self):
        board = utils.generate_board()
        self.assertEqual(board[0].right, board[1])
        self.assertEqual(board[1].left, board[0])
        self.assertEqual(board[9].right, None)
        self.assertEqual(board[99].right, None)

if __name__ == '__main__':
    unittest.main()
