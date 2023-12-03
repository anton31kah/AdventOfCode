#!/bin/bash

year=$(date +"year%Y")
day=$(date +"day%d")

part=${1:-1}

# echo "src.$year.$day.part$part"

python -m "src.$year.$day.part$part"
