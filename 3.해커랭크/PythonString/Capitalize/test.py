
#다른풀이
def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s

s= "chris alan"
r=solve(s)
print(r)
