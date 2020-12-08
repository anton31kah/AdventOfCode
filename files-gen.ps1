$starterCode = "from src.common.common import get_lines`n`n`nlines = get_lines()`n"

$day = Get-Date -Format "'day'dd"
# $day = 'day04'

New-Item -Path "src/$day" -Name "__init__.py" -ItemType "file" -Force
New-Item -Path "src/$day" -Name "part1.py" -ItemType "file" -Value $starterCode
New-Item -Path "src/$day" -Name "part2.py" -ItemType "file" -Value $starterCode
New-Item -Path "src/$day" -Name "in.txt" -ItemType "file"
