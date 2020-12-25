package lists

import (
  "fmt"
  "reflect"
  "testing"
)

func TestLastElement(t *testing.T) {
  var testCases = []struct {
    x Slice
    y string
  }{
    {Slice{"a", "b", "c", "d", "e"}, "e"},
    {Slice{"a", "b", "c", "d"}, "d"},
    {Slice{"a", "b", "c"}, "c"},
    {Slice{"a", "b"}, "b"},
    {Slice{"a"}, "a"},
    {Slice{}, ""},
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans, _ := LastElement(testCase.x)
      if ans != testCase.y {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestLastButOneElement(t *testing.T) {
  var testCases = []struct {
    x Slice
    y string
  }{
    {Slice{"a", "b", "c", "d", "e"}, "d"},
    {Slice{"a", "b", "c", "d"}, "c"},
    {Slice{"a", "b", "c"}, "b"},
    {Slice{"a", "b"}, "a"},
    {Slice{"a"}, ""},
    {Slice{}, ""},
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans, _ := LastButOneElement(testCase.x)
      if ans != testCase.y {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestKthElement(t *testing.T) {
  var testCases = []struct {
    x Slice
    k int
    y string
  }{
    {Slice{"a", "b", "c", "d", "e"}, 4, "d"},
    {Slice{"a", "b", "c", "d", "e"}, 1, "a"},
    {Slice{"a", "b", "c", "d", "e"}, 3, "c"},
    {Slice{"a", "b", "c", "d", "e"}, 2, "b"},
    {Slice{"a", "b", "c", "d", "e"}, 5, "e"},
    {Slice{"a", "b", "c", "d", "e"}, 6, ""},
  }

  for _, testCase := range testCases {
    testName := fmt.Sprintf("%v,%d", testCase.x, testCase.k)
    t.Run(testName, func(t *testing.T) {
      ans, _ := KthElement(testCase.x, testCase.k)
      if ans != testCase.y {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestLength(t *testing.T) {
  var testCases = []struct {
    x Slice
    y int
  }{
    {Slice{"a", "b", "c", "d", "e", "f", "g"}, 7},
    {Slice{"a", "b", "c", "d", "e", "f"}, 6},
    {Slice{"a", "b", "c", "d", "e"}, 5},
    {Slice{"a", "b", "c", "d"}, 4},
    {Slice{"a", "b", "c"}, 3},
    {Slice{"a", "b"}, 2},
    {Slice{"a"}, 1},
    {Slice{}, 0},
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := Length(testCase.x)
      if ans != testCase.y {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestReverse(t *testing.T) {
  var testCases = []struct {
    x Slice
    y Slice
  }{
    {
      Slice{"a", "b", "c", "d", "e", "f", "g"},
      Slice{"g", "f", "e", "d", "c", "b", "a"},
    },
    {
      Slice{"a", "b", "c", "d", "e", "f"},
      Slice{"f", "e", "d", "c", "b", "a"},
    },
    {
      Slice{"a", "b", "c", "d", "e"},
      Slice{"e", "d", "c", "b", "a"},
    },
    {
      Slice{"a", "b", "c", "d"},
      Slice{"d", "c", "b", "a"},
    },
    {
      Slice{"a", "b", "c"},
      Slice{"c", "b", "a"},
    },
    {
      Slice{"a", "b"},
      Slice{"b", "a"},
    },
    {
      Slice{"a"},
      Slice{"a"},
    },
    {
      Slice{},
      Slice{},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := Reverse(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestIsPalindrome(t *testing.T) {
  var testCases = []struct {
    x Slice
    y bool
  }{
    {Slice{"a", "b", "c", "d", "c", "b", "a"}, true},
    {Slice{"a", "b", "c", "d", "a", "b", "a"}, false},
    {Slice{"a", "b", "c", "c", "b", "a"}, true},
    {Slice{"a", "b", "c", "c", "b", "o"}, false},
    {Slice{"a", "b", "c", "b", "a"}, true},
    {Slice{"a", "i", "c", "b", "a"}, false},
    {Slice{"a", "b", "b", "a"}, true},
    {Slice{"e", "b", "e", "a"}, false},
    {Slice{"a", "b", "a"}, true},
    {Slice{"a", "b", "c"}, false},
    {Slice{"a", "a"}, true},
    {Slice{"a", "b"}, false},
    {Slice{"a"}, true},
    {Slice{}, true},
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := IsPalindrome(testCase.x)
      if ans != testCase.y {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestFlatten(t *testing.T) {
  var testCases = []struct {
    x ISlice
    y Slice
  }{
    {
      ISlice{"a", ISlice{ISlice{"b", "c"}, ISlice{"d", "e"}}, "f"},
      Slice{"a", "b", "c", "d", "e", "f"},
    },
    {
      ISlice{"a", ISlice{"b", ISlice{"c"}, "d"}, "e"},
      Slice{"a", "b", "c", "d", "e"},
    },
    {
      ISlice{ISlice{ISlice{"a", "b"}, "c"}, "d"},
      Slice{"a", "b", "c", "d"},
    },
    {
      ISlice{"a", ISlice{"b"}, "c"},
      Slice{"a", "b", "c"},
    },
    {
      ISlice{"a", ISlice{"b"}},
      Slice{"a", "b"},
    },
    {
      ISlice{ISlice{ISlice{"a", ISlice{"b"}}}},
      Slice{"a", "b"},
    },
    {
      ISlice{"a"},
      Slice{"a"},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := Flatten(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestCompress(t *testing.T) {
  var testCases = []struct {
    x Slice
    y Slice
  }{
    {
      Slice{"a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e"},
      Slice{"a", "b", "c", "a", "d", "e"},
    },
    {
      Slice{"a", "b", "b", "c", "b", "b", "d", "e", "e", "f", "f", "f", "f"},
      Slice{"a", "b", "c", "b", "d", "e", "f"},
    },
    {
      Slice{"a", "b", "a", "a", "b", "c", "c", "d", "c", "d", "d", "d", "e"},
      Slice{"a", "b", "a", "b", "c", "d", "c", "d", "e"},
    },
    {
      Slice{"a", "a", "b", "c", "d", "e", "f", "a", "a", "a", "b", "c", "c"},
      Slice{"a", "b", "c", "d", "e", "f", "a", "b", "c"},
    },
    {
      Slice{"a", "b", "b"},
      Slice{"a", "b"}},
    {
      Slice{"a", "a"},
      Slice{"a"}},
    {
      Slice{},
      Slice{},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := Compress(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestPack(t *testing.T) {
  var testCases = []struct {
    x Slice
    y []Slice
  }{
    {
      Slice{"a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e"},
      []Slice{
        Slice{"a", "a", "a", "a"}, Slice{"b"}, Slice{"c", "c"},
        Slice{"a", "a"}, Slice{"d"}, Slice{"e", "e", "e"}},
    },
    {
      Slice{"a", "b", "b", "c", "b", "b", "d", "e", "e", "f", "f", "f", "f"},
      []Slice{
        Slice{"a"}, Slice{"b", "b"}, Slice{"c"}, Slice{"b", "b"},
        Slice{"d"}, Slice{"e", "e"}, Slice{"f", "f", "f", "f"}},
    },
    {
      Slice{"a", "b", "a", "a", "b", "c", "c", "d", "c", "d", "d", "d", "e"},
      []Slice{
        Slice{"a"}, Slice{"b"}, Slice{"a", "a"}, Slice{"b"}, Slice{"c", "c"},
        Slice{"d"}, Slice{"c"}, Slice{"d", "d", "d"}, Slice{"e"}},
    },
    {
      Slice{"a", "a", "b", "c", "d", "e", "f", "a", "a", "a", "b", "c", "c"},
      []Slice{
        Slice{"a", "a"}, Slice{"b"}, Slice{"c"}, Slice{"d"}, Slice{"e"},
        Slice{"f"}, Slice{"a", "a", "a"}, Slice{"b"}, Slice{"c", "c"}},
    },
    {
      Slice{"a", "b", "b"},
      []Slice{Slice{"a"}, Slice{"b", "b"}},
    },
    {
      Slice{"a", "a"},
      []Slice{Slice{"a", "a"}},
    },
    {
      Slice{},
      []Slice{},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := Pack(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestEncode(t *testing.T) {
  var testCases = []struct {
    x Slice
    y ISlice
  }{
    {
      Slice{"a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e"},
      ISlice{
        LengthEncodedPair{4, "a"}, LengthEncodedPair{1, "b"}, LengthEncodedPair{2, "c"},
        LengthEncodedPair{2, "a"}, LengthEncodedPair{1, "d"}, LengthEncodedPair{3, "e"}},
    },
    {
      Slice{"a", "b", "b", "c", "b", "b", "d", "e", "e", "f", "f", "f", "f"},
      ISlice{
        LengthEncodedPair{1, "a"}, LengthEncodedPair{2, "b"}, LengthEncodedPair{1, "c"},
        LengthEncodedPair{2, "b"}, LengthEncodedPair{1, "d"}, LengthEncodedPair{2, "e"},
        LengthEncodedPair{4, "f"}},
    },
    {
      Slice{"a", "b", "a", "a", "b", "c", "c", "d", "c", "d", "d", "d", "e"},
      ISlice{
        LengthEncodedPair{1, "a"}, LengthEncodedPair{1, "b"}, LengthEncodedPair{2, "a"},
        LengthEncodedPair{1, "b"}, LengthEncodedPair{2, "c"}, LengthEncodedPair{1, "d"},
        LengthEncodedPair{1, "c"}, LengthEncodedPair{3, "d"}, LengthEncodedPair{1, "e"}},
    },
    {
      Slice{"a", "a", "b", "c", "d", "e", "f", "a", "a", "a", "b", "c", "c"},
      ISlice{
        LengthEncodedPair{2, "a"}, LengthEncodedPair{1, "b"}, LengthEncodedPair{1, "c"},
        LengthEncodedPair{1, "d"}, LengthEncodedPair{1, "e"}, LengthEncodedPair{1, "f"},
        LengthEncodedPair{3, "a"}, LengthEncodedPair{1, "b"}, LengthEncodedPair{2, "c"}},
    },
    {
      Slice{"a", "b", "b"},
      ISlice{LengthEncodedPair{1, "a"}, LengthEncodedPair{2, "b"}},
    },
    {
      Slice{"a", "a"},
      ISlice{LengthEncodedPair{2, "a"}},
    },
    {
      Slice{},
      ISlice{},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := Encode(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestEncodeModified(t *testing.T) {
  var testCases = []struct {
    x Slice
    y ISlice
  }{
    {
      Slice{"a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e"},
      ISlice{
        LengthEncodedPair{4, "a"}, "b", LengthEncodedPair{2, "c"},
        LengthEncodedPair{2, "a"}, "d", LengthEncodedPair{3, "e"}},
    },
    {
      Slice{"a", "b", "b", "c", "b", "b", "d", "e", "e", "f", "f", "f", "f"},
      ISlice{
        "a", LengthEncodedPair{2, "b"}, "c", LengthEncodedPair{2, "b"}, "d",
        LengthEncodedPair{2, "e"}, LengthEncodedPair{4, "f"}},
    },
    {
      Slice{"a", "b", "a", "a", "b", "c", "c", "d", "c", "d", "d", "d", "e"},
      ISlice{
        "a", "b", LengthEncodedPair{2, "a"}, "b", LengthEncodedPair{2, "c"},
        "d", "c", LengthEncodedPair{3, "d"}, "e"},
    },
    {
      Slice{"a", "a", "b", "c", "d", "e", "f", "a", "a", "a", "b", "c", "c"},
      ISlice{
        LengthEncodedPair{2, "a"}, "b", "c", "d", "e", "f",
        LengthEncodedPair{3, "a"}, "b", LengthEncodedPair{2, "c"}},
    },
    {
      Slice{"a", "b", "b"},
      ISlice{"a", LengthEncodedPair{2, "b"}},
    },
    {
      Slice{"a", "a"},
      ISlice{LengthEncodedPair{2, "a"}},
    },
    {
      Slice{},
      ISlice{},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := EncodeModified(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestDecode(t *testing.T) {
  var testCases = []struct {
    x ISlice
    y Slice
  }{
    {
      ISlice{
        LengthEncodedPair{4, "a"}, "b", LengthEncodedPair{2, "c"},
        LengthEncodedPair{2, "a"}, "d", LengthEncodedPair{3, "e"}},
      Slice{"a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e"},
    },
    {
      ISlice{
        "a", LengthEncodedPair{2, "b"}, "c", LengthEncodedPair{2, "b"}, "d",
        LengthEncodedPair{2, "e"}, LengthEncodedPair{4, "f"}},
      Slice{"a", "b", "b", "c", "b", "b", "d", "e", "e", "f", "f", "f", "f"},
    },
    {
      ISlice{
        "a", "b", LengthEncodedPair{2, "a"}, "b", LengthEncodedPair{2, "c"},
        "d", "c", LengthEncodedPair{3, "d"}, "e"},
      Slice{"a", "b", "a", "a", "b", "c", "c", "d", "c", "d", "d", "d", "e"},
    },
    {
      ISlice{
        LengthEncodedPair{2, "a"}, "b", "c", "d", "e", "f",
        LengthEncodedPair{3, "a"}, "b", LengthEncodedPair{2, "c"}},
      Slice{"a", "a", "b", "c", "d", "e", "f", "a", "a", "a", "b", "c", "c"},
    },
    {
      ISlice{"a", LengthEncodedPair{2, "b"}},
      Slice{"a", "b", "b"},
    },
    {
      ISlice{LengthEncodedPair{2, "a"}},
      Slice{"a", "a"},
    },
    {
      ISlice{},
      Slice{},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := Decode(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestEncodeDirect(t *testing.T) {
  var testCases = []struct {
    x Slice
    y ISlice
  }{
    {
      Slice{"a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e"},
      ISlice{
        LengthEncodedPair{4, "a"}, "b", LengthEncodedPair{2, "c"},
        LengthEncodedPair{2, "a"}, "d", LengthEncodedPair{3, "e"}},
    },
    {
      Slice{"a", "b", "b", "c", "b", "b", "d", "e", "e", "f", "f", "f", "f"},
      ISlice{
        "a", LengthEncodedPair{2, "b"}, "c", LengthEncodedPair{2, "b"}, "d",
        LengthEncodedPair{2, "e"}, LengthEncodedPair{4, "f"}},
    },
    {
      Slice{"a", "b", "a", "a", "b", "c", "c", "d", "c", "d", "d", "d", "e"},
      ISlice{
        "a", "b", LengthEncodedPair{2, "a"}, "b", LengthEncodedPair{2, "c"},
        "d", "c", LengthEncodedPair{3, "d"}, "e"},
    },
    {
      Slice{"a", "a", "b", "c", "d", "e", "f", "a", "a", "a", "b", "c", "c"},
      ISlice{
        LengthEncodedPair{2, "a"}, "b", "c", "d", "e", "f",
        LengthEncodedPair{3, "a"}, "b", LengthEncodedPair{2, "c"}},
    },
    {
      Slice{"a", "b", "b"},
      ISlice{"a", LengthEncodedPair{2, "b"}},
    },
    {
      Slice{"a", "a"},
      ISlice{LengthEncodedPair{2, "a"}},
    },
    {
      Slice{},
      ISlice{},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := EncodeDirect(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestDuplicate(t *testing.T) {
  var testCases = []struct {
    x Slice
    y Slice
  }{
    {
      Slice{"a", "b", "c", "a", "d", "e"},
      Slice{"a", "a", "b", "b",  "c", "c", "a", "a", "d", "d", "e", "e"},
    },
    {
      Slice{"a", "b", "c", "b", "d", "e", "f"},
      Slice{"a", "a", "b", "b", "c", "c", "b", "b", "d", "d", "e", "e", "f", "f"},
    },
    {
      Slice{"a", "b", "a", "b", "c", "d", "c"},
      Slice{"a", "a", "b", "b", "a", "a", "b", "b", "c", "c", "d", "d", "c", "c"},
    },
    {
      Slice{"a", "b", "b"},
      Slice{"a", "a", "b", "b", "b", "b"},
    },
    {
      Slice{"a"},
      Slice{"a", "a"},
    },
    {
      Slice{},
      Slice{},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x)
    t.Run(testName, func(t *testing.T) {
      ans := Duplicate(testCase.x)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}

func TestDuplicateTimes(t *testing.T) {
  var testCases = []struct {
    x Slice
    times int
    y Slice
  }{
    {
      Slice{"a", "b", "c", "a", "d", "e"}, 1,
      Slice{"a", "b", "c", "a", "d", "e"},
    },
    {
      Slice{"a", "b", "c", "b", "d", "e", "f"}, 2,
      Slice{"a", "a", "b", "b", "c", "c", "b", "b", "d", "d", "e", "e", "f", "f"},
    },
    {
      Slice{"a", "b", "a", "b", "c", "d", "c"}, 3,
      Slice{
        "a", "a", "a", "b", "b", "b", "a", "a", "a", "b", "b", "b",
        "c", "c", "c", "d", "d", "d", "c", "c", "c"},
    },
    {
      Slice{"a", "b", "b"}, 4,
      Slice{"a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b"}},
    {
      Slice{"a"}, 2,
      Slice{"a", "a"},
    },
    {
      Slice{}, 3,
      Slice{},
    },
  }

  for _, testCase := range testCases {
    testName := fmt.Sprint(testCase.x, testCase.times)
    t.Run(testName, func(t *testing.T) {
      ans := DuplicateTimes(testCase.x, testCase.times)
      if !(reflect.DeepEqual(ans, testCase.y)) {
        t.Errorf("Expected %v but the result was %v", testCase.y, ans)
      }
    })
  }
}
