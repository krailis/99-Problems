package arithmetic

import (
	"fmt"
	"gopkg.in/guregu/null.v3"
	"reflect"
	"testing"
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

// TestTotientPhi tests the solution of P34.
func TestTotientPhi(t *testing.T) {
	var testCases = []struct {
		x int
		y int
	}{
		{10, 4},
		{17, 16},
		{39, 24},
		{198, 60},
		{24420, 5760},
	}

	for _, testCase := range testCases {
		testName := fmt.Sprint(testCase.x)
		t.Run(testName, func(t *testing.T) {
			ans, _ := TotientPhi(testCase.x)
			if ans != testCase.y {
				t.Errorf("Expected %v but the result was %v", testCase.y, ans)
			}
		})
	}
}

// TestPrimeFactors tests the solution of P35.
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

// TestPrimeFactorsMult tests the solution of P36.
func TestPrimeFactorsMult(t *testing.T) {
	var testCases = []struct {
		x int
		y []IntSlice
	}{
		{
			315, []IntSlice{IntSlice{2, 3}, IntSlice{1, 5}, IntSlice{1, 7}},
		},
		{
			430, []IntSlice{IntSlice{1, 2}, IntSlice{1, 5}, IntSlice{1, 43}},
		},
		{
			728, []IntSlice{IntSlice{3, 2}, IntSlice{1, 7}, IntSlice{1, 13}},
		},
		{
			999, []IntSlice{IntSlice{3, 3}, IntSlice{1, 37}},
		},
		{
			1725, []IntSlice{IntSlice{1, 3}, IntSlice{2, 5}, IntSlice{1, 23}},
		},
	}

	for _, testCase := range testCases {
		testName := fmt.Sprint(testCase.x)
		t.Run(testName, func(t *testing.T) {
			ans := PrimeFactorsMult(testCase.x)
			if !(reflect.DeepEqual(ans, testCase.y)) {
				t.Errorf("Expected %v but the result was %v", testCase.y, ans)
			}
		})
	}
}

// TestTotientPhi2 tests the solution of P37.
func TestTotientPhi2(t *testing.T) {
	var testCases = []struct {
		x int
		y int
	}{
		{10, 4},
		{17, 16},
		{39, 24},
		{198, 60},
		{24420, 5760},
	}

	for _, testCase := range testCases {
		testName := fmt.Sprint(testCase.x)
		t.Run(testName, func(t *testing.T) {
			ans, _ := TotientPhi2(testCase.x)
			if ans != testCase.y {
				t.Errorf("Expected %v but the result was %v", testCase.y, ans)
			}
		})
	}
}

// TestRandomPermutation runs the solution of problem P38.
func TestCompareTotien(t *testing.T) {
	var testCases = []struct {
		x int
	}{
		{
			10,
		},
		{
			50,
		},
	}

	for _, testCase := range testCases {
		testName := fmt.Sprint(testCase.x)
		t.Run(testName, func(t *testing.T) {
			CompareTotient(testCase.x)
		})
	}
}

// TestPrimeFactors tests the solution of P39.
func TestPrimeList(t *testing.T) {
	var testCases = []struct {
		lower int
		upper int
		y     IntSlice
	}{
		{9, 41, IntSlice{11, 13, 17, 19, 23, 29, 31, 37, 41}},
		{3923, 4002, IntSlice{3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001}},
		{5003, 5024, IntSlice{5003, 5009, 5011, 5021, 5023}},
		{283, 312, IntSlice{283, 293, 307, 311}},
		{2131, 2142, IntSlice{2131, 2137, 2141}},
	}

	for _, testCase := range testCases {
		testName := fmt.Sprint(testCase.lower, testCase.upper)
		t.Run(testName, func(t *testing.T) {
			ans := PrimeList(testCase.lower, testCase.upper)
			if !(reflect.DeepEqual(ans, testCase.y)) {
				t.Errorf("Expected %v but the result was %v", testCase.y, ans)
			}
		})
	}
}

// TestGoldbach tests the solution of P40.
func TestGoldbach(t *testing.T) {
	var testCases = []struct {
		number int
		y      IntSlice
	}{
		{28, IntSlice{5, 23}},
		{30, IntSlice{7, 23}},
		{1002, IntSlice{5, 997}},
		{1004, IntSlice{7, 997}},
		{10000, IntSlice{59, 9941}},
		{5000, IntSlice{7, 4993}},
	}

	for _, testCase := range testCases {
		testName := fmt.Sprint(testCase.number)
		t.Run(testName, func(t *testing.T) {
			ans, _ := Goldbach(testCase.number)
			if !(reflect.DeepEqual(ans, testCase.y)) {
				t.Errorf("Expected %v but the result was %v", testCase.y, ans)
			}
		})
	}
}

// TestGoldbach tests the solution of P41.
func TestGoldbachList(t *testing.T) {
	var testCases = []struct {
		lower int
		upper int
		y     []IntSlice
	}{
		{
			9, 20,
			[]IntSlice{
				IntSlice{3, 7}, IntSlice{5, 7}, IntSlice{3, 11},
				IntSlice{3, 13}, IntSlice{5, 13}, IntSlice{3, 17},
			},
		},
		{
			28, 36,
			[]IntSlice{
				IntSlice{5, 23}, IntSlice{7, 23}, IntSlice{3, 29},
				IntSlice{3, 31}, IntSlice{5, 31},
			},
		},
		{
			240, 246,
			[]IntSlice{
				IntSlice{7, 233}, IntSlice{3, 239}, IntSlice{3, 241}, IntSlice{5, 241}},
		},
	}

	for _, testCase := range testCases {
		testName := fmt.Sprint(testCase.lower, testCase.upper)
		t.Run(testName, func(t *testing.T) {
			ans, _ := GoldbachList(testCase.lower, testCase.upper)
			if !(reflect.DeepEqual(ans, testCase.y)) {
				t.Errorf("Expected %v but the result was %v", testCase.y, ans)
			}
		})
	}
}
