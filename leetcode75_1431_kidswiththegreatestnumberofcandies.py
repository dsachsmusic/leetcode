#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
#1431 Kids With the Greatest Number of Candies
candies = [12,1,14]
extracandies = 10


for i in range(len(candies)):
   if i == 0:
      largestnumberfound = candies[i]
   elif candies[i] > largestnumberfound:
      largestnumberfound = candies[i]

kidWithMostCandiesCurrently = largestnumberfound

result = []
for i in range(len(candies)):
   if candies[i] + extracandies > kidWithMostCandiesCurrently:
      result += [1]
      
   else:
      result += [0]
      
result
