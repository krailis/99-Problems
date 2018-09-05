package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

object P22 {
  def range(i: Int, j: Int): List[Int] = {

    @tailrec
    def doRange(k: Int, acc: List[Int]): List[Int] = (k, acc) match {
      case (k, acc) if k <= j => doRange(k + 1, acc :+ k)
      case (_, acc) => acc
    }

    doRange(i, Nil)
  }
}
