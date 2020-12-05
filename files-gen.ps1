$day = Get-Date -Format "'day'dd"
# $day = 'day 05'

New-Item -ItemType directory "src/$day"
New-Item -ItemType file "src/$day/__init__.py"
New-Item -ItemType file "src/$day/part1.py"
New-Item -ItemType file "src/$day/part2.py"
New-Item -ItemType file "src/$day/in.txt"
