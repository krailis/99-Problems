// This package includes solutions to Arithmetic problems (31-41).
package arithmetic

import (
	"errors"
	"fmt"
	"gopkg.in/guregu/null.v3"
	"math"
	"math/rand"
	"time"
)

type IntSlice []int
type ISlice []interface{}

// IsPrime determines whether a given number is prime (P31).
func IsPrime(number int) bool {
	upperDivisor := int(math.Sqrt(float64(number))) + 1
	for divisor := 2; divisor < upperDivisor; divisor++ {
		if number%divisor == 0 {
			return false
		}
	}
	return true
}

// Gcd determines the greatest common divisor of two positive integer numbers (P32).
func Gcd(a int, b int) (int, error) {
	if a < 0 || b < 0 {
		return -1, errors.New("The given numbers are not positive.")
	}

	// Euclid's Algorithm
	if b == 0 {
		return a, nil
	} else {
		return Gcd(b, a%b)
	}
}

// IsCoprime determines if two positive integers are coprime (P33).
func IsCoprime(a int, b int) (null.Bool, error) {
	if a < 0 || b < 0 {
		return null.BoolFromPtr(nil), errors.New("The given numbers are not positive.")
	}

	gcd, _ := Gcd(a, b)
	return null.BoolFrom(gcd == 1), nil
}

// TotientPhi calculates Euler's totient function phi(m) (P34).
func TotientPhi(m int) (int, error) {
	if m < 1 {
		return -1, errors.New("The given number is not positive")
	}

	if m == 1 {
		return 1, nil
	}
	if IsPrime(m) {
		return m - 1, nil
	}
	coPrimes := 1
	for i := 2; i < int(m/2)+1; i++ {
		if m%i != 0 {
			if coPrime, _ := IsCoprime(i, m); coPrime.ValueOrZero() {
				coPrimes++
			}
		}
	}
	for i := int(m/2) + 1; i < m; i++ {
		if coPrime, _ := IsCoprime(i, m); coPrime.ValueOrZero() {
			coPrimes++
		}
	}
	return coPrimes, nil
}

// PrimeFactors determine the prime factors of a given positive number (P35).
func PrimeFactors(number int) IntSlice {
	if IsPrime(number) {
		return IntSlice{number}
	}
	primeFactors := IntSlice{}
	for number%2 == 0 {
		primeFactors = append(primeFactors, 2)
		number = int(number / 2)
	}
	for i := 3; i < int(math.Sqrt(float64(number)))+1; i += 2 {
		for number%i == 0 {
			primeFactors = append(primeFactors, i)
			number = int(number / i)
		}
	}
	if number > 2 {
		primeFactors = append(primeFactors, number)
	}
	return primeFactors
}

// PrimeFactorsMult returns the length-encoded prime factor list (P36).
func PrimeFactorsMult(number int) []IntSlice {
	primeFactors := PrimeFactors(number)
	encoded, current, count := []IntSlice{}, primeFactors[0], 1
	for _, factor := range primeFactors[1:] {
		if current != factor {
			encoded = append(encoded, IntSlice{count, current})
			current, count = factor, 1
			continue
		}
		count++
	}
	encoded = append(encoded, IntSlice{count, current})
	return encoded
}

// TotientPhi2 calculates Euler's totient function effectively (P37).
func TotientPhi2(m int) (int, error) {
	if m < 1 {
		return -1, errors.New("The given number is not positive")
	}

	if m == 1 {
		return 1, nil
	}
	phi := 1.0
	primeFactorsEncoded := PrimeFactorsMult(m)
	for _, elem := range primeFactorsEncoded {
		m, p := elem[0], elem[1]
		phi *= float64(p-1) * math.Pow(float64(p), float64(m-1))
	}
	return int(phi), nil
}

// CompareTotient compare the two methods of calculating Euler's totient function (P38).
func CompareTotient(numberOfTests int) {
	rand.Seed(time.Now().UnixNano())
	m := 0
	fmt.Println("--------------------------------------------")
	fmt.Printf("%s\t%10s\t%10s\n", "Argument", "TotientPhi", "TotientPhi2")
	fmt.Println("============================================")
	for i := 0; i < numberOfTests; i++ {
		m = rand.Intn(20000)
		// TotientPhi
		startTotientPhi := time.Now()
		TotientPhi(m)
		elapsedTotientPhi := time.Since(startTotientPhi)
		// TotientPhi2
		startTotientPhi2 := time.Now()
		TotientPhi2(m)
		elapsedTotientPhi2 := time.Since(startTotientPhi2)
		// Print time
		fmt.Printf("%6v\t\t%10v\t%11v\n", m, elapsedTotientPhi, elapsedTotientPhi2)
	}
	fmt.Println("--------------------------------------------")
}

// PrimeList returns a list of prime numbers (P39).
func PrimeList(lower int, upper int) IntSlice {
	// Sieve of Eratosthenes.
	array := make([]int, upper+1)
	for i := 2; i < int(math.Sqrt(float64(upper)))+1; i++ {
		if array[i] == 0 {
			j := i * i
			for j <= upper {
				array[j] = 1
				j += i
			}
		}
	}
	primeList := IntSlice{}
	for i := lower - 1; i < upper+1; i++ {
		if array[i] == 0 {
			primeList = append(primeList, i)
		}
	}
	return primeList
}

// Goldbach computes Goldbach's Conjecture (P40).
func Goldbach(number int) (IntSlice, error) {
	if number <= 2 {
		return nil, errors.New("The given number is smaller than 2.")
	}
	if number%2 == 1 {
		return nil, errors.New("The given number is odd.")
	}

	var prime int
	primeList := PrimeList(3, int(number/2))
	for _, prime = range primeList {
		if IsPrime(number - prime) {
			break
		}
	}
	return IntSlice{prime, number - prime}, nil
}

// GoldbachList returns a list of Goldbach compositions (P41).
func GoldbachList(lower int, upper int) ([]IntSlice, error) {
	goldbachList := []IntSlice{}
	if lower%2 == 1 {
		lower += 1
	}
	for i := lower; i < upper+1; i = i + 2 {
		numbers, err := Goldbach(i)
		if err != nil {
			return nil, err
		} else {
			goldbachList = append(goldbachList, numbers)
		}
	}
	return goldbachList, nil
}
