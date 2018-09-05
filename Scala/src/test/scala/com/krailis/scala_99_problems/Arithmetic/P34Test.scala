package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P34.IntTotient
import org.scalatest.FunSuite

class P34Test extends FunSuite {

  test("Fifty seven") {
    assert(57.totient === 36)
  }

  test("Two hundred nine") {
    assert(209.totient === 180)
  }

  test("Two hundred eleven") {
    assert(211.totient === 210)
  }

  test("Five hundred") {
    assert(500.totient === 200)
  }
}
