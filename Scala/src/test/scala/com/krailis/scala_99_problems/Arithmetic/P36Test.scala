package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P36.IntPrimeFactorsMultiplicity
import org.scalatest.FunSuite

class P36Test extends FunSuite {

  test("315") {
    assert(315.primeFactorsMultiplicity === List((3, 2), (5, 1), (7, 1)))
  }

  test("294") {
    assert(294.primeFactorsMultiplicity === List((2, 1), (3, 1), (7, 2)))
  }

  test("Prime: 211") {
    assert(211.primeFactorsMultiplicity === List((211, 1)))
  }

  test("272") {
    assert(272.primeFactorsMultiplicity === List((2, 4), (17, 1)))
  }
}
