#!/usr/bin/env bash
set -e

# /data/html/: Fix dir attr in HTML documents
RTL_LANGS=`grep <data/html/index.xml "dir='rtl'" | sed 's/^.* f=.\([a-z0-9_]*\).*$/\1/'`
for lang in $RTL_LANGS
do
    FILE="data/html/udhr_$lang.html"
    sed -i .orig 's/^\(.*div lang=.*\)>$/\1 dir="rtl">/' $FILE
    sed -i .orig 's/^\(.*html xmlns.*\) dir=.rtl.>$/\1>/' $FILE
done
