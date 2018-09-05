package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P12Test extends FunSuite {

  val p12 = new P12[Any]()

  test("Empty List") {
    assert(p12.listDecoding(List()) === List())
  }

  test("Normal List") {
    assert(p12.listDecoding(List((4, 'a), (1, 'b), (2, 'c), (2, 'a), (1, 'd), (4, 'e))) ===
      List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e))
  }

}
