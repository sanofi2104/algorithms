#!/usr/bin/env python

import unittest
import bubblesort

class SortTests(unittest.TestCase):

    def setUp(self):
        self.A = [1, 8, 5, 2, 6, 3]
        self.B = [3]
        self.C = []
        self.D = [1, 3, 2, 5, 2]

    '''
        Bubble Sort 
    '''
    def test_bsort_sort(self):
        self.assertEqual(sorted(self.A), bubblesort.bubblesort(self.A))
    
    def test_bsort_empty(self):
        self.assertFalse(bubblesort.bubblesort(self.C))

    def test_bsort_single(self):
        self.assertEqual(self.B, bubblesort.bubblesort(self.B))
    
    def test_bsort_max(self):
        self.assertEqual(range(10), bubblesort.bubblesort(range(10)[::-1]))
    
    def test_bsort_repeat(self):
        self.assertEqual(sorted(self.D), bubblesort.bubblesort(self.D))


if '__main__' == __name__:
    unittest.main()
