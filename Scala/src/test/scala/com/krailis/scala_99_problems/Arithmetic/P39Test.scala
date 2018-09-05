package com.krailis.scala_99_problems.Arithmetic

import org.scalatest.FunSuite

class P39Test extends FunSuite {

  test("7 to 31") {
    assert(P39.listPrimesinRange(7, 31) ===
      List(7, 11, 13, 17, 19, 23, 29, 31))
  }

  test("670 to 740") {
    assert(P39.listPrimesinRange(670, 740) ===
      List(673, 677, 683, 691, 701, 709, 719, 727, 733, 739))
  }


}
