package com.krailis.scala_99_problems.Arithmetic

import scala.collection.mutable
import scala.math.sqrt

object P39 {
  def listPrimesinRange(lower: Int, upper: Int): List[Int] = {
    var a = mutable.Buffer.fill(upper+1)(true)
    for (i <- 2 until sqrt(upper).toInt + 1) {
      if (a(i)) {
        var j = i * i
        while (j <= upper) {
          a(j) = false
          j += i
        }
      }
    }
    (for (i <- lower until upper + 1 if a(i)) yield i).toList
  }
}
