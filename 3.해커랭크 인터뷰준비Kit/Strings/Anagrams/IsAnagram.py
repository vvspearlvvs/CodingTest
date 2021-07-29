from collections import Counter
def isAnagram(s,t) -> bool:
    a = Counter(s)
    b = Counter(t)
    c = a - b
    d = b - a
    e = c + d
    if len(list(e.keys()))==0:
        return True
    return False
