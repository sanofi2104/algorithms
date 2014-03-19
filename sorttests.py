#!/usr/bin/env python

import unittest
import bubblesort
import insertionsort
import mergesort
import quicksort

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


    '''
        Insertion Sort 
    '''
    def test_isort_sort(self):
        self.assertEqual(sorted(self.A), insertionsort.insertionsort(self.A))

    def test_isort_empty(self):
        self.assertFalse(insertionsort.insertionsort(self.C))

    def test_isort_single(self):
        self.assertEqual(self.B, insertionsort.insertionsort(self.B))

    def test_isort_repeat(self):
        self.assertEqual(sorted(self.D), insertionsort.insertionsort(self.D))

    
    '''
        Merge Sort 
    '''
    # check merging algorithm (mergetwo function)
    def test_msort_merge(self):
        self.assertEqual([1,2,3,4,5], mergesort.mergetwo([2,3], [1,4,5]))

    #check sorting algorithm
    def test_msort_sort(self):
        self.assertEqual(sorted(self.A), mergesort.mergesort(self.A))

    def test_msort_empty(self):
        self.assertFalse(mergesort.mergesort(self.C))

    def test_msort_single(self):
        self.assertEqual(self.B, mergesort.mergesort(self.B))

    def test_msort_repeat(self):
        self.assertEqual(sorted(self.D), mergesort.mergesort(self.D))


    '''
        Quick Sort 
    '''
    # check merging algorithm (mergetwo function)
    def test_qsort_merge(self):
        self.assertEqual([2,1,3,3,4,5], quicksort.merge([2,1], 3, [3,4,5]))

    #check sorting algorithm
    def test_qsort_sort(self):
        self.assertEqual(sorted(self.A), quicksort.quicksort(self.A))

    def test_qsort_empty(self):
        self.assertFalse(quicksort.quicksort(self.C))

    def test_qsort_single(self):
        self.assertEqual(self.B, quicksort.quicksort(self.B))

    def test_qsort_repeat(self):
        self.assertEqual(sorted(self.D), quicksort.quicksort(self.D))

if '__main__' == __name__:
    unittest.main()
