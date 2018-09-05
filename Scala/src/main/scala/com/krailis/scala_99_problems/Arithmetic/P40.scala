package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P31.IntIsPrime

object P40 {

  implicit class IntGoldbach(n: Int) {
    def goldbach: (Int, Int) = {
      val primeList = P39.listPrimesinRange(3, (n / 2).toInt)
      for (prime <- primeList) if ((n - prime).isPrime) return (prime, n - prime)
      (-1, -1)
    }
  }

}