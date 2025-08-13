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

def test_c3_middle():
    assert board_index_to_tile_pair((3,1), 19, 19) == [(0,0),(1,0)]
    assert board_index_to_tile_pair((3,2), 19, 19) == [(0,0),(1,0)]
    assert board_index_to_tile_pair((3,4), 19, 19) == [(0,1),(1,1)]
    assert board_index_to_tile_pair((3,5), 19, 19) == [(0,1),(1,1)]
    assert board_index_to_tile_pair((3,7), 19, 19) == [(0,2),(1,2)]
    assert board_index_to_tile_pair((3,8), 19, 19) == [(0,2),(1,2)]
    assert board_index_to_tile_pair((3,10), 19, 19) == [(0,3),(1,3)]
    assert board_index_to_tile_pair((3,11), 19, 19) == [(0,3),(1,3)]
    assert board_index_to_tile_pair((3,13), 19, 19) == [(0,4),(1,4)]
    assert board_index_to_tile_pair((3,14), 19, 19) == [(0,4),(1,4)]
    assert board_index_to_tile_pair((3,16), 19, 19) == [(0,5),(1,5)]
    assert board_index_to_tile_pair((3,17), 19, 19) == [(0,5),(1,5)]

def test_c6_middle():
    assert board_index_to_tile_pair((6,1), 19, 19) == [(1,0),(2,0)]
    assert board_index_to_tile_pair((6,2), 19, 19) == [(1,0),(2,0)]
    assert board_index_to_tile_pair((6,4), 19, 19) == [(1,1),(2,1)]
    assert board_index_to_tile_pair((6,5), 19, 19) == [(1,1),(2,1)]
    assert board_index_to_tile_pair((6,7), 19, 19) == [(1,2),(2,2)]
    assert board_index_to_tile_pair((6,8), 19, 19) == [(1,2),(2,2)]
    assert board_index_to_tile_pair((6,10), 19, 19) == [(1,3),(2,3)]
    assert board_index_to_tile_pair((6,11), 19, 19) == [(1,3),(2,3)]
    assert board_index_to_tile_pair((6,13), 19, 19) == [(1,4),(2,4)]
    assert board_index_to_tile_pair((6,14), 19, 19) == [(1,4),(2,4)]
    assert board_index_to_tile_pair((6,16), 19, 19) == [(1,5),(2,5)]
    assert board_index_to_tile_pair((6,17), 19, 19) == [(1,5),(2,5)]

def test_c9_middle():
    assert board_index_to_tile_pair((9,1), 19, 19) == [(2,0),(3,0)]
    assert board_index_to_tile_pair((9,2), 19, 19) == [(2,0),(3,0)]
    assert board_index_to_tile_pair((9,4), 19, 19) == [(2,1),(3,1)]
    assert board_index_to_tile_pair((9,5), 19, 19) == [(2,1),(3,1)]
    assert board_index_to_tile_pair((9,7), 19, 19) == [(2,2),(3,2)]
    assert board_index_to_tile_pair((9,8), 19, 19) == [(2,2),(3,2)]
    assert board_index_to_tile_pair((9,10), 19, 19) == [(2,3),(3,3)]
    assert board_index_to_tile_pair((9,11), 19, 19) == [(2,3),(3,3)]
    assert board_index_to_tile_pair((9,13), 19, 19) == [(2,4),(3,4)]
    assert board_index_to_tile_pair((9,14), 19, 19) == [(2,4),(3,4)]
    assert board_index_to_tile_pair((9,16), 19, 19) == [(2,5),(3,5)]
    assert board_index_to_tile_pair((9,17), 19, 19) == [(2,5),(3,5)]

