package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P02Test extends FunSuite {

  val p02 = new P02[Any]()

  test("Empty Input List") {
    assert(p02.lastButOne(List()) === None)
  }

  test("Single Element List") {
    assert(p02.lastButOne(List(0)) === None)
  }

  test("Two-element List") {
    assert(p02.lastButOne(List(1, 2)) === Some(1))
  }

  test("Multiple Element List") {
    assert(p02.lastButOne(List(1, 6, "a", 5, 7, "b")) === Some(7))
  }
}
