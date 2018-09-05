package com.krailis.scala_99_problems.Arithmetic

object P32 {
  def gcd(a: Int, b: Int): Int = (a, b) match {
    case (x, 0) => x
    case (x, y) => gcd(y, x % y)
  }
}
