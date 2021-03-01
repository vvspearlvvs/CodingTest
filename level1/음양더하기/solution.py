a=[4,7,12]
b=[true,false,true]
for i in b:
    print(type(i))
def solution(absolutes, signs):
    answer = 123456789
    temp =[]
    for i in range(len(signs)):
        if signs[i] ==true:
            absolutes[i] = absolutes[i]*1
        elif signs[i] ==false:
            absolutes[i] = absolutes[i]*-1
    answer = sum(absolutes)
    return answer

#print(solution(a,b))
