// Package lists includes solutions to List Problems (1-28).
package lists

import (
	"errors"
	"math/rand"
	"sort"
	"time"
)

type Slice []string
type ISlice []interface{}
type LengthEncodedPair struct {
	length int
	str    string
}

type ByLength []Slice

func (a ByLength) Len() int           { return len(a) }
func (a ByLength) Less(i, j int) bool { return len(a[i]) < len(a[j]) }
func (a ByLength) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }

type ByLength2 [][]Slice

func (a ByLength2) Len() int           { return len(a) }
func (a ByLength2) Less(i, j int) bool { return len(a[i]) < len(a[j]) }
func (a ByLength2) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }

// LastElement find The Last Element of a Slice (P01).
func LastElement(s Slice) (string, error) {
	length := len(s)
	if length < 1 {
		return "", errors.New("The given list is empty. Try again with a non-empty list.")
	}
	return s[length-1], nil
}

// LastButOneElement finds the Last but One Element of a Slice (P02).
func LastButOneElement(s Slice) (string, error) {
	length := len(s)
	if length < 2 {
		return "", errors.New("The given list has fewer elements than needed.")
	}
	return s[length-2], nil
}

// KthElement finds the k'th Element of a Slice (P03).
func KthElement(s Slice, k int) (string, error) {
	length := len(s)
	if length < k {
		return "", errors.New("The given list's length is smaller than the given k.")
	}
	return s[k-1], nil
}

// Length finds the lenght of a Slice (P04).
func Length(s Slice) int {
	return len(s)
}

// Reverse reverses a given Slice (P05).
func Reverse(s Slice) Slice {
	length := len(s)
	for i := 0; i < length/2; i++ {
		s[i], s[length-i-1] = s[length-i-1], s[i]
	}
	return s
}

// IsPalindrome returns true if a given Slice is palindrome (P06).
func IsPalindrome(s Slice) bool {
	length := len(s)
	for i := 0; i < length/2; i++ {
		if s[i] != s[length-i-1] {
			return false
		}
	}
	return true
}

// Flatten flattens a nested ISlice structure (P07).
func Flatten(s ISlice) Slice {
	var result Slice
	for _, elem := range s {
		switch x := elem.(type) {
		case string:
			result = append(result, x)
		case ISlice:
			result = append(result, Flatten(x)...)
		}
	}
	return result
}

// Compress removes consecutive duplicates of a Slice (P08).
func Compress(s Slice) Slice {
	if len(s) < 1 {
		return s
	}
	result := Slice{s[0]}
	for _, elem := range s {
		if result[len(result)-1] == elem {
			continue
		}
		result = append(result, elem)
	}
	return result
}

// Pack packs consecutive elements and returns a Slice of Slice (P09).
func Pack(s Slice) []Slice {
	var result []Slice
	if len(s) == 0 {
		return []Slice{}
	}
	sublist := Slice{s[0]}
	for _, elem := range s[1:] {
		if sublist[len(sublist)-1] != elem {
			result = append(result, sublist)
			sublist = append(Slice{}, elem)
		} else {
			sublist = append(sublist, elem)
		}
	}
	result = append(result, sublist)
	return result
}

// Encode returns a length-encoded Slice (P10).
func Encode(s Slice) ISlice {
	result := ISlice{}
	packedSlice := Pack(s)
	for _, elem := range packedSlice {
		result = append(result, LengthEncodedPair{len(elem), elem[0]})
	}
	return result
}

// EncodeModified returns a modified length encoding of a Slice (P11).
func EncodeModified(s Slice) ISlice {
	result := ISlice{}
	packedSlice := Pack(s)
	for _, elem := range packedSlice {
		if len(elem) == 1 {
			result = append(result, elem[0])
		} else {
			result = append(result, LengthEncodedPair{len(elem), elem[0]})
		}
	}
	return result
}

// Decode decodes a length-encoded Slice (P12).
func Decode(encoded ISlice) Slice {
	decoded := Slice{}
	for _, elem := range encoded {
		switch x := elem.(type) {
		case string:
			decoded = append(decoded, x)
		case LengthEncodedPair:
			for i := 0; i < x.length; i++ {
				decoded = append(decoded, x.str)
			}
		}
	}
	return decoded
}

// EncodeDirect offers an alternative solution to Encode (P13).
func EncodeDirect(s Slice) ISlice {
	if len(s) == 0 {
		return ISlice{}
	} else if len(s) == 1 {
		return ISlice{s[0]}
	}

	encoded, current, count := ISlice{}, s[0], 1
	for _, elem := range s[1:] {
		if current != elem {
			if count == 1 {
				encoded = append(encoded, current)
			} else {
				encoded = append(encoded, LengthEncodedPair{count, current})
			}
			current, count = elem, 1
		} else {
			count += 1
		}
	}
	if count == 1 {
		encoded = append(encoded, current)
	} else {
		encoded = append(encoded, LengthEncodedPair{count, current})
	}
	return encoded
}

// Duplicate doubles the elements of the list (P14).
func Duplicate(s Slice) Slice {
	duplicated := Slice{}
	for _, elem := range s {
		duplicated = append(duplicated, elem, elem)
	}
	return duplicated
}

