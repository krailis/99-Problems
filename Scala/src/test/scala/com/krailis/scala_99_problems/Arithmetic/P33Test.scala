package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P33.IntIsCoprime
import org.scalatest.FunSuite

class P33Test extends FunSuite {

  test("Co-prime One") {
    assert(9.isCoprimeTo(4) === true)
  }

  test("Not Co-prime One") {
    assert(21.isCoprimeTo(9) === false)
  }

  test("Not Co-prime Two") {
    assert(49.isCoprimeTo(21) === false)
  }

  test("Co-prime Two") {
    assert(23.isCoprimeTo(7) === true)
  }
}
