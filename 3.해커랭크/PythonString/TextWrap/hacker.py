def wrap(string,max_width):
    result=[]
    for i in range(0,len(string),max_width):
        result.append(string[i:i+max_width])
    return '\n'.join(result)


string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width=4
r=wrap(string,max_width)
print(r)
'''
총길이26
0-3 4*1-1
4-7 4*2-1
8-11
12-15
16-19
20-23
24-27
24 25
'''
