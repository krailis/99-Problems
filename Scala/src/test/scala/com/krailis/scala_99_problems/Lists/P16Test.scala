package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P16Test extends FunSuite {

  val p16 = new P16[Any]()

  test("Empty List") {
    assert(p16.drop(3, List()) === List())
  }

  test("Less than N Elements") {
    assert(p16.drop(3, List('a, 'b)) === List('a, 'b))
  }

  test("List with Multiple Elements") {
    assert(p16.drop(3, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)) === List('a, 'b, 'd, 'e, 'g, 'h, 'j, 'k))
  }
}
