package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P07Test extends FunSuite {

  test("Empty List") {
    assert(P07.flatten(List()) === List())
  }

  test("Flat List") {
    assert(P07.flatten(List(1, 2, 3, 4, 5)) === List(1, 2, 3, 4, 5))
  }

  test("Nested List") {
    assert(P07.flatten(List(List(1, 1), 2, List(3, List(5, 8)))) === List(1, 1, 2, 3, 5, 8))
  }

}
