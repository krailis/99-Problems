// Package lists includes solutions to List Problems (1-28).
package lists

import (
  "errors"
  // "fmt"
)

type Slice []string
type ISlice []interface{}

// LastElement find The Last Element of a List (P01).
func LastElement(s Slice) (string, error) {
  length := len(s)
  if length < 1 {
    return "", errors.New("The given list is empty. Try again with a non-empty list.")
  }
  return s[length-1], nil
}

// LastButOneElement finds the Last but One Element of a List (P02).
func LastButOneElement(s Slice) (string, error) {
  length := len(s)
  if length < 2 {
    return "", errors.New("The given list has fewer elements than needed.")
  }
  return s[length-2], nil
}

// KthElement finds the k'th Element of a List (P03).
func KthElement(s Slice, k int) (string, error) {
  length := len(s)
  if length < k {
    return "", errors.New("The given list's length is smaller than the given k.")
  }
  return s[k - 1], nil
}

func Length(s Slice) int {
  return len(s)
}

func Reverse(s Slice) Slice {
  length := len(s)
  for i := 0; i < length / 2; i++ {
    s[i], s[length-i-1] = s[length-i-1], s[i]
  }
  return s
}

func IsPalindrome(s Slice) bool {
  length := len(s)
  for i := 0; i < length / 2; i++ {
      if s[i] != s[length-i-1] {
        return false
      }
  }
  return true
}

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

func Pack(s Slice) []Slice {
  var result []Slice
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

func Encode(s Slice) []interface{} {
  var result []interface{}
  packedSlice := Pack(s)
  for _, elem := range packedSlice {
    result = append(result, []interface{}{len(elem), elem[0]})
  }
  return result
}

func EncodeModified(s Slice) []interface{} {
  var result []interface{}
  packedSlice := Pack(s)
  for _, elem := range packedSlice {
    if len(elem) == 1 {
      result = append(result, elem[0])
    } else {
      result = append(result, []interface{}{len(elem), elem[0]})
    }
  }
  return result
}



// func main () {
//   fmt.Println(EncodeModified(Slice{"a", "a", "b", "c", "d", "e", "e", "f"}))
// }
