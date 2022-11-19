word = input('')
string = ''
b='a'
z='z'
f='f'
j='j'
p='p'
v='v'
e='e'
i='i'
o='o'
u='u'
def step_3(a, string):
    if a == 26:
        string = string + z
    elif a == 4:
        string = string + f
    elif a == 8:
        string = string + j
    elif a == 14:
        string = string + p
    elif a == 20:
        string = string + v
    else:
        a = int(a) + 97
        string = string + chr(a)
    return string
for x in word:
    if x == 'a' or x == 'e' or x == 'o' or x == 'i' or x == 'u':
        string = string + x
    else:
        string = string + x
        a = ord(x) - 96
        if a <= 3:
            string = string + b
        elif a <= 7:
            string = string + e
        elif a <= 12:
            string = string + i
        elif a <= 18:
            string = string + o
        else:
            string = string + u
        string = step_3(a, string)
print(string)
