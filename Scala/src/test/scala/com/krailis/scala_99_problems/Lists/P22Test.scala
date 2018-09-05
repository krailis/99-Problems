package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P22Test extends FunSuite {

  test("From 4 to 9") {
    assert(P22.range(4, 9) === List(4, 5, 6, 7, 8, 9))
  }

}
