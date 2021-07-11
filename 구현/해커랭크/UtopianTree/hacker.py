#봄에는 height가 배로증
#여름에는 1씩쯩가
#처음에 1미터였을때(0,1) n년후 높이는?
'''
a0=1
an1=an0*2
an2=an1+1=(an0*2)+1
an3=an2*2=(an1+1)*2
an4=an3+1=(an2*2)+1
((an1+1)*2)+1=(((an0*2)+1)*2)+1
a5=a4*2=(an3+1)*2
((((an0*2)+1)*2)+1)*2
'''

def utopianTree(n):
    answer=0
    for i in range(n+1):
        if i%2==1:
            answer=answer*2
        elif i%2==0:
            answer=answer+1
    return answer

t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    result = utopianTree(n)
