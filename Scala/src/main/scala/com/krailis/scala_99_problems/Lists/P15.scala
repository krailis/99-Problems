package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P15[A] {
  def duplicateNTimes(n: Int, list: List[A]): List[A] = {

    @tailrec
    def doDuplicate(list: List[A], acc: List[A]): List[A] = (list, acc) match {
      case (Nil, acc) => acc
      case (x :: xs, acc) => doDuplicate(xs, acc ++ List.fill(n)(x))
    }

    doDuplicate(list, Nil)
  }
}
