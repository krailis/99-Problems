package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P40.IntGoldbach
import org.scalatest.FunSuite

class P40Test extends FunSuite {

  test("28") {
    assert(28.goldbach === (5, 23))
  }

  test("20") {
    assert(20.goldbach === (3, 17))
  }

  test("30") {
    assert(30.goldbach === (7, 23))
  }
}
