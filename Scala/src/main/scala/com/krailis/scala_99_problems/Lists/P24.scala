package com.krailis.scala_99_problems.Lists

import P22.range

import scala.annotation.tailrec
import scala.util.Random

object P24 {
  def lotto(N: Int, M: Int): List[Int] = {

    val rangeList: List[Int] = range(1, M)
    val random = new Random()

    @tailrec
    def doLotto(n: Int, ls: List[Int]): List[Int] = (n, ls) match {
      case (0, acc) => acc
      case (n, acc) => doLotto(n-1, acc :+ rangeList(random.nextInt(M - 1)))
    }

    doLotto(N, Nil)
  }
}
