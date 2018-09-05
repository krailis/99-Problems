package com.krailis.scala_99_problems.Lists

class P19[A] {
  def rotate(i: Int, list: List[A]): List[A] = i match {
    case i if i > 0 => positiveRotation(i % list.length, list)
    case i if i < 0 => negativeRotation((-i) % list.length, list)
    case _ => list
  }

  def positiveRotation(i: Int, as: List[A]): List[A] = (i, as) match {
    case (i, x :: xs) if i > 0 => positiveRotation(i - 1, xs ++ List(x))
    case (_, xs) => xs
  }

  def negativeRotation(i: Int, as: List[A]): List[A] = (i, as.reverse) match {
    case (i, x :: xs) if i > 0 => negativeRotation(i - 1, x :: xs.reverse)
    case (_, xs) => xs.reverse
  }
}
