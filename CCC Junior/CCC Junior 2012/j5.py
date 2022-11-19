n = 0

class Node:
    def __init__(self, m, l):
        self.m = m
        self.level = l

def done (move):
    global n
    i = 0
    while i < n and move[i] == str(i+1):
        i = i + 1
    return i == n 
    
def inTree(t, m):
    for x in t:
        if x.m == m:
            return True
    return False

def createNewMove (oldmove, p1, p2):
    global n
    newmove = []
    for i in range (n):
        newmove.append(oldmove[i])
        
    newmove[p2] = newmove[p1][0:1] + newmove[p2]
    newmove[p1] = newmove[p1][1:]

    if p2 < p1 and newmove[p2][0:1] == str(n):
        return oldmove
    else:
        return newmove

                                              
def search(move):
    global n
    if done(move):
        return 0
    else:
        tree = []
        queue = 0
        tree.append(Node(move,0))          
        while queue < len(tree):   
            x = tree[queue]
            queue = queue + 1
            for i in range(n):
                if i < len(m)-1:
                    if len(x.m[i+1]) == 0 or x.m[i][0:1] < x.m[i+1][0:1]:
                        newmove = createNewMove(x.m, i, i+1) 
                        if not inTree(tree, newmove):
                            tree.append(Node(newmove,x.level + 1))
                            if done(newmove):
                                return x.level + 1
                if i > 0:
                    if len(x.m[i-1]) == 0 or x.m[i][:1] < x.m[i-1][:1]:
                        newmove = createNewMove(x.m, i, i-1)
                        if not inTree(tree, newmove):
                            tree.append(Node(newmove,x.level + 1))
                            if done(newmove):
                                return x.level + 1
                          
        return "IMPOSSIBLE"     

n = int(input())
while n > 0:
    m = input().strip().split()
    print (search(m))
    n = int(input())
