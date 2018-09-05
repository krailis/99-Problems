package com.krailis.scala_99_problems.Lists

import scala.util.Random

class P25[A] {
  def randomPermute(ls: List[A]): List[A] = {
    Random.shuffle(ls)
  }
}
