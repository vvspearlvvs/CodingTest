def solution2(strings,n):
    strings.sort()
    return sorted(strings,key=lambda x:x[n])

print(solution2(["sun", "bed", "car"],1))
print(solution2(["abce", "abcd", "cdx"],2))

'''
새로알게 된 것
lambda http://goo.gl/IjKPF6
sorted할때 기준을 key로 잡을 수 있음
'''
