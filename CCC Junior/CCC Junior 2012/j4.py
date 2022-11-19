k=int(input())
word=input()
new_word=''

def shift(letter, q):
    if ord(letter)-q>64:
        return chr(ord(letter)-q)
    else:
        return chr(ord(letter)-q+91-65)
        
for x in range(len(word)):
    y = shift(word[x], 3*x+k+3)
    new_word=new_word+y
print(new_word)
