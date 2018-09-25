package com.krailis.scala_99_problems.Logic_and_Codes

import org.scalatest.FunSuite

class P50Test extends FunSuite {

  test("n = 1") {
    assert(P50.grayCode(1) === List("0", "1"))
  }

  test("n = 2") {
    assert(P50.grayCode(2) === List("00", "01", "11", "10"))
  }

  test("n = 3") {
    assert(P50.grayCode(3) === List("000", "001", "011", "010", "110", "111", "101", "100"))
  }
}
