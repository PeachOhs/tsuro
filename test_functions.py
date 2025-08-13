"""
Run by running
python -m pytest
in the root dir of the project
""" 

#import unittest
import pytest
from helper import *

#class TestBoard_index_to_tile_pair(unittest.TestCase):
def test_top_edges():
    assert board_index_to_tile_pair((1,0), 19, 19) == [(0,0)]
    assert board_index_to_tile_pair((2,0), 19, 19) == [(0,0)]
    assert board_index_to_tile_pair((4,0), 19, 19) == [(1,0)]
    assert board_index_to_tile_pair((5,0), 19, 19) == [(1,0)]
    assert board_index_to_tile_pair((7,0), 19, 19) == [(2,0)]
    assert board_index_to_tile_pair((8,0), 19, 19) == [(2,0)]
    assert board_index_to_tile_pair((10,0), 19, 19) == [(3,0)]
    assert board_index_to_tile_pair((11,0), 19, 19) == [(3,0)]
    assert board_index_to_tile_pair((13,0), 19, 19) == [(4,0)]
    assert board_index_to_tile_pair((14,0), 19, 19) == [(4,0)]
    assert board_index_to_tile_pair((16,0), 19, 19) == [(5,0)]
    assert board_index_to_tile_pair((17,0), 19, 19) == [(5,0)]

def test_left_edges():
    assert board_index_to_tile_pair((0,1), 19, 19) == [(0,0)]
    assert board_index_to_tile_pair((0,2), 19, 19) == [(0,0)]
    assert board_index_to_tile_pair((0,4), 19, 19) == [(0,1)]
    assert board_index_to_tile_pair((0,5), 19, 19) == [(0,1)]
    assert board_index_to_tile_pair((0,7), 19, 19) == [(0,2)]
    assert board_index_to_tile_pair((0,8), 19, 19) == [(0,2)]
    assert board_index_to_tile_pair((0,10), 19, 19) == [(0,3)]
    assert board_index_to_tile_pair((0,11), 19, 19) == [(0,3)]
    assert board_index_to_tile_pair((0,13), 19, 19) == [(0,4)]
    assert board_index_to_tile_pair((0,14), 19, 19) == [(0,4)]
    assert board_index_to_tile_pair((0,16), 19, 19) == [(0,5)]
    assert board_index_to_tile_pair((0,17), 19, 19) == [(0,5)]

def test_bottom_edges():
    assert board_index_to_tile_pair((1,18), 19, 19) == [(0,5)]
    assert board_index_to_tile_pair((2,18), 19, 19) == [(0,5)]
    assert board_index_to_tile_pair((4,18), 19, 19) == [(1,5)]
    assert board_index_to_tile_pair((5,18), 19, 19) == [(1,5)]
    assert board_index_to_tile_pair((7,18), 19, 19) == [(2,5)]
    assert board_index_to_tile_pair((8,18), 19, 19) == [(2,5)]
    assert board_index_to_tile_pair((10,18), 19, 19) == [(3,5)]
    assert board_index_to_tile_pair((11,18), 19, 19) == [(3,5)]
    assert board_index_to_tile_pair((13,18), 19, 19) == [(4,5)]
    assert board_index_to_tile_pair((14,18), 19, 19) == [(4,5)]
    assert board_index_to_tile_pair((16,18), 19, 19) == [(5,5)]
    assert board_index_to_tile_pair((17,18), 19, 19) == [(5,5)]

def test_right_edges():
    assert board_index_to_tile_pair((18,1), 19, 19) == [(5,0)]
    assert board_index_to_tile_pair((18,2), 19, 19) == [(5,0)]
    assert board_index_to_tile_pair((18,4), 19, 19) == [(5,1)]
    assert board_index_to_tile_pair((18,5), 19, 19) == [(5,1)]
    assert board_index_to_tile_pair((18,7), 19, 19) == [(5,2)]
    assert board_index_to_tile_pair((18,8), 19, 19) == [(5,2)]
    assert board_index_to_tile_pair((18,10), 19, 19) == [(5,3)]
    assert board_index_to_tile_pair((18,11), 19, 19) == [(5,3)]
    assert board_index_to_tile_pair((18,13), 19, 19) == [(5,4)]
    assert board_index_to_tile_pair((18,14), 19, 19) == [(5,4)]
    assert board_index_to_tile_pair((18,16), 19, 19) == [(5,5)]
    assert board_index_to_tile_pair((18,17), 19, 19) == [(5,5)]

def test_middle():
    assert board_index_to_tile_pair((6,7), 19, 19) == [(1,2),(2,2)]

def test_other_middle():
    assert board_index_to_tile_pair((7,6), 19, 19) == [(2,1),(2,2)]

#if __name__ == '__main__':
    #unittest.main()