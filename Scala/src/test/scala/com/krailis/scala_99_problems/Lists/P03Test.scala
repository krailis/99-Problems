package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P03Test extends FunSuite {

  val p03 = new P03[Any]()

  test("Empty List") {
    assert(p03.nthElement(2, List()) === None)
  }

  test("Negative Index") {
    assert(p03.nthElement(-1, List(1, 3, 4, 6)) === None)
  }

  test("Index Greater than Length") {
    assert(p03.nthElement(7, List(1, 3, 4, 6)) === None)
  }

  test("Normal List with Multiple Elements") {
    assert(p03.nthElement(3, List(1, 3, 4, 6, 9, 14)) === Some(6))
  }
}
