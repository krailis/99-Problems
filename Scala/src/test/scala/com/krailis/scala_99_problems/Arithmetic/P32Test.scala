package com.krailis.scala_99_problems.Arithmetic

import org.scalatest.FunSuite

class P32Test extends FunSuite {

  test("54 & 24") {
    assert(P32.gcd(54, 24) === 6)
  }

  test("78 & 104") {
    assert(P32.gcd(104, 78) === 26)
  }

  test("105 & 21") {
    assert(P32.gcd(105, 21) === 21)
  }

  test("GCD is One") {
    assert(P32.gcd(103, 23) === 1)
  }
}
