#https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
#note: this is not a perfect answer....it has issues
$str1 = "ABCABC"
$str2 = "ABCABCABCABC"

$shorterString = $str1, $str2 | where {$_.length -eq $($str1.Length, $str2.Length | Measure-Object -Minimum).Minimum}
$longerString = $str1, $str2 | where {$_.length -eq $($str1.Length, $str2.Length | Measure-Object -Maximum).Maximum}


for ($i = $shorterString.length; $i -ge 0; $i--) {
   $shorterStringBaseTry = $shorterstring[0..$i] -join ""
   $shorterStringBaseTryTest = $null
   if ($longerString.Length%$shorterStringBaseTry.Length -eq 0){
        for ($j = 1; $j -le $($longerString.length/$shorterStringBaseTry.Length); $j++){
            
            $shorterStringBaseTryTest += $shorterStringBaseTry
        }

       if ($shorterStringBaseTryTest -eq $longerString){
            Write-OUtput "$shorterStringBaseTry"
            Return
       }
    }
}


