package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P17Test extends FunSuite {

  val p17 = new P17[Any]()

  test("Empty List") {
    assert(p17.split(3, List()) === (Nil, Nil))
  }

  test("Less than N Elements") {
    assert(p17.split(3, List('a, 'b)) === (List('a, 'b), Nil))
  }

  test("List with Multiple Elements") {
    assert(p17.split(3, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)) ===
      (List('a, 'b, 'c), List('d, 'e, 'f, 'g, 'h, 'i, 'j, 'k)))
  }
}
