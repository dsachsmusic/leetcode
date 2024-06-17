# windows install: https://docs.python.org/3/using/windows.html#windows-full (use the full installer. Perhaps check off
# the option for adding Python to PATH...however, in my experience, I needed to add Python (and pip, by the way)
# to PATH manually)
# when prompted, select to remove (disable) MAX_PATH)
# find out what methods, functions (attributes?), etc. an object has with dir(something)...
# then, can call those...methods, functions (attributes)...can use ...calls(?) like string.__len__(), or string.upper()
string = "abcd"
something = string
for item in (dir(something)): print(item) 

# for interactive help: help()

# spacing...indents are 3 spaces? (not tab(?))


# variable names and function names style should be lowercase with words separated by underscores
# https://peps.python.org/pep-0008/#function-and-variable-names

# comments first character should be a space. inline comments should start two or more spaces from code

# expanding variables within strings (printing) 
# https://www.freecodecamp.org/news/python-print-variable-how-to-print-a-string-and-variable/
# note: printing integers: 
# https://www.sololearn.com/en/Discuss/185759/printing-string-and-integer-or-float-in-the-same-line


# browse the file system https://builtin.com/data-science/python-list-files-in-directory
import os; os.listdir() # etc.

# to make a character array out of a string, can use the "list" function: list(string)

# joining (like, an array, into a string): something like the following 
# (and, below, '' could also be ',', etc.)
my_array = ['a','e','i']
print(''.join(my_array)) 

# types of loops...
# for each loop (a.k.a for in loop)
array = ["bob", "dan", "joe"]
for item in array: 
   print(item)
# for loop
array = ["bob", "dan", "joe"]
for i in range(len(array)):
   print(array[i], 'is number', i)

# understanding how += works ...as append() or extend()
# .... it works differenly depending on whether you are adding a l
# compare the results of the following
# chatGPT explaination below
# and consider just using the append/extend methods, when dealing with lists?
array_of_words = []
array_of_words += "word"
array_of_words += "anotherword"
array_of_words # results in ['w', 'o', 'r', 'd', 'a', 'n', 'o', 't', 'h', 'e', 'r', 'w', 'o', 'r', 'd']

array_of_words = []
array_of_words += ["word"]
array_of_words += ["anotherword"]
array_of_words #results in ['word', 'anotherword']

# chatGPT explaination of ^^ 
# The += operator is used for concatenation or addition with assignment.
# When used with lists, it extends the list on the left side by adding the 
# elements of the object on the right side.
# If the object on the right side is a list, its elements are added individually 
# to the list on the left side.
# If the object on the right side is a single element (like a string or a number), 
# that element is added as a single item to the list on the left side.
# Essentially, list1 += item is equivalent to list1.extend(item) when item is iterable (like a list) or 
# list1.append(item) when item is not iterable.


#spacing (style) - four spaces is the standard...but it can be anything


#slicing an array: use brackets, with two values, first value is starting point (inclusive) and second is ending point (exclusive, i.e. up to, but not including)...
array = ['zero','one','two','three']         
array[0:2]
#output: ['zero','one']


#exiting a loop: "return" is used to stop processing of functions, "break" is used to exit loops (?)