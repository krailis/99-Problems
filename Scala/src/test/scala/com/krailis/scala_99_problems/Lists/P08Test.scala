package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P08Test extends FunSuite {

  val p08 = new P08[Any]()

  test("Empty List") {
    assert(p08.eliminateDuplicates(List()) === List())
  }

  test("No duplicates") {
    assert(p08.eliminateDuplicates(List('a, 'b, 'c, 'd, 'e)) === List('a, 'b, 'c, 'd, 'e))
  }

  test("Nested List") {
    assert(p08.eliminateDuplicates(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)) === List('a, 'b, 'c, 'a, 'd, 'e))
  }

}
