package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P08[A] {
  def eliminateDuplicates(list: List[A]): List[A] = {

    @tailrec
    def doEliminate(list: List[A], acc: List[A]): List[A] = (list, acc) match {
      case (Nil, acc) => acc
      case (x1 :: x2 :: xs, acc) if x1 == x2 => doEliminate(x2 :: xs, acc)
      case (x :: xs, acc) => doEliminate(xs, acc :+ x)
    }

    doEliminate(list, Nil)
  }
}
