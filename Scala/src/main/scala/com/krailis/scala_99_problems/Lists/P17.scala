package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P17[A] {
  def split(num: Int, list: List[A]): (List[A], List[A]) = {

    @tailrec
    def doSplit(n: Int, list: List[A], acc: List[A]): (List[A], List[A]) = (n, list, acc) match {
      case (0, ls, acc) => (acc, ls)
      case (_, Nil, acc) => (acc, Nil)
      case (n, x :: xs, acc) => doSplit(n - 1, xs, acc :+ x)
    }

    doSplit(num, list, Nil)
  }
}