def test_c12_middle():
    assert board_index_to_tile_pair((12,1), 19, 19) == [(3,0),(4,0)]
    assert board_index_to_tile_pair((12,2), 19, 19) == [(3,0),(4,0)]
    assert board_index_to_tile_pair((12,4), 19, 19) == [(3,1),(4,1)]
    assert board_index_to_tile_pair((12,5), 19, 19) == [(3,1),(4,1)]
    assert board_index_to_tile_pair((12,7), 19, 19) == [(3,2),(4,2)]
    assert board_index_to_tile_pair((12,8), 19, 19) == [(3,2),(4,2)]
    assert board_index_to_tile_pair((12,10), 19, 19) == [(3,3),(4,3)]
    assert board_index_to_tile_pair((12,11), 19, 19) == [(3,3),(4,3)]
    assert board_index_to_tile_pair((12,13), 19, 19) == [(3,4),(4,4)]
    assert board_index_to_tile_pair((12,14), 19, 19) == [(3,4),(4,4)]
    assert board_index_to_tile_pair((12,16), 19, 19) == [(3,5),(4,5)]
    assert board_index_to_tile_pair((12,17), 19, 19) == [(3,5),(4,5)]

def test_c15_middle():
    assert board_index_to_tile_pair((15,1), 19, 19) == [(4,0),(5,0)]
    assert board_index_to_tile_pair((15,2), 19, 19) == [(4,0),(5,0)]
    assert board_index_to_tile_pair((15,4), 19, 19) == [(4,1),(5,1)]
    assert board_index_to_tile_pair((15,5), 19, 19) == [(4,1),(5,1)]
    assert board_index_to_tile_pair((15,7), 19, 19) == [(4,2),(5,2)]
    assert board_index_to_tile_pair((15,8), 19, 19) == [(4,2),(5,2)]
    assert board_index_to_tile_pair((15,10), 19, 19) == [(4,3),(5,3)]
    assert board_index_to_tile_pair((15,11), 19, 19) == [(4,3),(5,3)]
    assert board_index_to_tile_pair((15,13), 19, 19) == [(4,4),(5,4)]
    assert board_index_to_tile_pair((15,14), 19, 19) == [(4,4),(5,4)]
    assert board_index_to_tile_pair((15,16), 19, 19) == [(4,5),(5,5)]
    assert board_index_to_tile_pair((15,17), 19, 19) == [(4,5),(5,5)]

def test_r3_middle():
    assert board_index_to_tile_pair((1,3), 19, 19) == [(0,0),(0,1)]
    assert board_index_to_tile_pair((2,3), 19, 19) == [(0,0),(0,1)]
    assert board_index_to_tile_pair((4,3), 19, 19) == [(1,0),(1,1)]
    assert board_index_to_tile_pair((5,3), 19, 19) == [(1,0),(1,1)]
    assert board_index_to_tile_pair((7,3), 19, 19) == [(2,0),(2,1)]
    assert board_index_to_tile_pair((8,3), 19, 19) == [(2,0),(2,1)]
    assert board_index_to_tile_pair((10,3), 19, 19) == [(3,0),(3,1)]
    assert board_index_to_tile_pair((11,3), 19, 19) == [(3,0),(3,1)]
    assert board_index_to_tile_pair((13,3), 19, 19) == [(4,0),(4,1)]
    assert board_index_to_tile_pair((14,3), 19, 19) == [(4,0),(4,1)]
    assert board_index_to_tile_pair((16,3), 19, 19) == [(5,0),(5,1)]
    assert board_index_to_tile_pair((17,3), 19, 19) == [(5,0),(5,1)]

def test_r6_middle():
    assert board_index_to_tile_pair((1,6), 19, 19) == [(0,1),(0,2)]
    assert board_index_to_tile_pair((2,6), 19, 19) == [(0,1),(0,2)]
    assert board_index_to_tile_pair((4,6), 19, 19) == [(1,1),(1,2)]
    assert board_index_to_tile_pair((5,6), 19, 19) == [(1,1),(1,2)]
    assert board_index_to_tile_pair((7,6), 19, 19) == [(2,1),(2,2)]
    assert board_index_to_tile_pair((8,6), 19, 19) == [(2,1),(2,2)]
    assert board_index_to_tile_pair((10,6), 19, 19) == [(3,1),(3,2)]
    assert board_index_to_tile_pair((11,6), 19, 19) == [(3,1),(3,2)]
    assert board_index_to_tile_pair((13,6), 19, 19) == [(4,1),(4,2)]
    assert board_index_to_tile_pair((14,6), 19, 19) == [(4,1),(4,2)]
    assert board_index_to_tile_pair((16,6), 19, 19) == [(5,1),(5,2)]
    assert board_index_to_tile_pair((17,6), 19, 19) == [(5,1),(5,2)]