// DuplicateTimes duplicates the elements of the list a given number of times (P15).
func DuplicateTimes(s Slice, times int) Slice {
	if times == 1 {
		return s
	}

	duplicated := Slice{}
	for _, elem := range s {
		for i := 0; i < times; i++ {
			duplicated = append(duplicated, elem)
		}
	}
	return duplicated
}

// Drop removes every N'th element of a list (P16).
func Drop(s Slice, period int) (Slice, error) {
	if period > len(s) || period < 1 {
		return nil, errors.New("The value of `period` is not valid.")
	}
	if period == 1 {
		return Slice{}, nil
	}
	result := Slice{}
	for i := 0; i < len(s); i++ {
		if (i+1)%period != 0 {
			result = append(result, s[i])
		}
	}
	return result, nil
}

// Split splits a list in two parts according to the length of the first (P17).
func Split(s Slice, lengthOfFirst int) (Slice, Slice, error) {
	if lengthOfFirst > len(s) || lengthOfFirst < 0 {
		return nil, nil, errors.New("The length of the first list is not valid.")
	}
	return s[:lengthOfFirst], s[lengthOfFirst:], nil
}

// SliceList returns a Slice from a list (P18).
func SliceList(s Slice, start int, end int) (Slice, error) {
	if start < 1 || len(s) < start {
		return nil, errors.New("The value of `start` is not valid.")
	}
	if end < start || len(s) < end {
		return nil, errors.New("The value of `end` is not valid.")
	}
	return s[start-1 : end], nil
}

// Rotate rotates a list N places to the left (P19).
func Rotate(s Slice, places int) Slice {
	places = places % len(s)
	if places < 0 {
		places = len(s) + places
	}
	rotated := s[places:]
	rotated = append(rotated, s[:places]...)
	return rotated
}

// RemoveAt removes the K'th element of a list (P20).
func RemoveAt(s Slice, index int) (Slice, error) {
	if index < 0 || len(s) < index {
		return nil, errors.New("The `index` argument is not valid.")
	}
	return append(s[:index-1], s[index:]...), nil
}

// InsertAt inserts an element at a given position (P21).
func InsertAt(s Slice, position int, element string) (Slice, error) {
	if position < 0 || len(s)+1 < position {
		return nil, errors.New("The `position` argument is not valid.")
	}
	if position == len(s)+1 {
		return append(s, element), nil
	}
	s = append(s[:position], s[position-1:]...)
	s[position-1] = element
	return s, nil
}

// Range returns a list of integers from start to end (P22).
func Range(start int, end int) ([]int, error) {
	if end < start {
		return nil, errors.New("The given arguments are invalid.")
	}
	rangeList := []int{}
	for i := start; i <= end; i++ {
		rangeList = append(rangeList, i)
	}
	return rangeList, nil
}

// RandomSelect picks N random elements from a List (P23).
func RandomSelect(s []int, samples int) ([]int, error) {
	if samples < 0 || len(s) < samples {
		return nil, errors.New("The requested number of samples is invalid.")
	}
	rand.Seed(time.Now().UnixNano())
	randomlySelected := []int{}
	for i := 0; i < samples; i++ {
		randomlySelected = append(randomlySelected, s[rand.Intn(len(s))])
	}
	return randomlySelected, nil
}

// Lotto randomly picks N integers from Range 1 to M (P24).
func Lotto(n int, m int) ([]int, error) {
	if n < 0 || m < 1 {
		return nil, errors.New("The given values are invalid.")
	}
	if m < n {
		return nil, errors.New("The value of numbers to draw cannot be greater than the range.")
	}
	rangeList, _ := Range(1, m)
	return RandomSelect(rangeList, n)
}

// RandomPermutation generates a random permutation of a list (P25).
func RandomPermutation(s []int) ([]int, error) {
	return RandomSelect(s, len(s))
}

// Combination returns the combinations of K distinct elements of a list (P26).
func Combination(s Slice, k int) <-chan Slice {
	channel := make(chan Slice)
	go func() {
		defer close(channel)
		if k <= 0 {
			channel <- Slice{}
			return
		}
		thisone := Slice{}
		for i := 0; i < len(s); i++ {
			thisone = Slice{s[i]}
			for another := range Combination(s[i+1:], k-1) {
				channel <- append(thisone, another...)
			}
		}
	}()
	return channel
}

// LengthSort sorts a List according to the length of its sublists (P28a)
func LengthSort(s []Slice) []Slice {
	sort.Sort(ByLength(s))
	return s
}

// LengthFrequencySort sorts a List accoring to sublist length frequency (P28b)
func LengthFrequencySort(s []Slice) []Slice {
	// Group sublists according to length in a map
	listLenMap := make(map[int][]Slice)
	for _, elem := range s {
		if value, ok := listLenMap[len(elem)]; ok {
			listLenMap[len(elem)] = append(value, elem)
		} else {
			listLenMap[len(elem)] = []Slice{elem}
		}
	}
	// Keep only grouped sublists
	groupedSublists := [][]Slice{}
	for _, sublists := range listLenMap {
		groupedSublists = append(groupedSublists, sublists)
	}
	sort.Sort(ByLength2(groupedSublists))
	// Form output slice
	sorted := []Slice{}
	for _, sublist := range groupedSublists {
		sorted = append(sorted, sublist...)
	}
	return sorted
}
