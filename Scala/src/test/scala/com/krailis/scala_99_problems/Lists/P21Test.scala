package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P21Test extends FunSuite {

  val p21 = new P21[Any]()

  test("Bigger than Length") {
    assert(p21.insertAt('new, 20, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)) ===
      List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))
  }

  test("First Element") {
    assert(p21.insertAt('new, 0,  List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)) ===
      List('new, 'a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))
  }

  test("K'th Position") {
    assert(p21.insertAt('new, 1, List('a, 'b, 'c, 'd)) === List('a, 'new, 'b, 'c, 'd))
  }

}

