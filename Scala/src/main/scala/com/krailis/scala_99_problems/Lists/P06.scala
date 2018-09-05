package com.krailis.scala_99_problems.Lists

import scala.annotation.tailrec

class P06[A] {
  def isPalindrome(list: List[A]): Boolean = list == reverse(list)

  def reverse(list: List[A]): List[A] = {

    @tailrec
    def rev(ls: List[A], acc: List[A]): List[A] = (ls, acc) match {
      case (Nil, acc) => acc
      case (x :: xs, acc) => rev(xs, x :: acc)
    }

    rev(list, Nil)
  }
}
