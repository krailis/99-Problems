#!/usr/bin/env python3

import unittest
from solutions_1_10 import *

class problemsOneToTen(unittest.TestCase):

	def test_s1_lastElement(self):
		self.assertEqual(8, s1_lastElement([2, 5, 7, 1, 8]))

	def test_s2_lastButOne(self):
		self.assertEqual(1, s2_lastButOne([5, 6, 8, 1, 9]))

	def test_s3_kthElement(self):
		self.assertEqual(6, s3_kthElement([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))

	def test_s4_listLength(self):
		self.assertEqual(8, s4_listLength([1, 2, 4, 5, 6, 7, 8, 9]))

	def test_s5_listReverse(self):
		self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1], s5_listReverse([1, 2, 3, 4, 5, 6, 7, 8, 9]))

	def test_s6_isPalindrome(self):
		self.assertTrue(s6_isPalindrome([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]))
		self.assertTrue(s6_isPalindrome([1, 2, 3, 4, 5, 4, 3, 2, 1]))
		self.assertTrue(s6_isPalindrome(["a", "b", "c", "d", "c", "b", "a"]))
		self.assertTrue(not s6_isPalindrome([1, 2, 4, 5, 6, 2, 1]))
		self.assertTrue(not s6_isPalindrome(["a", "b", "c", "d", "e"]))

	def test_s7_flattenList(self):
		self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], s7_flattenList([1, 2, [3, 4], [5, 6, [7, [8]]]]))
		self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], s7_flattenList([1, [2, [3, [4, [5], 6], 7], 8], 9]))

	def test_s8_eliminateConsecutiveDuplicates_1(self):
		self.assertEqual([1, 2, 3, 1, 4, 5], 
		s8_eliminateConsecutiveDuplicates_1([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]))

	def test_s8_eliminateConsecutiveDuplicates_2(self):
		self.assertEqual([1, 2, 3, 1, 4, 5],
		s8_eliminateConsecutiveDuplicates_2([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]))

	def test_s9_packConsecutiveDuplicates(self):
		self.assertEqual([[1, 1, 1, 1], [2], [3, 3], [1, 1], [4], [5, 5, 5, 5]],
		s9_packConsecutiveDuplicates([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]))

	def test_s10_listLengthEncoding(self):
		self.assertEqual([[4, "a"], [1, "b"], [2, "c"], [2, "a"], [1, "d"], [4, "e"]],
		s10_listLengthEncoding(["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"]))

if __name__ == '__main__':
	unittest.main()
