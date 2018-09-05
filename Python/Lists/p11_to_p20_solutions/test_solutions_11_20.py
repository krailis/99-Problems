#!/usr/bin/env python3

import unittest
from solutions_11_20 import *

class problemsElevenToTwenty (unittest.TestCase):

	def test_s11_modifiedLengthEncoding (self):
		self.assertEqual([[4, "a"], "b", [2, "c"], [2, "a"], "d", [4, "e"]],
		s11_modifiedLengthEncoding(["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"]))

	def test_s12_decodeList (self):
		self.assertEqual(["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"],
		s12_decodeList([[4, "a"], "b", [2, "c"], [2, "a"], "d", [4, "e"]]))

	def test_s13_directLengthEncoding (self):
		self.assertEqual([[4, "a"], "b", [2, "c"], [2, "a"], "d", [4, "e"]],
		s13_directLengthEncoding(["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"]))

	def test_s14_duplicateListElements (self):
		self.assertEqual([1, 1, 2, 2, 3, 3, 3, 3, 4, 4], s14_duplicateListElements([1, 2, 3, 3, 4]))

	def test_s15_duplicateGivenTimes (self):
		self.assertEqual([1, 1, 1, 2, 2, 2, 3, 3, 3], s15_duplicateGivenTimes([1, 2, 3], 3))

	def test_s16_dropEveryNthElement (self):
		self.assertEqual([1, 2, 4, 5, 7, 8], s16_dropEveryNthElement([1, 2, 3, 4, 5, 6, 7, 8], 3))

	def test_s17_splitList (self):
		self.assertEqual([[1, 2, 3, 4], [5, 6, 7, 8, 9]], s17_splitList([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))

	def test_s18_extractSlice (self):
		self.assertEqual([3, 4, 5, 6], s18_extractSlice([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))

	def test_s19_rotateList (self):
		self.assertEqual([4, 5, 6, 7, 8, 9, 1, 2, 3], s19_rotateList([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
		self.assertEqual([8, 9, 1, 2, 3, 4, 5, 6, 7], s19_rotateList([1, 2, 3, 4, 5, 6, 7, 8, 9], -2))

	def test_s20_removeKthElement (self):
		self.assertEqual([1, 2, 3, 4, 5, 7, 8, 9], s20_removeKthElement([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))

if __name__ == "__main__":
	unittest.main()
