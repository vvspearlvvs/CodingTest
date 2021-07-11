
def mutate_string(string, position, character):
    l=list(string)
    l[int(i)]=character
    string=''.join(l)
    return string


s = input() #abracadabra
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
