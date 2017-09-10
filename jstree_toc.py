#!/usr/bin/env python3

import codecs
import re
import sys

jstree_code = """
  	<script type="text/JavaScript" src="_static/js/jstree.js"></script>
	<link rel="stylesheet" href="_static/js/themes/default/style.min.css" />
    <script type="text/javascript">
	  $(function() {
            $("#tocTree").jstree({ "plugins" : ["wolerow","themes","html_data","ui"]}).bind("select_node.jstree", function (e, data) {
              var href = data.node.a_attr.href;
              window.open().location.href = href;
            });

	  });
    </script>
"""

def main():
    jstree_toc(sys.argv[1])

    
def jstree_toc(infile):
    p1 = re.compile(r"^\s*<\/head>")
    p2 = re.compile(r"div class=\"toctree-wrapper compound\"")
    p3 = re.compile(r"(<li class=\"toctree-.+>)([0-9]+\.)+\s+(\S.+?)(<\/a>.*)")
    for line in codecs.open(infile, 'r', 'utf-8'):
        m = p1.search(line)
        if m != None:
            sys.stdout.buffer.write(jstree_code.encode('utf-8'))
            sys.stdout.buffer.write(line.encode('utf-8'))
            #sys.stderr.write("!!")
            #sys.stderr.write(line)
            continue

        m = p2.search(line)
        if m != None:
            sys.stdout.buffer.write("<div class=\"toctree-wrapper compound\" id=\"tocTree\">\n".encode('utf-8'))
            #sys.stderr.write("!!!")
            #sys.stderr.write(line)
            continue

        m = p3.search(line)
        if m != None:
            line = m.group(1) + m.group(3) + m.group(4) + "\n" 
            line = line.replace("href=", "target=\"new\" href=")
            sys.stdout.buffer.write(line.encode('utf-8'))
            #sys.stderr.write("!!!")
            #sys.stderr.write(line)
            continue
        
        sys.stdout.buffer.write(line.encode('utf-8'))

        



if __name__ == "__main__":
    main()
