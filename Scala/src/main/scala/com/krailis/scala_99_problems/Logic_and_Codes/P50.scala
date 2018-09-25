package com.krailis.scala_99_problems.Logic_and_Codes

import scala.annotation.tailrec

object P50 {
  def grayCode(n: Int): List[String] = {
    @tailrec
    def doGrayCode(i: Int, acc: List[String]): List[String] = (i, acc) match {
      case (0, ls) => ls
      case (j, ls) => doGrayCode(j-1, ls.map(x => "0" + x) ::: ls.reverse.map(x => "1" + x))
    }

    doGrayCode(n-1, List("0", "1"))
  }
}
