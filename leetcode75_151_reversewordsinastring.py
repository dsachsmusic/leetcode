#? string compression

s = "  hello world  "


#make an array of the words 
s_as_array = s.split() #in python, split defaults to space character for splitting, removes leading/trailing

#create new array of words, using count of words in original array to reverse-index (so to speak)
s_as_array_reversed = []
for i in range(len(s_as_array)):
    s_as_array_reversed.append(s_as_array[len(s_as_array)-i-1])


print(' '.join(s_as_array_reversed))