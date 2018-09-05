package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P20Test extends FunSuite {

  val p20 = new P20[Any]()

  test("Bigger than Length") {
    assert(p20.removeAt(20, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)) ===
      (List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k), None))
  }

  test("First Element") {
    assert(p20.removeAt(0, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)) ===
      (List('b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k), Some('a)))
  }

  test("K'th Element") {
    assert(p20.removeAt(2, List('a, 'b, 'c, 'd)) === (List('a, 'b, 'd), Some('c)))
  }

}

