package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P20[A] {
  def removeAt(k: Int, list: List[A]): (List[A], Option[A]) = {

    @tailrec
    def doRemove(i: Int, h: List[A], t: List[A]): (List[A], Option[A]) = (i, h, t) match {
      case (_, h, Nil) => (h, None)
      case (0, h, x :: xs) => (h ++ xs, Some(x))
      case (i, h, x :: xs) => doRemove(i - 1, h :+ x, xs)
    }

    doRemove(k, Nil, list)
  }
}
