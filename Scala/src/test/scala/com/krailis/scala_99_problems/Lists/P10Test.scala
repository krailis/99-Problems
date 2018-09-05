package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P10Test extends FunSuite {

  val p10 = new P10[Any]()

  test("Empty List") {
    assert(p10.lengthEncoding(List()) === List())
  }

  test("Normal List With Duplicates") {
    assert(p10.lengthEncoding(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)) ===
      List((4,'a), (1,'b), (2,'c), (2,'a), (1,'d), (4,'e)))
  }

}
