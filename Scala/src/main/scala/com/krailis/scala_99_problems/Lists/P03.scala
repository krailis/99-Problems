package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

@tailrec
class P03[A] {
  def nthElement(n: Int, list: List[A]): Option[A] = (n, list) match {
    case (0, x :: _) => Some(x)
    case (_, Nil) => None
    case (k, _) if k < 0 => None
    case (k, _ :: xs) => nthElement(k - 1, xs)
  }
}
