chars = ["a","a","b","b","c","c","c"]

s = ""

char_sequence = []
for i in range(len(chars)):
    print("the loop is on", i)
    if i == len(chars)-1:
        s += (char_sequence[0])
        s += (str(len(char_sequence)))
        print("Added " + s[len(s)-2], s[len(s)-1] + " to string")
        print("s is", s)
        break
    if len(char_sequence) == 0:
        char_sequence = char_sequence.__add__([chars[i]])
        print("Just added a(n)", char_sequence[0] + " to an empty char_sequence")
    elif chars[i].__eq__(char_sequence[0]): 
        char_sequence = char_sequence.__add__([chars[i]])
        print("Just added another", char_sequence[0] + " to char_sequence")
        print(len(char_sequence), char_sequence[0] + " characters in a row")
    else:
        print("chars[i] is", chars[i], "current car_sequence is collecting", char_sequence[0])
        s += (char_sequence[0])
        s += (str(len(char_sequence)))
        print("Added " + s[len(s)-2], s[len(s)-1] + " to string")
        char_sequence = []
        char_sequence = char_sequence.__add__([chars[i]])
        print("Just added a(n)", char_sequence[0] + " to a newly instantiated char_sequence")