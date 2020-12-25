// Package lists includes solutions to List Problems (1-28).
package lists

import "errors"

type Slice []string
type ISlice []interface{}
type LengthEncodedPair struct {
  length int
  str string
}

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
  return s[k - 1], nil
}

// Length finds the lenght of a Slice (P04).
func Length(s Slice) int {
  return len(s)
}

// Reverse reverses a given Slice (P05).
func Reverse(s Slice) Slice {
  length := len(s)
  for i := 0; i < length / 2; i++ {
    s[i], s[length-i-1] = s[length-i-1], s[i]
  }
  return s
}

// IsPalindrome returns true if a given Slice is palindrome (P06).
func IsPalindrome(s Slice) bool {
  length := len(s)
  for i := 0; i < length / 2; i++ {
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
  if len(s) == 0 {return []Slice{}}
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
