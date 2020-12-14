package arithmetic

import (
  "errors"
  "lists"
  "math"
  "gopkg.in/guregu/null.v3"
)

type IntSlice []int

func IsPrime(number int) bool {
  upperDivisor := int(math.Sqrt(float64(number))) + 1
  for divisor := 2; divisor < upperDivisor ; divisor++ {
    if number % divisor == 0 {
      return false
    }
  }
  return true
}

func Gcd(a int, b int) (int, error) {
  if a < 0 || b < 0 {
    return -1, errors.New("The given numbers are not positive.")
  }

  // Euclid's Algorithm
  if b == 0 {
    return a, nil
  } else {
    return Gcd(b, a % b)
  }
}

func IsCoprime(a int, b int) (null.Bool, error) {
  if a < 0 || b < 0 {
    return null.BoolFromPtr(nil), errors.New("The given numbers are not positive.")
  }

  gcd, _ := Gcd(a, b)
  return null.BoolFrom(gcd == 1), nil
}

func PrimeFactors(number int) IntSlice {
  if IsPrime(number) {
    return IntSlice{number}
  }
  primeFactors := IntSlice{}
  for number % 2 == 0 {
    primeFactors = append(primeFactors, 2)
    number = int(number / 2)
  }
  for i := 3; i < int(math.Sqrt(float64(number))) + 1; i += 2 {
    for number % i == 0 {
      primeFactors = append(primeFactors, i)
      number = int(number / i)
    }
  }
  if number > 2 {
    primeFactors = append(primeFactors, number)
  }
  return primeFactors
}

func PrimeFactorsMult(number int) []interface{} {
  return lists.Encode(PrimeFactors(number))
}
