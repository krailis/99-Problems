"""arithmetic/test_arithmetic.py

This file includes solutions to Arithmetic Problems (31 - 40).

author(s):	Konstantinos Railis <kons.railis@gmail.com>

"""
import unittest

from arithmetic import is_prime, gcd, is_co_prime, totient_phi, prime_factors, prime_factors_mult, \
	totient_phi_2, primes_list, goldbach, goldbach_list


class ArithmeticProblemsTest(unittest.TestCase):
    """Arithmetic Problems Testing Class."""

    def test_is_prime(self):
        """Test is_prime (P31)."""
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(101))
        self.assertFalse(is_prime(49))
        self.assertFalse(is_prime(122))

    def test_gcd(self):
        """Test gcd (P32)."""
        self.assertEqual(gcd(36, 63), 9)
        self.assertEqual(gcd(78, 32), 2)
        self.assertEqual(gcd(35, 49), 7)
        self.assertEqual(gcd(32, 112), 16)
        self.assertEqual(gcd(33, 132), 33)
        self.assertRaises(ValueError, gcd, -1, 2)
        self.assertRaises(ValueError, gcd, 1.2, 4.7)

    def test_is_co_prime(self):
        """Test is_co_prime (P33)."""
        self.assertTrue(is_co_prime(35, 64))
        self.assertTrue(is_co_prime(35, 64))
        self.assertTrue(is_co_prime(35, 64))
        self.assertTrue(is_co_prime(35, 64))
        self.assertFalse(is_co_prime(35, 49))
        self.assertFalse(is_co_prime(35, 56))
        self.assertRaises(ValueError, is_co_prime, -1, 2)
        self.assertRaises(ValueError, is_co_prime, 1.2, 4.7)

    def test_totient_phi(self):
        """Test totient_phi (P34)."""
        self.assertEqual(totient_phi(10), 4)
        self.assertEqual(totient_phi(17), 16)
        self.assertEqual(totient_phi(39), 24)
        self.assertEqual(totient_phi(198), 60)
        self.assertEqual(totient_phi(24420), 5760)
        self.assertRaises(ValueError, totient_phi, 0)
        self.assertRaises(ValueError, totient_phi, 10.4)

    def test_prime_factors(self):
        """Test prime_factors (P35)."""
        self.assertEqual(prime_factors(315), [3, 3, 5, 7])
        self.assertEqual(prime_factors(430), [2, 5, 43])
        self.assertEqual(prime_factors(728), [2, 2, 2, 7, 13])
        self.assertEqual(prime_factors(999), [3, 3, 3, 37])
        self.assertEqual(prime_factors(430), [2, 5, 43])
        self.assertEqual(prime_factors(1725), [3, 5, 5, 23])

    def test_prime_factors_mult(self):
        """Test prime factors (P36)."""
        self.assertEqual(prime_factors_mult(315), [[2, 3], [1, 5], [1, 7]])
        self.assertEqual(prime_factors_mult(430), [[1, 2], [1, 5], [1, 43]])
        self.assertEqual(prime_factors_mult(728), [[3, 2], [1, 7], [1, 13]])
        self.assertEqual(prime_factors_mult(999), [[3, 3], [1, 37]])
        self.assertEqual(prime_factors_mult(430), [[1, 2], [1, 5], [1, 43]])
        self.assertEqual(prime_factors_mult(1725), [[1, 3], [2, 5], [1, 23]])

    def test_totient_phi_2(self):
        """Test totient_phi_2 (P37)."""
        self.assertEqual(totient_phi_2(10), 4)
        self.assertEqual(totient_phi_2(17), 16)
        self.assertEqual(totient_phi_2(39), 24)
        self.assertEqual(totient_phi_2(198), 60)
        self.assertEqual(totient_phi_2(24420), 5760)
        self.assertRaises(ValueError, totient_phi_2, 0)
        self.assertRaises(ValueError, totient_phi_2, 10.4)

    def test_primes_list(self):
        """Test primes_list (P38)."""
        self.assertEqual(primes_list(9, 41), [11, 13, 17, 19, 23, 29, 31, 37, 41])
        self.assertEqual(primes_list(3923, 4002), [3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001])
        self.assertEqual(primes_list(5003, 5024), [5003, 5009, 5011, 5021, 5023])
        self.assertEqual(primes_list(283, 312), [283, 293, 307, 311])
        self.assertEqual(primes_list(2131, 2142), [2131, 2137, 2141])

    def test_goldbach(self):
        """Test goldbach (P40)."""
        self.assertEqual(goldbach(28), [5, 23])
        self.assertEqual(goldbach(30), [7, 23])
        self.assertEqual(goldbach(1002), [5, 997])
        self.assertEqual(goldbach(1004), [7, 997])
        self.assertEqual(goldbach(10000), [59, 9941])
        self.assertEqual(goldbach(5000), [7, 4993])
        self.assertRaises(ValueError, goldbach, 0)
        self.assertRaises(ValueError, goldbach, 23)

    def test_goldbach_list(self):
        """Test goldbach_list (P41)."""
        self.assertEqual(goldbach_list(9, 20), [[3, 7], [5, 7], [3, 11], [3, 13], [5, 13], [3, 17]])
        self.assertEqual(goldbach_list(28, 36), [[5, 23], [7, 23], [3, 29], [3, 31], [5, 31]])
        self.assertEqual(goldbach_list(240, 246), [[7, 233], [3, 239], [3, 241], [5, 241]])


if __name__ == '__main__':
    unittest.main()
