#!/usr/bin/env python3

import unittest

class problemsFortyEightToFortyNine (unittest.TestCase):

	def test_s48_grayCode (self):
		self.assertEqual(["0", "1"], s48_grayCode(1))
		self.assertEqual(["00","01","11","10"], s48_grayCode(2))
		self.assertEqual(["000","001","011","010","110","111","101","100"], s48_grayCode(3))

	def test_s49_huffman (self):
		self.assertEqual([('a', '0'), ('b', '101'), ('c', '100'), ('d', '111'), ('e', '1101'), ('f', '1100')],
				 s49_huffman([(45, 'a'), (13, 'b'), (12, 'c'), (16, 'd'), (9, 'e'), (5, 'f')]))

if __name__ == "__main__":
	unittest.main()
