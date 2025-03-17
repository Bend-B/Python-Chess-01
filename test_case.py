import unittest
import main

class TestFactorial(unittest.TestCase):
    """
    Test class
    """

    def test_moves_empty_game(self):

        game = None
        player = -1

        #moves = chess.possible_moves(game, player)

        #self.assertEqual(moves, [])


    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = 12
        self.assertEqual(res, 12)

if __name__ == '__main__':
    unittest.main()