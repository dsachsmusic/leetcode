#? string compression

$s = "  hello world  "

#make an array of the words in s, by splitting the string at any space character...
#and then removing any space characters from the array
$sAsArray = $s -split " " | where { $_ -ne ""}

#create new array of words, using count of words in original array to reverse-index (so to speak)
$sAsArrayReversed = @()
for ($i = 0; $i -lt $sAsArray.count; $i++) {
    $sAsArrayReversed += @($sAsArray[$sAsArray.count-$i-1])
}

$sAsArrayReversed -join " "
