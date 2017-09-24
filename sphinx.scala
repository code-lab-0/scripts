#!/usr/bin/env scala

import scala.sys.process._


def sphinx_create(project_name: String) : Seq[String] = {
  Seq(
    "sphinx-quickstart",
    "-q", "--sep",
    "-p", project_name,
    "-a", "Osamu Ogasawara",
    "-v", "0.1")
}



def sphinx_rewrite_conf_py() : Unit = {
   val pattern1 = """^# -- General configuration -+""".r

   implicit val codec = Codec("UTF-8")
   codec.onMalformedInput(CodingErrorAction.REPLACE)
   codec.onUnmappableCharacter(CodingErrorAction.REPLACE)
 
   for (line <- Source.fromInputStream(System.in).getLines()) {
     line match {
       case pattern() => {
         println("import sys")

         println(result)
       }
       case _ => {
         println(result)
       }
     }
   } yield 
}


}



def main() : Unit = {
  val command = args(0)
  val project_name = args(1)
  if (command == "create") {
    val com = sphinx_create(project_name)
    com !
  }
}


main()
