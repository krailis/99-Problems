package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P16[A] {
  def drop(num: Int, list: List[A]): List[A] = {

    @tailrec
    def doDrop(n: Int, list: List[A], acc: List[A]): List[A] = (n, list, acc) match {
      case (0, _ :: xs, acc) => doDrop(num - 1, xs, acc)
      case (_, Nil, acc) => acc
      case (n, x :: xs, acc) => doDrop(n - 1, xs, acc :+ x)
    }

    doDrop(num - 1, list, Nil)
  }
}
