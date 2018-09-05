package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P05Test extends FunSuite {

  val p05 = new P05[Any]()

  test("Empty List") {
    assert(p05.reverse(List()) === List())
  }

  test("Single-Element List") {
    assert(p05.reverse(List(1)) === List(1))
  }

  test("Multiple-Element List") {
    assert(p05.reverse(List(1, 2, 3, 4, 5, 6, 7)) == List(7, 6, 5, 4, 3, 2, 1))
  }
}
