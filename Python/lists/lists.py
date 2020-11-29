"""lists/lists.py

This file includes solutions to List Problems (1 - 28)

author(s): Konstantinos Railis <kons.railis@gmail.com>

"""
import itertools
import random


def last_element(list_a: list):
    """Problem 1: Find The Last Element of a List.

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    element
        The last element of the list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the input list does not contain elements

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if len(list_a) < 1:
        raise ValueError('The input list does not contain any elements.')
    return list_a[-1]


def last_but_one(list_a: list):
    """Problem 2: Find the Last but One Element of a List.

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    element
        The second to last element of the list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the input list contains less than two elements

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if len(list_a) < 2:
        raise ValueError('The input list contains less than two elements.')
    return list_a[-2]


def kth_element(list_a: list, k: int):
    """Problem 3: Find the K'th Element of a List

    Parameters
    ----------
    list_a : list
        The input list
    k : int
        The element to fetch

    Returns
    -------
    element
        The k'th element of the input list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the input list contains less than two elements, or the given k is less than 1

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if len(list_a) < k:
        raise ValueError(f'The input list contains less than [{k}] elements.')
    if k < 1:
        raise ValueError('The value of k cannot be less than 1.')
    return list_a[k - 1]


def length(list_a: list):
    """Problem 4: Find the number of Elements of a List.

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    integer
        The length of the input list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    return len(list_a)


def reverse(list_a: list):
    """Problem 5: Reverse a List.

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    list_a : list
        The input list reversed

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    list_a.reverse()
    return list_a


def is_palindrome(list_a: list):
    """Problem 6: Find out whether a list is palindrome

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    bool
        `True` if the list is palindrome, `False` otherwise

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    # Compare elements of the list symmetrically. If any two symmetric
    # elements differ then the list is not palindrome
    for i in range(0, int(len(list_a) / 2)):
        if list_a[i] != list_a[-1 - i]:
            return False
    return True


def flatten(list_a: list):
    """Problem 7: Flatten a Nested List Structure,

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    flat : list
        The flattened input list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    flat = []
    for x in list_a:
        if isinstance(x, list):
            # If element x is a list then the initial list should be
            # extended by the elements of list x
            flat.extend(flatten(x))
        else:
            # Otherwise a single element is appended
            flat.append(x)

    return flat


def compress(list_a: list):
    """Problem 8: Eliminate Consecutive Duplicates of List.

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    list
        A list with consecutive duplicates eliminated.

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    if len(list_a) <= 1:
        return list_a

    compressed = [list_a[0]]
    for element in list_a:
        if compressed[-1] == element:
            continue
        compressed.append(element)

    return compressed


def pack(list_a: list):
    """Problem 9: Pack Consecutive Duplicates of a List.

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    list of list
        A list of lists packed with consecutive duplicates

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    if len(list_a) <= 1:
        # In case of empty or one-element list return.
        return list_a

    packed, sublist = [], [list_a[0]]
    for element in list_a[1:]:
        if sublist[-1] != element:
            # If current element does not match the last of the sublist
            # extend packed list and reset sublist to a single-element
            packed.append(sublist)
            sublist = [element]
        else:
            # If another same element is found, append to the sublist
            sublist.append(element)
    packed.append(sublist)

    return packed


def encode(list_a: list):
    """Problem 10: Run Length Encoding of List.

    Parameters
    ----------
    list_a : list of list
        The input list

    Returns
    -------
    list of list
        An length-encoded list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    # After packing the list using the previous function use the
    # sublist length and append the new pair to the output list
    encoded = []
    packed = pack(list_a)
    for x in packed:
        encoded.append([len(x), x[0]])

    return encoded


def encode_modified(list_a: list):
    """Problem 11: Modified Length Encoding of List.

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    list
        A modified length-encoded list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    encoded = []
    packed = pack(list_a)
    for x in packed:
        if len(x) > 1:
            encoded.append([len(x), x[0]])
        else:
            encoded.append(x[0])

    return encoded


def decode(encoded: list):
    """Problem 12: Decode a run-length encoded list.

    Parameters
    ----------
    encoded : list
        The encoded input list

    Returns
    -------
    list
        The decoded list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(encoded, list):
        raise TypeError('The argument given is not of `list` type.')

    decoded = []
    for x in encoded:
        if isinstance(x, list):
            decoded.extend(x[0] * [x[1]])
        else:
            decoded.append(x)

    return decoded


