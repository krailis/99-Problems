"""arithmetic/arithmetic.py

This file includes solutions to Arithmetic Problems (31 - 40).

author(s):	Konstantinos Railis <kons.railis@gmail.com>

"""
import math
from timeit import Timer

from lists import pack


def is_prime(number: int):
    """Problem 31: Determine whether a given number is prime.

    Parameters
    ----------
    number : int
        The number to check for prime

    Returns
    -------
    bool
        `True` if number is prime, `False` otherwise

    """
    divisors = [x for x in range(2, number) if number % x == 0]
    return divisors == []


def gcd(a: int, b: int):
    """Problem 32: Determine the greatest common divisor of two positive integer numbers.

    Parameters
    ----------
    a : int
        An positive integer number
    b : int
        An positive integer number

    Returns
    -------
    int
        The greatest common divisor of the given numbers.

    Raises
    ------
    ValueError
        If the given numbers are negative

    """
    if a < 0 or b < 0:
        raise ValueError('The given numbers are not positive.')
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('The given numbers are not integers.')

    return a if b == 0 else gcd(b, a % b)


def is_co_prime(a: int, b: int):
    """Problem 33: Determine whether two positive integer numbers are co-prime.

    Parameters
    ----------
    a : int
        An positive integer number
    b : int
        An positive integer number

    Returns
    -------
    bool
        `True` if the given numbers are co-prime, `False` otherwise

    """
    if a < 0 or b < 0:
        raise ValueError('The given numbers are not positive.')
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('The given numbers are not integers.')

    return gcd(a, b) == 1


def prime_factors(number: int):
    """Problem 35: Determine the prime factors of a given positive number

    Parameters
    ----------
    number : int
        A positive integer number

    Returns
    -------
    list of int
        A list of the number's prime factors

    Raises
    ------
    ValueError
        If the given number is not positive

    """
    prime_factor_list = []
    if number % 2 == 0:
        # If 2 is repeated more than once we have 4 which is not a prime number
        prime_factor_list.append(2)
        number = number / 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        # Divide by i until not possible and then increase
        while number % i == 0:
            prime_factor_list.append(i)
            number = number / i
    if number > 2:
        prime_factor_list.append(number)
    return prime_factor_list


def totient_phi(m: int):
    """Problem 34: Calculate Euler's totient function phi(m).

    Parameters
    ----------
    m : int
        A positive integer number

    Returns
    -------
    int
        The totient of the given number

    Raises
    ------
    ValueError
        If the given number is not a positive integer

    """
    if m < 1:
        raise ValueError('The given number is not positive.')
    if not isinstance(m, int):
        raise ValueError('The given number is not an integer')

    if m == 1:
        return 1
    if is_prime(m):
        # If m is prime then it is co-prime with all numbers up to (m - 1)
        return m - 1

    # Firstly the prime factors are computed.
    prime_factor_list = prime_factors(m)

    # Non-prime factors are computed on the primes.
    all_factors = [x * y for x in prime_factor_list for y in prime_factor_list]
    all_factors.extend(prime_factor_list)

    # Subtract the factor set and keep all the non-factors.
    non_factor_set = set(range(1, m)) - set(all_factors)
    co_primes = [x for x in non_factor_set if is_co_prime(x, m)]

    return len(co_primes)


def prime_factors_mult(number: int):
    """Problem 36: Construct a list containing the prime factors and their multiplicity.

    Parameters
    ----------
    number : int
        An integer number

    Returns
    -------
    list of list
        A length-encoded list of factors

    """
    prime_factor_list = prime_factors(number)
    prime_factor_packed = pack(prime_factor_list)
    prime_factor_mult = []
    for x in prime_factor_packed:
        prime_factor_mult.append([x[0], len(x)])
    return prime_factor_mult


def totient_phi_2(m: int):
    """Problem 37: Calculate Euler's totient function phi(m) (improved).

    Parameters
    ----------
    m : int
        A positive integer number

    Returns
    -------
    int
        The totient of the given number

    Raises
    ------
    ValueError
        If the given number is not a positive integer

    """
    if m < 1:
        raise ValueError('The given number is not positive.')
    if not isinstance(m, int):
        raise ValueError('The given number is not an integer')

    if m == 1:
        return 1

    phi = 1
    prime_factor_encoded = prime_factors_mult(m)
    for element in prime_factor_encoded:
        phi *= (element[0] - 1) * (element[0] ** (element[1] - 1))
    return int(phi)


def compare_totient(number_of_tests: int):
    """Problem 38: Compare the two methods of calculating Euler's totient function.

    Parameters
    ----------
    number_of_tests : int
        The number of tests to run for comparison

    """
    import random
    print('%-25s | %-25s | %-25s' %
          ('Argument', 'Time of totient_phi (s)', 'Time of totient_phi_2 (s)'))
    for m in random.sample(range(6, 20000, 2), number_of_tests):
        stmt_phi = f'totient_phi({m})'
        setup_phi = 'from arithmetic import totient_phi'
        timer_phi = Timer(stmt=stmt_phi, setup=setup_phi)
        stmt_phi_2 = f'totient_phi_2({m})'
        setup_phi_2 = 'from arithmetic import totient_phi_2'
        timer_phi_2 = Timer(stmt=stmt_phi_2, setup=setup_phi_2)
        print('%-25s | %-25s | %-25s' %
              (m, str(timer_phi.timeit(number=100)), str(timer_phi_2.timeit(number=100))), end='\r')


def primes_list(lower, upper):
    """Problem 39: A list of prime numbers

    Parameters
    ----------
    lower : int
        The lower bound of the prime numbers to return
    upper : int
        The upper bound of the prime numbers ro return

    Returns
    -------
    list of int
        A list of prime integer numbers

    """
    # Implemented the Sieve of Eratosthenes
    a = (upper + 1) * [True]
    for i in range(2, int(math.sqrt(upper)) + 1):
        if a[i]:
            j = i * i
            while j <= upper:
                a[j] = False
                j += i
    return [i + lower for i, x in enumerate(a[lower:]) if x]


def goldbach(number: int):
    """Problem 40: Goldbach's conjecture.

    Parameters
    ----------
    number : int
        A positive integer number

    Returns
    -------
    list of int
        A pair of prime numbers that sum up to the initial given number.

    Raises
    ------
    ValueError
        If the given number is not a positive even number

    """
    if number <= 2 or number % 2 != 0:
        raise ValueError('The given number is even and greater than 2.')

    prime_list = primes_list(3, int(number / 2))
    for prime in prime_list:
        if is_prime(number - prime):
            return [prime, number - prime]


def goldbach_list(lower, upper):
    """Problem 40: A list of Goldbach's conjecture.

    Parameters
    ----------
    lower : int
        A positive integer number
    upper : int
        A positive integer number

    Returns
    -------
    list of int
        A pair of prime numbers that sum up to the initial given number.

    Raises
    ------
    ValueError
        If the given number is not a positive even number

    """
    gb_list = []
    if lower % 2 == 1:
        lower = lower + 1
    for number in range(lower, upper + 1, 2):
        gb_list.append(goldbach(number))
    return gb_list
