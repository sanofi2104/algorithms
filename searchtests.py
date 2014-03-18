#!/usr/bin/env python


import unittest
import linearsearch

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.A = [1, 3, 5, 2, 4, 6]
        self.B = []
        self.C = [2, -1]
        self.D = [1, 1, 2, 1, 0]

    def test_ls_index(self):
        index = linearsearch.linearsearch(self.A, 2)
        self.assertEqual(3, index)

    def test_ls_false(self):
        index = linearsearch.linearsearch(self.A, 0)
        self.assertEqual(-1, index)

    def test_ls_empty(self):
        index = linearsearch.linearsearch(self.B, 2)
        self.assertEqual(-1, index)
    

if '__main__' == __name__:
    unittest.main()
