# My attempt to solve the 99 Prolog problems in Python
# This file includes solutions to problems 30 - 31

import math
import sys
sys.path.insert(0, '../')
from Lists.p01_to_p10_solutions.solutions_1_10 import s9_packConsecutiveDuplicates
from timeit import Timer

# Problem 1: Determine whether a given number is prime
def s31_isPrime (n):
	divisors = [x for x in range(2, n) if (n % x == 0)]
	return (divisors == [])

# Problem 2: Determine the prime factors of a given positive number
def s32_primeFactors (n):
	primeFactors = []
	# If 2 is repeated more than once we have 4 which is not a prime number
	if (n % 2 == 0):
		primeFactors.append(2)
		n = n / 2
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		# Divide by i until not possible and then increase
		while (n % i == 0):
			primeFactors.append(i)
			n = n / i
	if (n > 2):
		primeFactors.append(n)
	return primeFactors

# Problem 3: Determine the prime factors of a given positive number(2)
def s33_primeFactorsMult (n):
	primeFactors = s32_primeFactors(n)
	primeFactorsPacked = s9_packConsecutiveDuplicates(primeFactors)
	primeFactorsMult = []
	for x in primeFactorsPacked:
		primeFactorsMult.append([x[0], len(x)])
	return primeFactorsMult

# Problem 4: A list of prime numbers
def s34_primesList (lower, upper):
	# Implemented the Sieve of Eratosthenes
	a = [True for i in range(0, upper + 1)]
	for i in range(2, int(math.sqrt(upper)) + 1):
		if (a[i]):
			j = i * i
			while (j <= upper):
				a[j] = False
				j += i
	return [i + lower for i, x in enumerate(a[lower:]) if x]

	
# Problem 5: Goldbach's conjecture
def s35_goldbach (n):
	primesList = s34_primesList(3, int(n / 2))
	for x in primesList:
		if (s31_isPrime(n - x)):
			return [x, n - x]
			

# Problem 6: A list of Goldbach compositions
def s36_goldbachList (lower, upper):
	gbList = []
	if lower % 2 == 1:
		lower = lower + 1
	for i in range(lower, upper + 1, 2):
		gbList.append(s35_goldbach(i))
	return gbList

# Problem 7: Determine the greatest common divisor of two prositive integer numbers
def s37_gcd (a, b):
	# A version of Euclid's algorithm
	if (b == 0):
		return a
	else:
		return s37_gcd(b, a % b)

# Problem 8: Determine whether two positive integer numbers are coprime
def s38_coprime (a, b):
	return (s37_gcd(a, b) == 1)

# Problem 9: 
def s39_totientPhi (m):
	if (m == 1):
		return 1
	# If m is prime then it is coprime with all numbers up to (m - 1)
	if (s31_isPrime(m)):
		return (m - 1);
	# Narrow down the search for coprimes by removing the factors of m
	primeFactors = s32_primeFactors(m)
	allFactors = [x*y for x in primeFactors for y in primeFactors]
	allFactors.extend(primeFactors)
	checkCoprimality = set(range(1, m)) - set(allFactors)
	# Checking coprimality
	coprimesList = [x for x in checkCoprimality if s38_coprime(x, m)]
	return len(coprimesList)

# Problem 10: Calculate Euler's totient function phi(m)
def s40_totientPhi_2 (m):
	if (m == 1):
		return 1
	Phi = 1
	primeFactorsMult = s33_primeFactorsMult(m)
	for x in primeFactorsMult:
		Phi *= (x[0] - 1) * (x[0]**(x[1] - 1))
	return int(Phi)	

# Problem 11: Compare the two methods of calculating Euler's totient function
def s41_compareTotient (nTests):
	import random
	print("%-25s | %-25s" % ("Function Call", "Execution Time"))
	for m in random.sample(range(6, 20000, 2), nTests):
		input = "(" + str(m) +")"
		for func in ("s39_totientPhi", "s40_totientPhi_2"):
			stmt = func + input
			setup = "from __main__ import %s" % func
			timer = Timer(stmt = stmt, setup = setup)
			print("%-25s | %-25s" % (stmt, str(timer.timeit(number=100))))
