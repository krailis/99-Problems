package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P15Test extends FunSuite {

  val p15 = new P15[Any]()

  test("List with Multiple Elements") {
    assert(p15.duplicateNTimes(3, List('a, 'b, 'c, 'c, 'd)) ===
      List('a, 'a, 'a, 'b, 'b, 'b, 'c, 'c, 'c, 'c, 'c, 'c, 'd, 'd, 'd))
  }
}
