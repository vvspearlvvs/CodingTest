#후위표기식, 계산결과
#피연산자(숫자) 만나면 push, 연산자만나면 pop

n=int(input()) #피연산자의 개수
sen=input() #후위표기식

num=[0]*n #피연산자에 대응하는 숫자값을 받음
for i in range(n):
    num[i]=int(input())
print(num)

stack=[]
for i in sen:
    if 'A'<= i <='Z': #피연산자 만나면 push
        index=ord(i)-ord('A')
        stack.append(num[index]) #ord(알파벳)=숫자 (A=65,B=66)
    else: #연산자 만나면 pop
        st2=stack.pop()
        st1=stack.pop()

        if i=='+':
            stack.append(st1+st2)
        elif i=='-':
            stack.append(st1-st2)
        elif i=='*':
            stack.append(st1*st2)
        elif i=='/':
            stack.append(st1/st2)
print('%.2f' %stack[0])
