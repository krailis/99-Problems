package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P33.IntIsCoprime
import com.krailis.scala_99_problems.Arithmetic.P31.IntIsPrime

object P34 {

  implicit class IntTotient(n: Int) {
    def totient: Int = {
      if (n.isPrime) return n - 1
      var counter: Int = 1
      for (i <- 2 until n)
        if (n.isCoprimeTo(i)) counter += 1
      counter
    }
  }

}
