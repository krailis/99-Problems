package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P06Test extends FunSuite {

  val p06 = new P06[Any]()

  test("Empty List") {
    assert(p06.isPalindrome(List()) === true)
  }

  test("Single-Element List") {
    assert(p06.isPalindrome(List(1)) === true)
  }

  test("Multiple-Element Palindrome") {
    assert(p06.isPalindrome(List(1, 2, 3, 4, 3, 2, 1)) === true)
  }

  test("Multiple-Element Not Palindrome") {
    assert(p06.isPalindrome(List(1, 2, 3, 4, 3, 1)) === false)
  }
}
