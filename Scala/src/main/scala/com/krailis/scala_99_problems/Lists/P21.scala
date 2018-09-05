package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P21[A] {
  def insertAt(elem: A, k: Int, list: List[A]): List[A] = {

    @tailrec
    def doInsert(i: Int, h: List[A], t: List[A]): List[A] = (i, h, t) match {
      case (_, h, Nil) => h
      case (0, h, xs) => (h :+ elem) ++ xs
      case (i, h, x :: xs) => doInsert(i - 1, h :+ x, xs)
    }

    doInsert(k, Nil, list)
  }
}
