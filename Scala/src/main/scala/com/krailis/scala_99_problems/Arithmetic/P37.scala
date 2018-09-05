package com.krailis.scala_99_problems.Arithmetic

import com.krailis.scala_99_problems.Arithmetic.P36.IntPrimeFactorsMultiplicity
import scala.annotation.tailrec
import scala.math.pow

object P37 {

  implicit class IntTotientAlternative(n: Int) {
    def totient2: Int = {
      @tailrec
      def computeTotient(x: Double, ps: List[(Int, Int)]): Int = (x, ps) match {
        case (phi, Nil) => phi.toInt
        case (phi, t :: ts) => computeTotient(phi*(t._1-1)*pow(t._1, t._2-1), ts)
      }
      computeTotient(1, n.primeFactorsMultiplicity)
    }
  }

}
