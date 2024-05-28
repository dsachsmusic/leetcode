#? merge strings alternately

$s = "hello"

$vowels = @('a','e','i','o','u')

#pull all vowels into an array

$sAsCharArray = $s.ToCharArray() 

$vowelsInSArray = $sAsCharArray | where {$_ -in $vowels}

#create an array with the vowels from $s appearing in reverse order
$vowelsInSArrayReversed = @()

for ($i = 0; $i -lt $vowelsInSArray.count; $i++) {
    $vowelsInSArrayReversed += $vowelsInSArray[$vowelsInSArray.count-$i-1]
}

#loop through $sAsCharArray, and recreate it, the count of vowels, as they are encountered, to choose index number 

$vowelCountPlacekeeper = 0
$newS = @()
foreach ($item in $sAsCharArray) {# ($i = 0; $i -lt $sAsCharArray.count; $i++) {
    if ($item -in $vowels){
        $vowelCountPlacekeeper += 1
        $newS += $vowelsInSArrayReversed[$vowelCountPlacekeeper-1]
    }
    else {
        $newS += $item
    }
    
}
Write-Output $($newS -join "")