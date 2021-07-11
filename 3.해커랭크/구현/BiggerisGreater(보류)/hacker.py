def biggerIsGreater(w):
    tmp=list(w[::-1]) #역순
    #print(tmp)
    for i in range(1,len(tmp)):
        if tmp[i-1]>tmp[i]:
            #print(tmp[i-1],tmp[i])
            for j in range(i):
                if tmp[j]>tmp[i]:
                    #print(tmp[j],tmp[i])
                    tmp[j],tmp[i] = tmp[j],tmp[i]
                    tmp=sorted(tmp[:i])[::-1]
                    print(''.join(tmp[::-1]))
                    break
            break
        else:
            print("no answer5")

w="dhck"
biggerIsGreater(w)
'''
T = int(input().strip())
for T_itr in range(T):
    w = input()
    result = biggerIsGreater(w)
'''
