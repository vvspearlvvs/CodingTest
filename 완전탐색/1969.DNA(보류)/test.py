n,k=map(int,input().split())
dna_list=[]
for i in range(n):
    dna_list.append(input())
print(dna_list)

dna_dict={}
sum_hs=0
for i in range(len(dna_list)):
    for j in range(i+1,len(dna_list)):
        dna_hs=0
        for k in range(k):
            if dna_list[i][k]!=dna_list[j][k]:
                dna_hs=dna_hs+1
        print(dna_list[i]+"와"+dna_list[j]+"의 hs")
        print(dna_hs)
        sum_hs=sum_hs+dna_hs
    print(dna_list[i]+"의 전체합"+str(sum_hs))

            #    dna_dict[dna_list[i]]=dna_hs
print(dna_dict)

for k,v in dna_dict.items():
    min=v
    if min>v:
        min=v
    value = min(v)
    print(min(v))
