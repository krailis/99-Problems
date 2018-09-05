package com.krailis.scala_99_problems.Lists

class P10[A] {
  def lengthEncoding(list: List[A]): List[(Int, A)] = {
    new P09().packConsecutive(list).map(l => (l.size, l.head))
  }
}
