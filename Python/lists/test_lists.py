"""lists/test_lists.py

This module includes tests for the solutions to List Problems (1-28).

author(s):  Konstantinos Railis

"""
import unittest

from lists import last_element, last_but_one, kth_element, length, reverse, is_palindrome, \
    flatten, compress, pack, encode, encode_modified, decode, encode_direct, duplicate, \
    duplicate_times, drop, split, slice_list, rotate, remove_kth_element, insert_at, \
    range_list, length_sort, length_frequency_sort


class ListProblemsTest(unittest.TestCase):
    """List Problems Testing Class."""

    def test_last_element(self):
        """Test last_element (P01)."""
        self.assertEqual(last_element([2, 5, 7, 1, 8]), 8)
        self.assertEqual(last_element(['a', 'b', 'c', 'd', 'e']), 'e')
        self.assertEqual(last_element([1]), 1)
        self.assertRaises(ValueError, last_element, [])
        self.assertRaises(TypeError, last_element, {})

    def test_last_but_one(self):
        """Test last_but_one (P02)."""
        self.assertEqual(last_but_one([1, 2, 3, 4, 5]), 4)
        self.assertEqual(last_but_one(['a', 'b', 'c', 'd', 'e']), 'd')
        self.assertEqual(last_but_one([1, 2]), 1)
        self.assertEqual(last_but_one(['a', 'b']), 'a')
        self.assertRaises(ValueError, last_but_one, [1])
        self.assertRaises(ValueError, last_but_one, [])
        self.assertRaises(TypeError, last_but_one, {})

    def test_kth_element(self):
        """Test kth_element (P03)."""
        self.assertEqual(kth_element([1, 2, 3, 4, 5, 6, 7, 8, 9], 6), 6)
        self.assertEqual(kth_element(['a', 'b', 'c', 'd', 'e'], 2), 'b')
        self.assertRaises(ValueError, kth_element, [1, 2, 3, 4, 5], 6)
        self.assertRaises(TypeError, kth_element, {}, 8)

    def test_length(self):
        """Test length (P04)."""
        self.assertEqual(length([1, 2, 4, 5, 6, 7, 8, 9]), 8)
        self.assertEqual(length(['a', 'b', 'c', 'd', 'e', 'f', 'g']), 7)
        self.assertRaises(TypeError, length, {})

    def test_reverse(self):
        """Test reverse (P05)."""
        self.assertEqual(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9]), [9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(reverse(['a', 'b', 'c', 'd', 'e', 'f']), ['f', 'e', 'd', 'c', 'b', 'a'])
        self.assertEqual(reverse([1]), [1])
        self.assertEqual(reverse([]), [])
        self.assertRaises(TypeError, reverse, {})

    def test_is_palindrome(self):
        """Test is_palindrome (P06)."""
        self.assertTrue(is_palindrome([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]))
        self.assertTrue(is_palindrome([1, 2, 3, 4, 5, 4, 3, 2, 1]))
        self.assertTrue(is_palindrome(['a', 'b', 'c', 'd', 'c', 'b', 'a']))
        self.assertTrue(is_palindrome(['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a']))
        self.assertFalse(is_palindrome([1, 2, 4, 5, 6, 2, 1]))
        self.assertFalse(is_palindrome(["a", "b", "c", "d", "e"]))
        self.assertRaises(TypeError, is_palindrome, {})

    def test_flatten(self):
        """Test flatten (P07)."""
        self.assertEqual(flatten([1, 2, [3, 4], [5, 6, [7, [8]]]]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(flatten([1, [2, [3, [4, [5], 6], 7], 8], 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(flatten([['a', [['b', 'c'], ['d']]], ['e']]), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(flatten([[[['a', ['b']]], 'c']]), ['a', 'b', 'c'])
        self.assertEqual(flatten(['a']), ['a'])
        self.assertEqual(flatten([]), [])
        self.assertRaises(TypeError, flatten, {})

    def test_compress(self):
        """Test compress (P08)."""
        self.assertEqual(compress([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]), [1, 2, 3, 1, 4, 5])
        self.assertEqual(compress(['a', 'a', 'a', 'b', 'b', 'c', 'd', 'd']), ['a', 'b', 'c', 'd'])
        self.assertEqual(compress(['a', 'a', 'a']), ['a'])
        self.assertEqual(compress([]), [])
        self.assertRaises(TypeError, compress, {})

    def test_pack(self):
        """Test pack (P09)."""
        self.assertEqual(
            pack([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]),
            [[1, 1, 1, 1], [2], [3, 3], [1, 1], [4], [5, 5, 5, 5]]
        )
        self.assertEqual(
            pack(['a', 'a', 'a', 'b', 'b', 'c', 'd', 'd']),
            [['a', 'a', 'a'], ['b', 'b'], ['c'], ['d', 'd']]
        )
        self.assertEqual(pack(['a']), [['a']])
        self.assertRaises(TypeError, pack, {})

    def test_encode(self):
        """Test encode (P10)."""
        self.assertEqual(
            encode([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]),
            [[4, 1], [1, 2], [2, 3], [2, 1], [1, 4], [4, 5]]
        )
        self.assertEqual(
            encode(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']),
            [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]
        )
        self.assertEqual(encode(['a', 'a']), [[2, 'a']])
        self.assertEqual(encode(['a', 'b']), [[1, 'a'], [1, 'b']])
        self.assertRaises(TypeError, encode, {})

    def test_encode_modified(self):
        """Test encode_modified (P11)."""
        self.assertEqual(
            encode_modified([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]),
            [[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]
        )
        self.assertEqual(
            encode_modified(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']),
            [[4, 'a'], 'b', [2, 'c'], [2, 'a'], 'd', [4, 'e']]
        )
        self.assertEqual(encode_modified(['a', 'a']), [[2, 'a']])
        self.assertEqual(encode_modified(['a', 'b']), ['a', 'b'])
        self.assertRaises(TypeError, encode_modified, {})

    def test_decode(self):
        """Test decode (P12)."""
        self.assertEqual(
            decode([[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]),
            [1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]
        )
        self.assertEqual(
            decode([[4, 'a'], 'b', [2, 'c'], [2, 'a'], 'd', [4, 'e']]),
            ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
        )
        self.assertEqual(decode([[2, 'a']]), ['a', 'a'])
        self.assertEqual(decode(['a', 'b']), ['a', 'b'])
        self.assertRaises(TypeError, decode, {})

    def test_encode_direct(self):
        """Test encode_direct (P13)."""
        self.assertEqual(
            encode_direct([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]),
            [[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]
        )
        self.assertEqual(
            encode_direct(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']),
            [[4, 'a'], 'b', [2, 'c'], [2, 'a'], 'd', [4, 'e']]
        )
        self.assertEqual(encode_direct(['a', 'a']), [[2, 'a']])
        self.assertEqual(encode_direct(['a', 'b']), ['a', 'b'])
        self.assertRaises(TypeError, encode_direct, {})

    def test_duplicate(self):
        """Test duplicate (P14)."""
        self.assertEqual(duplicate([1, 2, 3, 3, 4, 5]), [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5])
        self.assertEqual(duplicate(['a', 'b', 'c', 'd']), ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'])
        self.assertRaises(TypeError, duplicate, {})

    def test_duplicate_times(self):
        """Test duplicate_times (P15)."""
        self.assertEqual(duplicate_times([1, 2, 3], 3), [1, 1, 1, 2, 2, 2, 3, 3, 3])
        self.assertEqual(duplicate_times(['a', 'b', 'c'], 2), ['a', 'a', 'b', 'b', 'c', 'c'])
        self.assertEqual(duplicate_times(['a', 'b'], 4), ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'])
        self.assertRaises(TypeError, duplicate_times, {})

    def test_drop(self):
        """Test drop (P16)."""
        self.assertEqual(drop([1, 2, 3, 4, 5, 6, 7, 8], 3), [1, 2, 4, 5, 7, 8])
        self.assertEqual(drop(['a', 'b', 'c', 'd'], 2), ['a', 'c'])
        self.assertEqual(drop([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])
        self.assertRaises(ValueError, drop, [1, 2, 3, 4, 5], 6)
        self.assertRaises(TypeError, drop, {}, 2)

    def test_split(self):
        """Test split (P17)."""
        self.assertEqual(split([1, 2, 3, 4, 5, 6, 7, 8, 9], 4), ([1, 2, 3, 4], [5, 6, 7, 8, 9]))
        self.assertEqual(split(['a', 'b', 'c', 'd', 'e'], 2), (['a', 'b'], ['c', 'd', 'e']))
        self.assertEqual(split([1, 2, 3, 4, 5], 5), ([1, 2, 3, 4, 5], []))
        self.assertEqual(split([1, 2, 3, 4, 5], 0), ([], [1, 2, 3, 4, 5]))
        self.assertRaises(ValueError, split, [1, 2, 3, 4, 5], 6)
        self.assertRaises(TypeError, split, {}, 2)

    def test_slice_list(self):
        """Test slice (P18)."""
        self.assertEqual(slice_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7), [3, 4, 5, 6, 7])
        self.assertEqual(slice_list(['a', 'b', 'c', 'd', 'e'], 1, 4), ['a', 'b', 'c', 'd'])
        self.assertEqual(slice_list(['a', 'b', 'c', 'd', 'e'], 1, 5), ['a', 'b', 'c', 'd', 'e'])
        self.assertRaises(ValueError, slice_list, [1, 2, 3, 4, 5], 0, 3)
        self.assertRaises(ValueError, slice_list, [1, 2, 3, 4], 1, 7)
        self.assertRaises(TypeError, slice_list, {}, 3, 5)

    def test_rotate(self):
        """Test rotate (P19)."""
        self.assertEqual(rotate([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [4, 5, 6, 7, 8, 9, 1, 2, 3])
        self.assertEqual(rotate([1, 2, 3, 4, 5, 6, 7, 8, 9], -2), [8, 9, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(rotate(['a', 'b', 'c', 'd', 'e'], 7), ['c', 'd', 'e', 'a', 'b'])
        self.assertEqual(rotate(['a', 'b', 'c', 'd', 'e'], -7), ['d', 'e', 'a', 'b', 'c'])
        self.assertRaises(TypeError, rotate, {}, 2)

    def test_remove_kth_element(self):
        """Test remove_kth_element (P20)."""
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5, 6, 7, 8], 3), [1, 2, 4, 5, 6, 7, 8])
        self.assertEqual(remove_kth_element(['a', 'b', 'c', 'd'], 2), ['a', 'c', 'd'])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])
        self.assertRaises(ValueError, remove_kth_element, [1, 2, 3, 4, 5], 6)
        self.assertRaises(TypeError, remove_kth_element, {}, 2)

    def test_insert_at(self):
        """Test insert_at (P21)."""
        self.assertEqual(insert_at([1, 2, 3, 4, 5, 6], 6, 100), [1, 2, 3, 4, 5, 100, 6])
        self.assertEqual(insert_at(['a', 'b', 'c', 'd'], 3, 'z'), ['a', 'b', 'z', 'c', 'd'])
        self.assertRaises(TypeError, insert_at, {}, 3, 100)
        self.assertRaises(ValueError, insert_at, [1, 2, 3], 4, 100)

    def test_range_list(self):
        """Test range_list (P22)."""
        self.assertEqual(range_list(7, 12), [7, 8, 9, 10, 11, 12])
        self.assertEqual(range_list(6, 10), [6, 7, 8, 9, 10])
        self.assertRaises(ValueError, range_list, 7, 3)

    def test_length_sort(self):
        """Test length_sort (P28(a))"""
        self.assertEqual(
            length_sort([[1, 2, 3], [4, 5], [6], [7, 8], [9, 10, 11]]),
            [[6], [4, 5], [7, 8], [1, 2, 3], [9, 10, 11]]
        )
        self.assertEqual(
            length_sort(
                [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'], ['i', 'j', 'k', 'l'],
                 ['m', 'n'], ['o']]),
            [['o'], ['d', 'e'], ['d', 'e'], ['m', 'n'], ['a', 'b', 'c'], ['f', 'g', 'h'],
             ['i', 'j', 'k', 'l']]
        )
        self.assertRaises(TypeError, length_sort, {})

    def test_length_frequency_sort(self):
        """Test length_sort (P28(b))"""
        self.assertEqual(
            length_frequency_sort([[1], [2], [3, 4], [5, 6, 7], [9], [10, 11]]),
            [[5, 6, 7], [3, 4], [10, 11], [1], [2], [9]]
        )
        self.assertEqual(
            length_frequency_sort(
                [['o'], ['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'],
                 ['i', 'j', 'k', 'l'], ['m', 'n']]),
            [['o'], ['i', 'j', 'k', 'l'], ['a', 'b', 'c'], ['f', 'g', 'h'], ['d', 'e'], ['d', 'e'],
             ['m', 'n']]
        )
        self.assertRaises(TypeError, length_frequency_sort, {})


if __name__ == '__main__':
    unittest.main()
