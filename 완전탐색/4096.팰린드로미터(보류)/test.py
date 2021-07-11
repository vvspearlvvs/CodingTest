def ispalin(word):
    wlist = list(word)
    n=len(wlist)
    k=[]
    for i in range(n//2):
        print(i)
        if wlist[i] == wlist[n-(i+1)]:
            #print("==")
            return 0
        else:
            print("#차이")
            k=int(wlist[n-(i+1)])-int(wlist[i]))
            a=10-k

k=ispalin("100000")
if k==0:
