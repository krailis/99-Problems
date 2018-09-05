package com.krailis.scala_99_problems.Lists

import org.scalatest.FunSuite

class P09Test extends FunSuite {

  val p09 = new P09[Any]()

  test("Empty List") {
    assert(p09.packConsecutive(List()) === List())
  }

  test("No duplicates") {
    assert(p09.packConsecutive(List('a, 'b, 'c, 'd, 'e)) === List(List('a), List('b), List('c), List('d), List('e)))
  }

  test("With Duplicates") {
    assert(p09.packConsecutive(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)) ===
      List(List('a, 'a, 'a, 'a), List('b), List('c, 'c), List('a, 'a), List('d), List('e, 'e, 'e, 'e)))
  }

}
