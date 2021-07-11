def count_substring(string, sub_string):
    n=len(sub_string)
    cnt=0
    for i in range(0,len(string)-n+1):
        tmp=string[i:i+n]
        print(tmp)
        if tmp==sub_string:
            cnt+=1
    return cnt

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)
