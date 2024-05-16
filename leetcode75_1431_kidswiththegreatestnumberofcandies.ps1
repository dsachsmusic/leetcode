#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
#1431 Kids With the Greatest Number of Candies
$candies = @(12,1,12)
$extraCandies = 10

$kidWithMostCandiesCurrently = $($candies | Measure-Object -Maximum).Maximum

$result = $null 
$candies | % {
    if ($($_ + $extraCandies) -ge $kidWithMostCandiesCurrently){
        $result += @(1)
    }
    else {
        $result += @(0)
    }
}
$result