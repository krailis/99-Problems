package com.krailis.scala_99_problems.Lists

object P07 {
  def flatten(list: List[Any]): List[Any] = list match {
    case (x :: xs) :: ls => flatten(x :: xs) ++ flatten(ls)
    case x :: xs => x :: flatten(xs)
    case Nil => Nil
  }
}
