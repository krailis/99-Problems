package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P18Test extends FunSuite {

  val p18 = new P18[Any]()

  test("Less than K Elements") {
    assert(p18.slice(3, 5, List('a, 'b, 1, 2, 3)) === List(2, 3))
  }

  test("List with Multiple Elements") {
    assert(p18.slice(3, 7, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)) === List('d, 'e, 'f, 'g))
  }

}