def test_r9_middle():
    assert board_index_to_tile_pair((1,9), 19, 19) == [(0,2),(0,3)]
    assert board_index_to_tile_pair((2,9), 19, 19) == [(0,2),(0,3)]
    assert board_index_to_tile_pair((4,9), 19, 19) == [(1,2),(1,3)]
    assert board_index_to_tile_pair((5,9), 19, 19) == [(1,2),(1,3)]
    assert board_index_to_tile_pair((7,9), 19, 19) == [(2,2),(2,3)]
    assert board_index_to_tile_pair((8,9), 19, 19) == [(2,2),(2,3)]
    assert board_index_to_tile_pair((10,9), 19, 19) == [(3,2),(3,3)]
    assert board_index_to_tile_pair((11,9), 19, 19) == [(3,2),(3,3)]
    assert board_index_to_tile_pair((13,9), 19, 19) == [(4,2),(4,3)]
    assert board_index_to_tile_pair((14,9), 19, 19) == [(4,2),(4,3)]
    assert board_index_to_tile_pair((16,9), 19, 19) == [(5,2),(5,3)]
    assert board_index_to_tile_pair((17,9), 19, 19) == [(5,2),(5,3)]

def test_r12_middle():
    assert board_index_to_tile_pair((1,12), 19, 19) == [(0,3),(0,4)]
    assert board_index_to_tile_pair((2,12), 19, 19) == [(0,3),(0,4)]
    assert board_index_to_tile_pair((4,12), 19, 19) == [(1,3),(1,4)]
    assert board_index_to_tile_pair((5,12), 19, 19) == [(1,3),(1,4)]
    assert board_index_to_tile_pair((7,12), 19, 19) == [(2,3),(2,4)]
    assert board_index_to_tile_pair((8,12), 19, 19) == [(2,3),(2,4)]
    assert board_index_to_tile_pair((10,12), 19, 19) == [(3,3),(3,4)]
    assert board_index_to_tile_pair((11,12), 19, 19) == [(3,3),(3,4)]
    assert board_index_to_tile_pair((13,12), 19, 19) == [(4,3),(4,4)]
    assert board_index_to_tile_pair((14,12), 19, 19) == [(4,3),(4,4)]
    assert board_index_to_tile_pair((16,12), 19, 19) == [(5,3),(5,4)]
    assert board_index_to_tile_pair((17,12), 19, 19) == [(5,3),(5,4)]

def test_r15_middle():
    assert board_index_to_tile_pair((1,15), 19, 19) == [(0,4),(0,5)]
    assert board_index_to_tile_pair((2,15), 19, 19) == [(0,4),(0,5)]
    assert board_index_to_tile_pair((4,15), 19, 19) == [(1,4),(1,5)]
    assert board_index_to_tile_pair((5,15), 19, 19) == [(1,4),(1,5)]
    assert board_index_to_tile_pair((7,15), 19, 19) == [(2,4),(2,5)]
    assert board_index_to_tile_pair((8,15), 19, 19) == [(2,4),(2,5)]
    assert board_index_to_tile_pair((10,15), 19, 19) == [(3,4),(3,5)]
    assert board_index_to_tile_pair((11,15), 19, 19) == [(3,4),(3,5)]
    assert board_index_to_tile_pair((13,15), 19, 19) == [(4,4),(4,5)]
    assert board_index_to_tile_pair((14,15), 19, 19) == [(4,4),(4,5)]
    assert board_index_to_tile_pair((16,15), 19, 19) == [(5,4),(5,5)]
    assert board_index_to_tile_pair((17,15), 19, 19) == [(5,4),(5,5)]

#if __name__ == '__main__':
    #unittest.main()