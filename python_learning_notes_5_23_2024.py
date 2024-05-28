#find out what methods, functions (attributes?), etc. an object has with dir(something)...
#then, can call those...methods, functions (attributes)...can use ...calls(?) like string.__len__(), or string.upper()
string = "abcd"
something = string
for item in (dir(something)): print(item) 

#for interactive help: help()

#spacing...indents are 3 spaces? (not tab(?))
