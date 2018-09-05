package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P34.IntTotient
import com.krailis.scala_99_problems.Arithmetic.P37.IntTotientAlternative


object P38 {
  def time[R](block: => R): R = {
    val t0 = System.nanoTime()
    val result = block    // call-by-name
    val t1 = System.nanoTime()
    println("Elapsed time: " + (t1 - t0) + "ns")
    result
  }

  def compareTotient(): Unit = {
    println("=== P34 Totient Computation ===")
    println(time {10090.totient})
    println("=== P37 Totient Computation ===")
    println(time {10090.totient2})
  }

}
