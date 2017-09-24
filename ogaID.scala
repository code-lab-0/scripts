#!/usr/bin/env scala

import java.util.Date

// A method for seed generation (which is not depend on date/time).
// See http://npnl.hatenablog.jp/entry/20090116/1232120896
val seed: Long = Runtime.getRuntime().freeMemory();

val r = new scala.util.Random(seed)
val p = r.nextInt(100000000).toHexString

// Generates random ID looks like 2017-09-24JST-171f07058
println("%tY-%<tm-%<td%<tZ-%<tH%s".format(new Date, p)) 
