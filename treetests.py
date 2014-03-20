#!/usr/bin/env python

import unittest
import binarytree

class treetests(unittest.TestCase):

    def setUp(self):
        self.tree = binarytree.binary_node('F')
        self.tree.left = binarytree.binary_node('B')
        self.tree.right = binarytree.binary_node('G')
        self.tree.left.left = binarytree.binary_node('A')
        self.tree.left.right = binarytree.binary_node('D')
        self.tree.left.right.left = binarytree.binary_node('C')
        self.tree.left.right.right = binarytree.binary_node('E')
        self.tree.right.right = binarytree.binary_node('I')
        self.tree.right.right.left = binarytree.binary_node('H')
    
        self.bf_result = 'FBGADICEH'
        self.df_preorder_result = 'FBADCEGIH'
        self.df_inorder_result = 'ABCDEFGHI'
        self.df_postorder_result = 'ACEDBHIGF'

    '''
    Breadth-first Search
    '''
    def test_bf_path(self):
        self.assertEqual(self.bf_result, ''.join(binarytree.breadth_first(self.tree))) 
    
    def test_bf_emptytree(self):
        self.assertFalse(binarytree.breadth_first(None))

    '''
    Depth-first Search
    '''
    # Pre-Order algorithm
    def test_df_preorder_path(self):
        self.assertEqual(self.df_preorder_result, ''.join(binarytree.pre_order(self.tree)))
    
    def test_df_preorder_empty(self):
        self.assertFalse(binarytree.pre_order(None))

    # In-Order algorithm
    def test_df_inorder_path(self):
        self.assertEqual(self.df_inorder_result, ''.join(binarytree.in_order(self.tree)))
    
    def test_df_inorder_empty(self):
        self.assertFalse(binarytree.in_order(None))
    
    # In-Order algorithm
    def test_df_postorder_path(self):
        self.assertEqual(self.df_postorder_result, ''.join(binarytree.post_order(self.tree)))
    
    def test_df_postorder_empty(self):
        self.assertFalse(binarytree.post_order(None))


if '__main__' == __name__:
    unittest.main()

