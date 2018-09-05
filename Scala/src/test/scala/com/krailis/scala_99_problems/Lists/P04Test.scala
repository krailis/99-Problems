package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P04Test extends FunSuite {

  val p04 = new P04[Any]()

  test("Empty List") {
    assert(p04.length(List()) === 0)
  }

  test("Single-Element List") {
    assert(p04.length(List(1)) === 1)
  }

  test("Multiple element list") {
    assert(p04.length(List(1, 3, 4, 6, 9, 14)) === 6)
  }
}
