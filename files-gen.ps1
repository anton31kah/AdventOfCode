$day = Get-Date -Format "'Day' dd"
$filename = "$day Binary Boarding"

# New-Item -ItemType directory "$day" 
# New-Item -ItemType file "$day/$filename (part 1).py"
# New-Item -ItemType file "$day/$filename (part 2).py"
# New-Item -ItemType file "$day/$filename.in.txt"

New-Item -ItemType file "$filename (part 1).py"
New-Item -ItemType file "$filename (part 2).py"
New-Item -ItemType file "$filename.in.txt"
