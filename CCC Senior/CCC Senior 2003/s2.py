import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
out = []
vowels = ["a", "e", "i", "o", "u"]
def rhyme(s1, s2):
    global vowels
    syllable1 = ""
    syllable2 = ""
    m1 = 0
    for i in range(len(s1)):
        if s1[i] in vowels:
            m1 = i
    m2 = 0
    for i in range(len(s2)):
        if s2[i] in vowels:
            m2 = i
    #print(s1[m1:], s2[m2:])
    
    if s1[m1:]==s2[m2:]: return True
    else: return False

for i in range(n):
    verses = [input().split()[-1].lower() for j in range(4)]
    if rhyme(verses[0], verses[1]) and rhyme(verses[2], verses[3]) and rhyme(verses[1], verses[2]):
        out.append("perfect")
    elif rhyme(verses[0], verses[1]) and rhyme(verses[2], verses[3]):
        out.append("even")
    elif rhyme(verses[0], verses[2]) and rhyme(verses[1], verses[3]):
        out.append("cross")
    elif rhyme(verses[0], verses[3]) and rhyme(verses[1], verses[2]):
        out.append("shell")
    else:
        out.append("free")

for i in out: print(i)