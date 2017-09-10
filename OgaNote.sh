#!/bin/bash

index_dir=$PWD/build/html/

make html
jstree_toc.py $index_dir/index.html > $index_dir/index2.html
mv $index_dir/index2.html $index_dir/index.html
