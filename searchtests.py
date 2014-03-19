#!/usr/bin/env python

import unittest
import linearsearch
import binarysearch 

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.A = [1, 3, 5, 2, 4, 6]
        self.B = []
        self.C = [2, -1]
        self.D = [1, 1, 2, 1, 0]
        self.E = [1, 2, 3, 8, 9, 10, 12, 15, 20]
        self.F = [4]

    '''
        Linear Search tests
    '''
    def test_ls_index(self):
        index = linearsearch.linearsearch(self.A, 2)
        self.assertEqual(3, index)

    def test_ls_false(self):
        index = linearsearch.linearsearch(self.A, 0)
        self.assertFalse(index)

    def test_ls_empty(self):
        index = linearsearch.linearsearch(self.B, 2)
        self.assertFalse(index)
    
    '''
        Binary Search tests
    '''
    def test_bs_index(self):
        self.assertEqual(6, binarysearch.binarysearch(self.E, 12))

    def test_bs_false(self):
        self.assertFalse(binarysearch.binarysearch(self.E, -15))

    def test_bs_empty(self):
        self.assertFalse(binarysearch.binarysearch(self.B, 12))

    def test_bs_single(self):
        self.assertEqual(0, binarysearch.binarysearch(self.F, 4))

    
if '__main__' == __name__:
    unittest.main()
