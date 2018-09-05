package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P18[A] {
  def slice(i: Int, k: Int, list: List[A]): List[A] = {

    @tailrec
    def doSlice(j: Int, list: List[A], acc: List[A]): List[A] = (j, list, acc) match {
      case (j, _ :: xs, acc) if i > j => doSlice(j + 1, xs, acc)
      case (j, x :: xs, acc) if (j >= i && j < k) => doSlice(j + 1, xs, acc :+ x)
      case (_, Nil, acc) => acc
      case (_, _, acc) => acc
    }

    doSlice(0, list, Nil)
  }
}