def encode_direct(list_a: list):
    """Problem 13: Run-length encoding of a list (direct solution).

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    list of list
        An length-encoded list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    if len(list_a) <= 1:
        # In case of empty or one-element list return.
        return list_a

    encoded, current, count = [], list_a[0], 1
    for element in list_a[1:]:
        if current != element:
            # If current element does not match the recorded current
            # append the count to the list
            encoded.append(current if count == 1 else [count, current])
            current, count = element, 1
        else:
            # If another same element is found, increase counter
            count += 1
    encoded.append(current if count == 1 else [count, current])

    return encoded


def duplicate(list_a: list):
    """Problem 14: Duplicate the Elements of a list.

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    list
        A list of duplicated elements in order

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    duplicated = []
    for x in list_a:
        duplicated.extend([x, x])

    return duplicated


def duplicate_times(list_a: list, times: int):
    """Problem 15: Duplicate the elements of a list a given number of times.

    Parameters
    ----------
    list_a : list
        The input list
    times : int
        The number of times to duplicate elements

    Returns
    -------
    list
        A list of n-times duplicated elements

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the given `times` value is smaller than or equal to zero

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if times <= 0:
        raise ValueError('An invalid value was given for `times`.')

    if times == 1:
        return list_a

    duplicated = []
    for x in list_a:
        duplicated.extend(times * [x])
    return duplicated


def drop(list_a: list, period: int):
    """Problem 16: Drop every N'th element from a list

    Parameters
    ----------
    list_a : list
        The input list
    period : int
        The number of every N elements to drop

    Returns
    -------
    list
        A list without a number of dropped elements.

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the given `n` is greater than the list's length or smaller than 1

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if period > len(list_a) or period < 1:
        raise ValueError('The value of `period` is not valid.')

    return [x for i, x in enumerate(list_a) if (i + 1) % period != 0]


def split(list_a: list, length_of_first: int):
    """Problem 17: Split a list in two parts; the length of the first list is given.

    Parameters
    ----------
    list_a : list
        The input list
    length_of_first : int
        The desired length of the first output list

    Returns
    -------
    (list, list)
        A tuple of lists

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the given `n` is greater than the list's length or smaller than 1

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if length_of_first > len(list_a) or length_of_first < 0:
        raise ValueError('The value of `l` is not valid.')

    return list_a[:length_of_first], list_a[length_of_first:]


def slice_list(list_a: list, start: int, end: int):
    """Problem 18: Extract a slice from list.

    Parameters
    ----------
    list_a : list
        The input list
    start : int
        The start of the slice
    end : int
        The end of the slice

    Returns
    -------
    list
        A slice of the initial list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the values of `start` and / or `end` are invalid

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if start < 1 or len(list_a) < start:
        raise ValueError('The value of `start` argument is not valid')
    if end < start or len(list_a) < end:
        raise ValueError('The value of `end` argument is not valid')

    return list_a[(start - 1):end]


def rotate(list_a: list, places: int):
    """Problem 19: Rotate a List N places to the left.

    Parameters
    ----------
    list_a : list
        The input list
    places : int
        The number of places to rotate the list to the left

    Returns
    -------
    list
        A list rotated n places to the left.

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    places = places % len(list_a)
    rotated = list_a[places:]
    rotated.extend(list_a[:places])
    return rotated


def remove_kth_element(list_a: list, index: int):
    """Problem 20: Remove K'th element from list.

    Parameters
    ----------
    list_a : list
        The input list
    index : int
        The element number to remove from the list

    Returns
    -------
    list
        The input list without the removed element

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the given `k` is not valid.

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if index < 0 or len(list_a) < index:
        raise ValueError('The argument `k` is not valid.')

    list_a.pop(index - 1)
    return list_a


