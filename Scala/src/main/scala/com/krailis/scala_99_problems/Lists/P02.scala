package com.krailis.scala_99_problems.Lists

class P02[A] {
  def lastButOne(list: List[A]): Option[A] = list match {
    case List() => None
    case List(_) => None
    case x :: _ :: Nil => Some(x)
    case _ :: xs => lastButOne(xs)
  }
}
