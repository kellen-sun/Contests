n=int(input())
def suffix(a,b):
    if a==b:
        return True
    elif len(a)>len(b):
        if a[len(a)-len(b):]==b:
            return True
    elif len(a)<len(b):
        if b[len(b)-len(a):]==a:
            return True
    return False

def prefix(a,b):
    if a==b:
        return True
    elif len(a)>len(b):
        if a[:len(b)]==b:
            return True
    elif len(a)<len(b):
        if b[:len(a)]==a:
            return True
    return False
    
print(prefix('ab','about'))
