package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P31.IntIsPrime
import org.scalatest.FunSuite

class P31Test extends FunSuite {

  test("Small Prime") {
    assert(7.isPrime === true)
  }

  test("Small not-prime") {
    assert(9.isPrime === false)
  }

  test("Large Prime") {
    assert(923371.isPrime === true)
  }

  test("Large not-Prime") {
    assert(923372.isPrime === false)
  }
}
