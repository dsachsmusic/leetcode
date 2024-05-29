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
# note: printing integers: https://www.sololearn.com/en/Discuss/185759/printing-string-and-integer-or-float-in-the-same-line