package com.krailis.scala_99_problems.Arithmetic


object P31 {

  implicit class IntIsPrime(n: Int) {
    def isPrime: Boolean = {
      for (i <- 2 until n-1)
        if (n % i == 0) return false
      true
    }
  }

}
