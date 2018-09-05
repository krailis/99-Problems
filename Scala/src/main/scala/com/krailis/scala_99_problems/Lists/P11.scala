package com.krailis.scala_99_problems.Lists

class P11[A] {
  def modifiedEncoding(list: List[A]): List[Any] = {
    new P10().lengthEncoding(list).map {
      case (1, x) => x
      case l => l
    }
  }
}
