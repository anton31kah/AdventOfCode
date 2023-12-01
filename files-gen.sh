#!/bin/bash

year=$(date +"year%Y")
day=$(date +"day%d")
# day='day04'

mkdir -p "src/$year/$day"
touch "src/$year/$day/__init__.py"
cp files-gen.template.py "src/$year/$day/part1.py"
cp files-gen.template.py "src/$year/$day/part2.py"
touch "src/$year/$day/in.txt"
touch "src/$year/$day/inS.txt"
