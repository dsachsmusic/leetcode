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
