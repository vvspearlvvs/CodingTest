#애너그램이면 True, 아니면 False

from collections import Counter
def isAnagram(a,b):
    acounter = Counter(a)
    bcounter = Counter(b)
    c = acounter - bcounter
    d = bcounter - acounter
    e = c + d
    if len(list(e.keys()))==0:
        return True
    return False

s = "anagram"
t = "nagaram"

s2 = "rat"
t2 = "car"
print(isAnagram(s2,t2))
