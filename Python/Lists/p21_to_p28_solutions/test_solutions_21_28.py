#!/usr/bin/env python3

import unittest
from solutions_21_28 import *

class problemsTwentyOneToTwentyEight (unittest.TestCase):

	def test_s21_insertElement (self):
		self.assertEqual([1, 2, 3, 4, 5, 100, 6, 7, 8, 9],
		s21_insertElement([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 100))

	def test_s22_range (self):
		self.assertEqual([7, 8, 9, 10, 11, 12], s22_range(7, 12))

	def test_s28_sortLists_a (self):
		self.assertEqual([["o"], ["d","e"], ["d","e"], ["m","n"], ["a","b","c"], ["f","g","h"], ["i","j","k","l"]],
		s28_sortLists_a([["a","b","c"], ["d","e"], ["f","g","h"], ["d","e"], ["i","j","k","l"], ["m","n"], ["o"]]))

	def test_s28_sortLists_b (self):
		self.assertEqual([["o"], ["i","j","k","l"], ["a","b","c"], ["f","g","h"], ["d","e"], ["d","e"], ["m","n"]],
		s28_sortLists_b([["a","b","c"], ["d","e"], ["f","g","h"], ["d","e"], ["i","j","k","l"], ["m","n"], ["o"]]))

if __name__ == "__main__":
	unittest.main()
