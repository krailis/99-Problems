package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P40.IntGoldbach

object P41 {
  def printGoldbachList(a: Int, b: Int): Unit = {
    var start = a
    if (a % 2 == 1) start += 1
    for (i <- start until b + 1 by 2) {
      val primes = i.goldbach
      println(i.toString + " = " + primes._1.toString + " + " + primes._2.toString)
    }
  }
}
