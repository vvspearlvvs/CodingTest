#1회차 : 뻔 – 데기 – 뻔 – 데기 – 뻔 – 뻔 – 데기 – 데기
#2회자 : 뻔 – 데기 – 뻔 - 데기 – 뻔 – 뻔 – 뻔 – 데기 – 데기 – 데기
#n-1회차  :뻔 – 데기 – 뻔 – 데기 – 뻔(x n번) – 데기(x n번)
a=int(input())
t=int(input())
f=int(input()) #0:뻔, 1:데기

round=3 #4회차까지 간다면

guho=["뻔","데기"]
guho=guho+guho
print(guho)
for n in range(1,round):
    for i in range(n):
        guho.append(guho[0]*i+1)
print(guho)
#print(a,t,f)
