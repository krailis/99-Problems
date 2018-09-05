package com.krailis.scala_99_problems.Arithmetic

import scala.collection.mutable.ListBuffer


object P35 {

  implicit class IntPrimeFactors(n: Int) {
    def primeFactors: List[Int] = {
      var factorList = new ListBuffer[Int]()
      var value = n
      while (value % 2 == 0) {
        factorList += 2
        value /= 2
      }
      for (i <- 3 until Math.sqrt(value).toInt + 1 by 2) {
        while (value % i == 0) {
          factorList += i
          value /= i
        }
      }
      if (value > 2) factorList += value
      factorList.toList
    }
  }

}
