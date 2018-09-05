package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P32.gcd

object P33 {

  implicit class IntIsCoprime(n: Int) {
    def isCoprimeTo(z: Int): Boolean = gcd(n, z) == 1
  }

}
