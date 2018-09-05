package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P37.IntTotientAlternative
import org.scalatest.FunSuite

class P37Test extends FunSuite {

  test("Fifty seven") {
    assert(57.totient2 === 36)
  }

  test("Two hundred nine") {
    assert(209.totient2 === 180)
  }

  test("Two hundred eleven") {
    assert(211.totient2 === 210)
  }

  test("Five hundred") {
    assert(500.totient2 === 200)
  }
}
