package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P35.IntPrimeFactors
import org.scalatest.FunSuite

class P35Test extends FunSuite {

  test("315") {
    assert(315.primeFactors === List(3, 3, 5, 7))
  }

  test("294") {
    assert(294.primeFactors === List(2, 3, 7, 7))
  }

  test("Prime: 211") {
    assert(211.primeFactors === List(211))
  }

  test("272") {
    assert(272.primeFactors === List(2, 2, 2, 2, 17))
  }
}
