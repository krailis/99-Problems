#!/usr/bin/env python3

import unittest
from solutions_31_41 import *

class problemsThirtyOneToFortyOne (unittest.TestCase):

	def test_s31_isPrime (self):
		self.assertTrue(s31_isPrime(7))
		self.assertTrue(s31_isPrime(31))
		self.assertTrue(s31_isPrime(101))
		self.assertTrue(not s31_isPrime(49))
		self.assertTrue(not s31_isPrime(122))

	def test_s32_primeFactors (self):
		self.assertEqual([3, 3, 5, 7], s32_primeFactors(315))

	def test_s33_primeFactorsMult (self):
		self.assertEqual([[3, 2], [5, 1], [7, 1]], s33_primeFactorsMult(315))

	def test_s34_primesList (self):
		self.assertEqual([11, 13, 17, 19, 23, 29, 31, 37, 41], s34_primesList(9, 41))

	def test_s35_goldbach (self):
		self.assertEqual([5, 23], s35_goldbach(28))

	def test_s36_goldbachList (self):
		self.assertEqual([[3, 7], [5, 7], [3, 11], [3, 13], [5, 13], [3, 17]], s36_goldbachList(9, 20))

	def test_s37_gcd (self):
		self.assertEqual(9, s37_gcd(36, 63))

	def test_s38_coprime (self):
		self.assertTrue(s38_coprime(35, 64))
		self.assertTrue(not s38_coprime(35, 49))

	def test_s39_totientPhi (self):
		self.assertEqual(4, s39_totientPhi(10))

	def test_s40_totientPhi_2 (self):
		self.assertEqual(4, s40_totientPhi_2(10))

if __name__ == '__main__':
	unittest.main()
