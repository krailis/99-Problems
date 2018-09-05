package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P11Test extends FunSuite {

  val p11 = new P11[Any]()

  test("Empty List") {
    assert(p11.modifiedEncoding(List()) === List())
  }

  test("Normal List With Duplicates") {
    assert(p11.modifiedEncoding(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)) ===
      List((4,'a), 'b, (2,'c), (2,'a), 'd, (4,'e)))
  }

}
