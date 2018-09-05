package com.krailis.scala_99_problems.Arithmetic

import scala.collection.mutable.ListBuffer

object P36 {

  implicit class IntPrimeFactorsMultiplicity(n: Int) {
    def primeFactorsMultiplicity: List[(Int, Int)] = {
      var factorList = new ListBuffer[(Int, Int)]()
      var counter = 0
      var value = n
      while (value % 2 == 0) {
        counter += 1
        value /= 2
      }
      if (counter != 0) factorList :+= (2, counter)
      for (i <- 3 until Math.sqrt(value).toInt + 1 by 2) {
        counter = 0
        while (value % i == 0) {
          counter += 1
          value /= i
        }
        if (counter != 0) factorList :+= (i, counter)
      }
      if (value > 2) factorList :+= (value, 1)
      factorList.toList
    }
  }

}
