package com.krailis.scala_99_problems.Lists

class P01[A] {
  def last(list: List[A]): Option[A] = list match {
    case List() => None
    case List(x) => Some(x)
    case _ :: xs => last(xs)
  }
}
