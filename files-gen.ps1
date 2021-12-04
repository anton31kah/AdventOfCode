$year = Get-Date -Format "'year'yyyy"
$day = Get-Date -Format "'day'dd"
# $day = 'day04'

New-Item -Path "src/$year/$day" -Name "__init__.py" -ItemType "file" -Force
Get-Content -Raw .\files-gen.template.py | New-Item -Path "src/$year/$day" -Name "part1.py" -ItemType "file"
Get-Content -Raw .\files-gen.template.py | New-Item -Path "src/$year/$day" -Name "part2.py" -ItemType "file"
New-Item -Path "src/$year/$day" -Name "in.txt" -ItemType "file"
New-Item -Path "src/$year/$day" -Name "inS.txt" -ItemType "file"
