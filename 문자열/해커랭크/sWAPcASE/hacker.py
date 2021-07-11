#lowwer->upper, upper->lower
def swap_case(s):
    result=""
    for i in s:
        if i.isalpha():
            if i.isupper():
                result+=i.replace(i,i.lower())
            elif i.islower():
                result+=i.replace(i,i.upper())
        else:
            result+=i
    return result


s="Www.HackerRank.com"
print(swap_case(s))
