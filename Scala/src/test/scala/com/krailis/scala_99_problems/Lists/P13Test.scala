package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P13Test extends FunSuite {

  val p13 = new P13[Any]()

  test("Empty List") {
    assert(p13.directEncoding(List()) === List())
  }

  test("Normal List With Duplicates") {
    assert(p13.directEncoding(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)) ===
      List((4,'a), (1,'b), (2,'c), (2,'a), (1,'d), (4,'e)))
  }

}
