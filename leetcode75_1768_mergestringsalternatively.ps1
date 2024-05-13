#https://leetcode.com/problems/merge-strings-alternately/description/
#took about 20 minutes...used snippets as well as get-member
$word1 = "abcd"; $word2 = "pq"

$word1.ToCharArray()
$word2.toCharArray()

 $longestStringLength = $(($word1.Length, $word2.Length) | Measure-Object -Maximum).Maximum

 $mergedWord = ""
for ($i = 0; $i -lt $($longestStringLength);$i++) {
    $mergedWord += $word1[$i]
    $mergedWord += $word2[$i]
}

$mergedWord