def insert_at(list_a: list, position: int, item):
    """Problem 21: Insert element at a given position into a list.

    Parameters
    ----------
    list_a : list
        The input list
    position : int
        The position where the inserted element should be
    item
        The element to insert to the list

    Returns
    -------
    list
        A list with an inserted element at the proper position

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the given `k` is not valid.

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if position < 0 or len(list_a) < position:
        raise ValueError('The value of `n` is not valid.')

    list_a.insert(position - 1, item)
    return list_a


def range_list(start: int, end: int):
    """Problem 22: Create a list containing all integers within a given range.

    Parameters
    ----------
    start : int
    end : int

    Returns
    -------
    list
        A list including all numbers from `start` to `end`

    Raises
    ------
    ValueError
        If the given `start` is smaller than `end`

    """
    if end < start:
        raise ValueError('The `end` argument is smaller than `start`.')

    return list(range(start, end + 1))


def rnd_select(list_a: list, n: int):
    """Problem 23: Extract a given number of randomly selected items from a list.

    Parameters
    ----------
    list_a : list
        The input list
    n : int
        The number of elements to randomly select

    Returns
    -------
    list
        A list of `n` randomly selected numbers out of the initial list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the given `start` is smaller than `end`

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if n < 0 or len(list_a) < n:
        raise ValueError('The value of the given `n` is invalid.')

    return random.sample(list_a, n)


def lotto(n: int, m: int):
    """Problem 24: Lotto; Draw N different random numbers from the set 1..M.

    Parameters
    ----------
    n : int
        The number of numbers to draw
    m : int
        The upper limit of the set to draw numbers from

    Returns
    -------
    list
        A list of randomly selected numbers from the set 1..m

    Raises
    ------
    ValueError
        If the value of `n` or `m` is invalid.

    """
    if n < 0 or m < 1:
        raise ValueError('The given values are invalid.')
    if m < n:
        raise ValueError('The value of numbers to draw cannot be greater than the range.')

    return rnd_select(range_list(1, m), n)


def rnd_permutation(list_a: list):
    """Problem 25: Generate Random Permutation of List.

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    list
        A random permutation of the input list as a list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    return rnd_select(list_a, len(list_a))


def combination(list_a: list, k: int):
    """Problem 26: Generate the combinations of K distinct objects chosen from N elements of list.

    Parameters
    ----------
    list_a : list
        The input list
    k : int
        The number of objects to use in each combination

    Returns
    -------
    list
        A list of combinations of k elements out of the input list

    Raises
    ------
    TypeError
        If the given argument is not of `list` type
    ValueError
        If the given `k` is not valid.

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')
    if k < 1 or len(list_a) < k:
        raise ValueError('The given value of `k` is not valid.')

    return list(itertools.combinations(list_a, k))


def disjoint_subsets(list_a: list, groups):
    """Problem 27: Group elements of set into disjoint subsets.

    Parameters
    ----------
    list_a : list
        The input list
    groups

    Returns
    -------

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    set_a = set(list_a)
    # Find all combinations with the given plurality of the first subset
    first_set = itertools.combinations(set_a, groups[0])
    disjoint_list = []
    for x in first_set:
        # For every subset of the possible combinations of the first
        # group, remove its members and find all combinations with
        # given plurality of the second subset
        temp_subset = set_a - set(x)
        second_set = itertools.combinations(temp_subset, groups[1])
        list_x = list(x)
        for y in second_set:
            subset = [list_x, list(y), list(temp_subset - set(y))]
            disjoint_list.append(subset)
    return disjoint_list


def length_sort(list_a: list):
    """Problem 28: (a) Sort lists according to length of sublists

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    list of list
        A list sorted according to length of sublists

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    return sorted(list_a, key=len)


def length_frequency_sort(list_a: list):
    """Problem 28: (b) Sort lists according to length frequency of sublists

    Parameters
    ----------
    list_a : list
        The input list

    Returns
    -------
    list of list
        A list of lists sorted according to the length frequency of the sublists

    Raises
    ------
    TypeError
        If the given argument is not of `list` type

    """
    if not isinstance(list_a, list):
        raise TypeError('The argument given is not of `list` type.')

    sorted_list = []
    list_length_dict = dict()
    for list_length in list(map(len, list_a)):
        list_length_dict[list_length] = [y for y in list_a if len(y) == list_length]
    length_sorted = sorted(list_length_dict.values(), key=len)
    for sublist in length_sorted:
        sorted_list.extend(sublist)

    return sorted_list
