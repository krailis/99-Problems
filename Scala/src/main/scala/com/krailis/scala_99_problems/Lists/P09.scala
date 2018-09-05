package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P09[A] {
  def packConsecutive(list: List[A]): List[List[A]] = {

    @tailrec
    def doPack(list: List[A], n: Int, acc: List[Any]): List[List[A]] = (list, n, acc) match {
      case (Nil, _, acc) => acc.asInstanceOf[List[List[A]]]
      case (x1 :: x2 :: xs, n, acc) if x1 == x2 => doPack(x2 :: xs, n + 1, acc)
      case (x :: xs, n, acc) => doPack(xs, 0, acc :+ List.fill(n + 1)(x))
    }

    doPack(list, 0, Nil)
  }
}
