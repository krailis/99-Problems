package arithmetic

import (
  "fmt"
  "reflect"
  "testing"
  "gopkg.in/guregu/null.v3"
)

// TestIsPrime tests the solution of P31.
func TestIsPrime(t *testing.T) {
  var testCases = []struct {
    x int
    y bool
  }{
    {7, true},
    {31, true},
    {101, true},
    {49, false},
    {122, false},
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := IsPrime(testCase.x)
      if ans != testCase.y {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

// TestGcd tests the solution of P32.
func TestGcd(t *testing.T) {
  var testCases = []struct {
    a int
    b int
    y int
  }{
    {36, 63, 9},
    {78, 32, 2},
    {35, 49, 7},
    {32, 112, 16},
    {33, 132, 33},
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.a, testCase.b)
    t.Run(testName, func(t *testing.T) {
      ans, _ := Gcd(testCase.a, testCase.b)
      if ans != testCase.y {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

// TestIsCoprime tests the solution of P33.
func TestIsCoprime(t *testing.T) {
  var testCases = []struct {
    a int
    b int
    y null.Bool
  }{
    {35, 64, null.BoolFrom(true)},
    {35, 49, null.BoolFrom(false)},
    {35, 56, null.BoolFrom(false)},
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.a, testCase.b)
    t.Run(testName, func(t *testing.T) {
      ans, _ := IsCoprime(testCase.a, testCase.b)
      if ans != testCase.y {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

// TestPrimeFactors tests the solution of P34.
func TestPrimeFactors(t *testing.T) {
  var testCases = []struct {
    x int
    y IntSlice
  }{
    {315, IntSlice{3, 3, 5, 7}},
    {430, IntSlice{2, 5, 43}},
    {728, IntSlice{2, 2, 2, 7, 13}},
    {999, IntSlice{3, 3, 3, 37}},
    {1725, IntSlice{3, 5, 5, 23}},
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := PrimeFactors(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}
