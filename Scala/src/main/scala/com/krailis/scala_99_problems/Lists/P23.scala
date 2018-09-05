package com.krailis.scala_99_problems.Lists

import scala.util.Random

class P23[A] {
  def randomSelect(n: Int, ls: List[A]): List[A] = {
    val p20 = new P20[A]()
    val random = new Random()
    var outputList: List[A] = ls

    for (_ <- 1 until (ls.length - n)) {
      outputList = p20.removeAt(random.nextInt(outputList.length), outputList)._1
    }

    outputList
  }
}
