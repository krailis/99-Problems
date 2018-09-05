package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P04[A] {
  def length(list: List[A]): Int = {

    @tailrec
    def len(acc: Int, ls: List[A]): Int = ls match {
      case Nil => acc
      case _ :: xs => len(acc + 1, xs)
    }

    len(0, list)
  }
}
