package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P14[A] {
  def duplicateElements(list: List[A]): List[A] = {

    @tailrec
    def doDuplicate(list: List[A], acc: List[A]): List[A] = (list, acc) match {
      case (Nil, acc) => acc
      case (x :: xs, acc) => doDuplicate(xs, acc ++ List(x, x))
    }

    doDuplicate(list, Nil)
  }
}
