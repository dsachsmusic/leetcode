#? merge strings alternately

s = "hello"

vowels = ['a','e','i','o','u']

#pull all vowels into an array

s_as_char_array = list(s)

vowels_in_s_char_array = [char for char in s_as_char_array if char in vowels]

#create an array with the vowels from $s appearing in reverse order
vowels_in_s_char_array_reversed = []

for i in range(len(vowels_in_s_char_array)):
    vowels_in_s_char_array_reversed += vowels_in_s_char_array[len(vowels_in_s_char_array)-i-1]
    vowels_in_s_char_array_reversed




vowel_count_placekeeper = 0
new_s = []

for i in range(len(s_as_char_array)):
    if s_as_char_array[i] in vowels:
        vowel_count_placekeeper += 1
        new_s += vowels_in_s_char_array_reversed[vowel_count_placekeeper-1]
    else:
        new_s += s_as_char_array[i]
    
print(''.join(new_s))