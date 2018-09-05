package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P12[A] {
  def listDecoding(list: List[(Int, A)]): List[A] = {

    @tailrec
    def doDecode(l: List[(Int, A)], acc: List[A]): List[A] = (l, acc) match {
      case (Nil, acc) => acc
      case ((n, x) :: xs, acc) => doDecode(xs, acc ++ List.fill(n)(x))
    }

    doDecode(list, Nil)
  }
}
