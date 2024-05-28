#https://leetcode.com/problems/merge-strings-alternately/description/
#
word1 = "abcd"; word2 = "pq"
word1asarray = []
for i in range(len(word1)):
   word1asarray+=word1[i]

word2asarray = []
for i in range(len(word2)):
   word2asarray+=word2[i]
   
if len(word1asarray).__gt__(len(word2asarray)):
   longeststringlength = len(word1asarray)
else:
   longeststringlength = len(word2asarray)

mergedword = ""
for i in range(longeststringlength):
   print(i)
   if len(word1asarray) >= i+1:
      mergedword = mergedword.__add__(word1[i])
   if len(word2asarray) >= i+1:
      mergedword = mergedword.__add__(word2[i])

print(mergedword)
