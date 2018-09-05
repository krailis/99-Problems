package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P01Test extends FunSuite {

  val p01 = new P01[Any]()

  test("Empty Input List") {
    assert(p01.last(List()) === None)
  }

  test("Single Element List") {
    assert(p01.last(List(0)) === Some(0))
  }

  test("Multiple Element List") {
    assert(p01.last(List(1, 6, "a", 5, 7, "b")) === Some("b"))
  }
}
