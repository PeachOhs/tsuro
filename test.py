import unittest
from helper import *

class TestBoard_index_to_tile_pair(unittest.TestCase):
    def test_middle(self):
        self.assertEqual(board_index_to_tile_pair((7,6), 19, 19), [(2,1),(2,2)])
        self.assertEqual(board_index_to_tile_pair((6,7), 19, 19), [(1,2),(2,2)])

    def test_edges(self):  
        self.assertEqual(board_index_to_tile_pair((17,18), 19, 19), [(5,5)])
        self.assertEqual(board_index_to_tile_pair((18,17), 19, 19), [(5,5)])

if __name__ == '__main__':
    unittest.main()