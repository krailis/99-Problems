package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P13[A] {
  def directEncoding(list: List[A]): List[(Int, A)] = {

    @tailrec
    def doEncode(list: List[A], n: Int, acc: List[Any]): List[(Int, A)] = (list, n, acc) match {
      case (Nil, _, acc) => acc.asInstanceOf[List[(Int, A)]]
      case (x1 :: x2 :: xs, n, acc) if x1 == x2 => doEncode(x2 :: xs, n + 1, acc)
      case (x :: xs, n, acc) => doEncode(xs, 0, acc :+ (n + 1, x))
    }

    doEncode(list, 0, Nil)
  }
}