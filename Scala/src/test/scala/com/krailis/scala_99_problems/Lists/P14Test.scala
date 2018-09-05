package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P14Test extends FunSuite {

  val p14 = new P14[Any]()

  test("Empty List") {
    assert(p14.duplicateElements(List()) === List())
  }

  test("Normal List with Multiple Elements") {
    assert(p14.duplicateElements(List('a, 'b, 'c, 'c, 'd)) === List('a, 'a, 'b, 'b, 'c, 'c, 'c, 'c, 'd, 'd))
  }

}
